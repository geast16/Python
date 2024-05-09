import boto3
ec2 = boto3.client("ec2")

internet_gateway_id = "igw-06c14abbae5acbbb4"
vpc_id = "vpc-0399d7accc08c5af3"

ec2.attach_internet_gateway(    #No need to store a response since there is no response
    InternetGatewayId=internet_gateway_id,
    VpcId=vpc_id,
)