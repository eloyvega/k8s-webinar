import os
import uuid
import time
import calendar

from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import pymongo


app = Flask(__name__)
cors = CORS(app, resources={r'*': {'origins': '*'}})

mongo_client = pymongo.MongoClient(os.environ['MONGO_URI'])
db = mongo_client['todo']
tasks = db['tasks']


@app.route('/')
def hello():
    return 'API is responding'


@app.route('/api/insert_task', methods=['POST'])
def insert_task():
    record = request.get_json()
    record['_id'] = str(uuid.uuid4())
    record['id'] = record['_id']
    record['timestamp'] = str(calendar.timegm(time.gmtime()))
    print(record)
    response_object = {
        'status': 0,
        'task': record
    }
    try:
        tasks.insert_one(record)
        response_object['status'] = 200
    except Exception as e:
        print(e)
        response_object['status'] = 400
    return jsonify(response_object)


@app.route('/api/get_tasks')
def get_tasks():
    try:
        response = tasks.find().sort('timestamp', -1)
        result = [item for item in response]
        print(result)
        return jsonify(result)
    except Exception as e:
        print(e)
        return jsonify([])
