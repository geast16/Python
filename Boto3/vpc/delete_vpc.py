import boto3
ec2 = boto3.client("ec2")

vpc_id = 'vpc-0399d7accc08c5af3' #always use environment variables instead of hardcording variables

ec2.delete_vpc(
    VpcId=vpc_id,
)
