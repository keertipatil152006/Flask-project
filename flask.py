from os import name
from flask import Flask
from flask.json import jsonify
from werkzeug.wrappers import request
app=Flask(__name__)
tasks=[
    {
        'id':1,
        'contact':'9876573490',
        'name':'Rahul',
        'done':False
    },
    {
        'id':2,
        'contact':'9876573491',
        'name':'Raju',
        'done':False
    }
]
@app.route('/')
def hello_world():
    return 'Hello World'
@app.route('/add-data',methods=['POST'])
def add_task():
    if not request.json:
        return jsonify({
            'status':'error',
            'message':'please provide the data'

        },400)
    contact={
        'id':tasks[-1]['id']+1,
        'name':request.json['name'],
        'contact':request.json.get('contact',''),
        'done':False
    }
    tasks.append(name)
    return jsonify({
        'status':'success',
        'message':'task added successfully'
    })
@app.route('/get-data')
def get_task():
    return jsonify({
        'data':tasks
    })
if (__name__=='__main__'):
    app.run(debug=True)