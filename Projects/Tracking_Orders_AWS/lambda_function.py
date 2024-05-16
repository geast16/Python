import boto3
import random

def lambda_handler(event, context):
    # Initialize the SQS client
    sqs = boto3.client('sqs', region_name='us-east-1')  # Specify your AWS region here

    # Define the queue URL (replace with your actual SQS queue URL)
    queue_url = 'https://sqs.us-east-1.amazonaws.com/583043870476/customer_order_queue'

    # Generate a random number (change this logic as needed)
    random_number = random.randint(1, 100)

    # Create a message with the random number
    message = f"Random Number: {random_number}"

    # Send the message to the SQS queue
    response = sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=message
    )

    # Print the response for logging (optional)
    print("Message sent to SQS:", response)

    return {
        'statusCode': 200,
        'body': 'Message sent to SQS'
    }