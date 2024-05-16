import boto3

# Create a DynamoDB resource object
dynamodb = boto3.resource('dynamodb')

# Define the table name
table_name = 'ItalianFood'

# Create the table
table = dynamodb.create_table(
    TableName=table_name,
    KeySchema=[
        {
            'AttributeName': 'ID',
            'KeyType': 'HASH'  # Partition key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'ID',
            'AttributeType': 'N'  # Numeric
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

# Wait until the table exists
table.meta.client.get_waiter('table_exists').wait(TableName=table_name)

# Now, let's add some items to the table
with table.batch_writer() as batch:
    batch.put_item(Item={'ID': 1, 'Name': 'Margherita Pizza'})
    batch.put_item(Item={'ID': 2, 'Name': 'Risotto'})
    batch.put_item(Item={'ID': 3, 'Name': 'Tiramisu'})
    batch.put_item(Item={'ID': 4, 'Name': 'Osso Buco'})
    batch.put_item(Item={'ID': 5, 'Name': 'Panna Cotta'})
    batch.put_item(Item={'ID': 6, 'Name': 'Caprese Salad'})
    batch.put_item(Item={'ID': 7, 'Name': 'Arancini'})
    batch.put_item(Item={'ID': 8, 'Name': 'Bistecca alla Fiorentina'})
    batch.put_item(Item={'ID': 9, 'Name': 'Pesto Pasta'})
    batch.put_item(Item={'ID': 10, 'Name': 'Cannoli'})

# Now let's scan the table
response = table.scan()
items = response['Items']
print("Scanned Items:")
for item in items:
    print(item)

# Query the table
response = table.query(
    KeyConditionExpression=boto3.dynamodb.conditions.Key('ID').eq(1)
)
item = response['Items'][0]
print("Queried Item:")
print(item)

# Remove an item from the table
table.delete_item(
    Key={
        'ID': 10
    }
)

# Delete the table
table.delete()