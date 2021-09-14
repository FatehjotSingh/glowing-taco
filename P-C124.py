from flask import Flask, jsonify, request

app = Flask(__name__)
tasks = [{
    'id':1,
    'contact':u'9876456345',
    'name':u'person 1',
    'done':False
},{
    'id':2,
    'contact':u'9234283182',
    'name':u'person 2',
    'done':False
}]

@app.route('/add-contact', methods = ["POST"])

def add_contact():
    if not request.json:
        return jsonify({
            'status':'ERROR',
            'message':'Please provide the data'
        },400)

    task = {
        'id':tasks[-1]['id'] +1,
        'contact':request.json['contact'],
        'name':request.json.get('name',""),
        'done':False,
        }

    tasks.append(task)

    return jsonify({
        'status':'SUCCESS',
        'message':'contact added successfully'
    })

@app.route('/get-contact')

def get_contact():
    return jsonify({
        'data':tasks,
    })

if __name__ == '__main__':
    app.run(debug = True)
