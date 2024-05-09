import boto3

ec2 = boto3.client("ec2")

response = ec2.describe_internet_gateways()


for igw in response["InternetGateways"]:
    print(igw["InternetGatewayId"])
    for attachment in igw["Attachments"]:
        print(attachment["VpcId"], attachment["State"])