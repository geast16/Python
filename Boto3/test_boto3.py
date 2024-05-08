import boto3

s3 = boto3.client('s3')

response = s3.create_bucket(
    Bucket='geast-boto3-05062024'
)

print(response)