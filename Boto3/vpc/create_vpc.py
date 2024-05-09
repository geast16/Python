import boto3
ec2 = boto3.client("ec2")


vpc = ec2.create_vpc(
    CidrBlock='10.20.0.0/16')

print(vpc["Vpc"]["VpcId"])