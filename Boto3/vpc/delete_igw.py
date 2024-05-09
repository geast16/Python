import boto3
ec2 = boto3.client("ec2")

internet_gateway_id = "igw-06c14abbae5acbbb4"

ec2.delete_internet_gateway(
    InternetGatewayId=internet_gateway_id,
)
