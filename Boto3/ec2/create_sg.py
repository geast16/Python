import boto3 #Always import the boto3 library at the beginning of your code.

ec2 = boto3.client("ec2")

response = ec2.create_security_group(
    Description='My security group',
    GroupName='my-security-group',
    VpcId='vpc-0e84e4ec0276690ed',
)

print(response["GroupId"])