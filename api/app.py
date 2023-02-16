"""Main app file"""
from flask import Flask, request, json
from base import Base, Session, engine
from task import Task
from flask_cors import CORS
import sqlalchemy

app = Flask('__name__')
CORS(app)

Base.metadata.create_all(engine)

# Home route to check health
@app.route('/')
def root():
    return 'api is running'

# Create task endpoint
@app.route('/create', methods=["POST"])
def create():
    """
    body of the request is of the format - {"task": "name of task"}
    """
    data = request.json
    session = Session()
    if not 'task' in data.keys():
        return {'result': "Error, please provide a key with 'task'"}
    try:
        new_task = Task(name=data['task'])
        
        session.add(new_task)
        session.commit()
        session.close()
        
        return {'result': f'successfully inserted task {data["task"]}'}
    
    except sqlalchemy.exc.IntegrityError:
        return {'error': f'Task {data["task"]} already exists'}

# Delete task endpoint
@app.route('/delete', methods=["DELETE"])
def delete():
    """
    body of the request is of the format - {"task": "name of task"}
    """
    data = request.json

    if not 'task' in data.keys():
        return {'result': "Error, please provide a key with 'task'"}
    session = Session()

    to_delete = data['task']
    
    session.query(Task).filter(Task.name == to_delete).delete()
    session.commit()
    session.close()

    return {'result': f'successfully deleted task {to_delete}'}

# Read tasks endpoint
@app.route('/read', methods=["GET"])
def read():
    session = Session()
    tasks = session.query(Task).all()

    return [{'task':task.name, 'completed': task.completed} for task in tasks]

# Update task endpoint
@app.route('/update', methods=['PUT'])
def update():
    """
    body of the request is of the format - {"task": "name of task"}
    """

    data = request.json

    if not 'task' in data.keys():
        return {'result': "Error, please provide a key with 'task'"}
    
    to_update = data['task']
    session = Session()
    t = session.query(Task).filter(Task.name == to_update).first()
    if t is None:
        return {'result': f'task {to_update} does not exist'}
    status = t.completed
    setattr(t, 'completed', not t.completed)
    
    session.commit()
    session.close()
    return {'result': f'updated task {to_update} to {not status}'}


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)