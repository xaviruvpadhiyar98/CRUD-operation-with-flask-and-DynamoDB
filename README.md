# BASIC CURD APP FLASK AND DYNAMODB

## Start DynamoDB database with  - 

```
java -Djava.library.path=./DynamoDBLocal_lib -jar DynamoDBLocal.jar
```

## Load The Database

```
python import_data.py
```

## Run the Flask App

```
python app.py
```

## ALL ENDPOINTS
* url1 = "http://localhost:5000/add_book"
* url2 = "http://localhost:5000/get_book/10"
* url3 = "http://localhost:5000/update_book/10"
* url4 = "http://localhost:5000/remove_book/10"

## TEST all the ENDPOINT

### Create an Item in DynamoDB.
```python
data = {
    'authors': 'J.K. Rowling',
    'average_rating': '4.20',
    'bookID': '10',
    'isbn': '439827604',
    'language_code': 'eng',
    'price': '100',
    'ratings_count': '27410',
    'title': 'Harry Potter Collection (Harry Potter  #1-6)'
}
response = requests.post(url4, data=json.dumps(data))
print(response.text)
```

### Read an Item from DynamoDB.
```python
response = requests.get(url2)
print(response.text)
```

### Update an Item from DynamoDB.
```python
data = {
    'price': '100',
    'average_rating': '4.20'
}
response = requests.post(url3, data=json.dumps(data))
print(response.text)
```

### Delete an Item from DynamoDB.
```python
response = requests.get(url4)
print(response.text)
```