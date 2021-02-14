import json
from boto3 import client, resource


# Parameters
database = 'dynamodb'
table_name = 'data'
endpoint_url = 'http://localhost:8000'
region_name = 'us-west-2'
creds = "anything"

# Load the data
with open("data.json",encoding="utf8") as f:
    json_data = json.load(f)

# Create Database Client
print('Creating Database Client....',end='')
ddb_client = client(
                    database,
                    endpoint_url=endpoint_url,
                    region_name=region_name,
                    aws_access_key_id=creds,
                    aws_secret_access_key=creds
                )
print('Done')

# Create Database Schema
print('Creating Database Schema....', end='')
response = ddb_client.create_table(
    AttributeDefinitions=[
        {
            'AttributeName': 'bookID',
            'AttributeType': 'S'
        },  
    ],
    TableName=table_name,
    KeySchema=[
        {
            'AttributeName': 'bookID',
            'KeyType': 'HASH'
        },
    ],
    BillingMode='PAY_PER_REQUEST',
)
print('Done')

# Create Table
print(f'Creating Table -> {table_name} ....', end='')
ddb = resource(
            database,
            endpoint_url=endpoint_url,
            region_name=region_name,
            aws_access_key_id=creds,
            aws_secret_access_key=creds
        ).Table(table_name)
print('Done')

# Write Batch to Database
print(f'There are total {len(json_data)} items.')

print(f'Inserting data into table - {table_name}')
with ddb.batch_writer() as batch:
    for i,item in enumerate(json_data):
        if i%1000 == 0:
            print(f'{i} items are inserted')
        batch.put_item(Item=item)
print('Done')
