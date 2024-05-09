import boto3
ec2 = boto3.client("ec2")
route_table_id = 'rtb-0527b55d791324802'
subnet_id = 'subnet-06b57b7cea6fdd3f9'

subnet_association = ec2.associate_route_table(
    RouteTableId=route_table_id,
    SubnetId=subnet_id,
)

print(subnet_association["AssociationId"])