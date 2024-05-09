import boto3

cidr_block = "10.20.1.0/24"
vpc_id = "vpc-0399d7accc08c5af3"

ec2 = boto3.client("ec2")


subnet = ec2.create_subnet(
    CidrBlock=cidr_block, VpcId=vpc_id)

print(subnet["Subnet"]["SubnetId"])