import boto3

# Replace with your actual AWS credentials
# Commenting out for me since my AWS credentials are already set.
#aws_access_key_id = 'YOUR_ACCESS_KEY_ID'
#aws_secret_access_key = 'YOUR_SECRET_ACCESS_KEY'
#region_name = 'YOUR_REGION'

# Initialize a session using Amazon DynamoDB
dynamodb = boto3.client(
    'dynamodb',
    #aws_access_key_id=aws_access_key_id,
    #aws_secret_access_key=aws_secret_access_key,
   # region_name=region_name
)

# Create a DynamoDB table
table_name = 'ItalianFood'

# Define the table schema and properties
try:
    dynamodb.create_table(
        TableName=table_name,
        KeySchema=[
            {
                'AttributeName': 'FoodID',
                'KeyType': 'HASH'  # Partition key
            },
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'FoodID',
                'AttributeType': 'S'
            },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )
    print(f"Table {table_name} created successfully.")
except dynamodb.exceptions.ResourceInUseException:
    print(f"Table {table_name} already exists.")

# Wait until the table exists.
dynamodb.get_waiter('table_exists').wait(TableName=table_name)
print(f"Table {table_name} is now active.")

# Initialize a DynamoDB resource for adding items
dynamodb_resource = boto3.resource(
    'dynamodb',
  #  aws_access_key_id=aws_access_key_id,
   # aws_secret_access_key=aws_secret_access_key,
   # region_name=region_name
)

table = dynamodb_resource.Table(table_name)

# List of Italian food items to add
italian_food_items = [
    {'FoodID': '1', 'Name': 'Pizza Margherita', 'Ingredients': 'Tomato, Mozzarella, Basil', 'Price': '8.99'},
    {'FoodID': '2', 'Name': 'Spaghetti Carbonara', 'Ingredients': 'Spaghetti, Eggs, Pancetta, Pecorino Cheese', 'Price': '12.50'},
    {'FoodID': '3', 'Name': 'Lasagna', 'Ingredients': 'Lasagna Noodles, Ground Beef, Tomato Sauce, Ricotta, Mozzarella', 'Price': '14.00'},
    {'FoodID': '4', 'Name': 'Tiramisu', 'Ingredients': 'Mascarpone, Coffee, Ladyfingers, Cocoa', 'Price': '6.00'},
    {'FoodID': '5', 'Name': 'Ravioli', 'Ingredients': 'Pasta Dough, Ricotta, Spinach', 'Price': '10.00'},
    {'FoodID': '6', 'Name': 'Risotto', 'Ingredients': 'Arborio Rice, Parmesan, White Wine, Broth', 'Price': '11.00'},
    {'FoodID': '7', 'Name': 'Gelato', 'Ingredients': 'Milk, Sugar, Various Flavors', 'Price': '5.00'},
    {'FoodID': '8', 'Name': 'Focaccia', 'Ingredients': 'Flour, Olive Oil, Salt, Rosemary', 'Price': '4.50'},
    {'FoodID': '9', 'Name': 'Gnocchi', 'Ingredients': 'Potatoes, Flour, Egg', 'Price': '9.50'},
    {'FoodID': '10', 'Name': 'Caprese Salad', 'Ingredients': 'Tomato, Mozzarella, Basil, Olive Oil', 'Price': '7.00'}
]

# Add each item to the DynamoDB table
for item in italian_food_items:
    table.put_item(Item=item)
    print(f"Added item: {item['Name']}")

# Scan the table to retrieve all items
response = table.scan()
items = response['Items']

print("Scanning the table for all items...")
for item in items:
    print(item)
