from boto3.dynamodb.conditions import Key,Attr,And
from boto3 import resource

from flask import Flask, request


app = Flask(__name__)

table_name = 'data'
data_table = resource('dynamodb',
                    endpoint_url='http://localhost:8000',
                    region_name='us-west-2',
                    aws_access_key_id="anything",
                    aws_secret_access_key="anything"
                ).Table(table_name)


@app.route('/', methods = ['GET'])
def hello():
    return "Hello World!"

# CREATE OPERATION
@app.route('/add_book', methods = ['POST','GET'])
def add_book():
    if request.method == 'POST':
        request_info = request.get_json(force=True)
        response = data_table.put_item(Item=request_info)
        return 'Book Added Successfully'
    else:
        return ('''This is the GET Request</br>
        format - ></br>
            {'language_code': 'eng',</br>
            'price': '123',</br>
            'isbn': '123456789,</br>
            'average_rating': '1.23',</br>
            'title': 'Title Goes Here',</br>
            'ratings_count': '123456',</br>
            'bookID': '12345',</br>
            'authors': 'Author names'</br>}
        ''')


# READ OPERATION
@app.route('/get_book/<bookID>', methods = ['GET'])
def get_book(bookID):
    response = data_table.query(
            KeyConditionExpression=Key('bookID').eq(str(bookID))
        )
    try:
        return response['Items'][0]
    except:
        return 'Book not found'

# Update Operation
@app.route('/update_book/<bookID>', methods = ['POST'])
def update_book(bookID):
    request_from_web = request.get_json(force=True)
    response_from_db = data_table.query(
            KeyConditionExpression=Key('bookID').eq(str(bookID))
        )
    response = response_from_db['Items'][0]
    response.update(request_from_web)
    update_response = data_table.put_item(Item=response)
    return f'Updated Successfully'


# Delete Operation
@app.route('/remove_book/<bookID>', methods = ['GET'])
def remove_favourite(bookID):
    response = data_table.delete_item(Key={'bookID':bookID})
    print(response)
    return 'Book Deleted Successfully'


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)