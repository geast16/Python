import boto3
ec2 = boto3.client("ec2")

route_table_id = 'rtb-0527b55d791324802'

ec2.delete_route(
    DestinationCidrBlock='0.0.0.0/0',
    RouteTableId=route_table_id,
)
