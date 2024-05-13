import boto3 #Always import the boto3 library at the beginning of your code.

ami_id = "ami-0615d2381591490c6"
key_pair_name = "Key from Boto3"
security_group_id = "sg-0ca4657b1b65cfe79"

ec2 = boto3.client("ec2")

response = ec2.run_instances(
    ImageId=ami_id,
    InstanceType='t2.micro',
    KeyName=key_pair_name,
    MaxCount=1,
    MinCount=1,
    SecurityGroupIds=[
        security_group_id
    ],
    TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [
                    {
                        'Key': 'Created from',
                        'Value': 'Boto3',
                    },
                ],
            },
        ],
    )
print(response["Instances"][0]['InstanceId'])