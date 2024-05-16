import boto3

# Create SQS client
sqs = boto3.client('sqs')

#Define the queue name
queue_name = "customer_order_queue"

# Create a new SQS queue
response = sqs.create_queue(
    QueueName= queue_name
)

# Print the queue URL
print("SQS queue URL:", response['QueueUrl'])
