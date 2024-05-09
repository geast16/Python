import boto3 #Always import the boto3 library at the beginning of your code.
ec2 = boto3.client("ec2")


response = ec2.describe_key_pairs()
for keypair in response["KeyPairs"]: #iterate through KeyPairs
    print(keypair["KeyName"], keypair["KeyPairId"])