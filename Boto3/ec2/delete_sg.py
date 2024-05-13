import boto3

ec2 = boto3.client('ec2')


response = ec2.delete_security_group(
    GroupId='sg-0ca4657b1b65cfe79',
)

print(response)