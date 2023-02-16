# DUBDUB API

## Stack
Flask framework to build the required API. <br>
PostgreSQL database running on a docker container to store data.

- [x] API for CRUD operations using Flask.
- [x] API endpoint to mark tasks as completed/not completed. 
- [x] Persist data into a data source - I have used postgres SQL database running on a docker container.
- [x] Documentation
- [x] Dockerise the application. 

## Steps to run
1. Make sure docker is running
2. ``` docker pull postgres ```
3. ``` docker compose build --no-cache ```
4. ``` docker compose up ```
5. API will now be running at <b>http://localhost:5050</b>
   
## Endpoints
1. /create - (only POST allowed)
2. /read - (only GET allowed)
3. /update - (only PUT allowed)
4. /delete - (only DELETE allowed)
5. / - (All methods allowed)