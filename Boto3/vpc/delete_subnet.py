import boto3
ec2 = boto3.client("ec2")

subnet_id = "subnet-06b57b7cea6fdd3f9"
response = ec2.delete_subnet(
    SubnetId=subnet_id,
)
