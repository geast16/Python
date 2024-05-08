import boto3

ec2 = boto3.resource('ec2')


response = ec2.describe_vpcs()

print(response)