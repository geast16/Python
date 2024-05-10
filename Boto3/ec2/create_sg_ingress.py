import boto3 #Always import the boto3 library at the beginning of your code.

ec2 = boto3.client("ec2")

security_group_id = "sg-0ca4657b1b65cfe79"

response = ec2.authorize_security_group_ingress(
    GroupId=security_group_id,
    IpPermissions=[
        {
            'FromPort': 22,
            'IpProtocol': 'tcp',
            'IpRanges': [
                {
                    'CidrIp': '0.0.0.0/0',
            
                },
            ],
            'ToPort': 22,
        },
        {
            'FromPort': 80,
            'IpProtocol': 'tcp',
            'IpRanges': [
                {
                    'CidrIp': '0.0.0.0/0',
            
                },
            ],
            'ToPort': 80,
        },
    ],
)

print(response)