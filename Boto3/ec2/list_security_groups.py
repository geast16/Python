import boto3 #Always import the boto3 library at the beginning of your code.
ec2 = boto3.client("ec2")

response = ec2.describe_security_groups()

for sg in response["SecurityGroups"]:
    print(sg["GroupId"], sg["VpcId"], sg["GroupName"], sg["Description"])


    for permission in sg["IpPermissions"]:
        if "FromPort" in sg:
            print(permission["FromPort"])

        if "IpProtocol" in sg:
            print(permission["IpProtocol"])

        if "ToPort" in sg:
            print(permission["ToPort"])
        
        if "IpRanges" in sg:
            for iprange in permission["IpRanges"]:
                print(iprange["CidrIp"])