from flask import Flask, request, json
from base import Base, Session, engine
from task import Task
from flask_cors import CORS
import sqlalchemy

app = Flask('__name__')
CORS(app)

Base.metadata.create_all(engine)

@app.route('/')
def root():
    return 'api is running'

@app.route('/create', methods=["POST"])
def create():
    
    session = Session()
    try:
        data = request.json
        new_task = Task(name=data['task'])
        
        session.add(new_task)
        session.commit()
        session.close()
        
        return {'result': f'successfully inserted task {data["task"]}'}
    
    except sqlalchemy.exc.IntegrityError:
        return {'error': f'Task {data["task"]} already exists'}

@app.route('/delete', methods=["DELETE"])
def delete():
    session = Session()

    data = request.json
    to_delete = data['task']
    
    session.query(Task).filter(Task.name == to_delete).delete()
    session.commit()
    session.close()

    return {'result': f'successfully deleted task {to_delete}'}

@app.route('/read', methods=["GET"])
def read():
    session = Session()
    tasks = session.query(Task).all()

    return [{'task':task.name, 'completed': task.completed} for task in tasks]

@app.route('/update')
def update():
    data = request.json
    to_update = data['task']
    session = Session()
    t = session.query(Task).filter(Task.name == to_update).first()
    status = t.completed
    setattr(t, 'completed', not t.completed)
    session.commit()
    session.close()
    return {'result': f'updated task {to_update} to {not status}'}

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)