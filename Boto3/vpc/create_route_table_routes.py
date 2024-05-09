import boto3
ec2 = boto3.client("ec2")

gateway_id = 'igw-06c14abbae5acbbb4'
route_table_id = 'rtb-0527b55d791324802'

ec2.create_route(
    DestinationCidrBlock='0.0.0.0/0',
    GatewayId=gateway_id,
    RouteTableId=route_table_id,
)