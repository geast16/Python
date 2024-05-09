import boto3 #Always import the boto3 library at the beginning of your code.
ec2 = boto3.client("ec2")

response = ec2.create_image(

    InstanceId='i-01abb92c75a236299',
    Name='SSH-Project',
)

print(response["ImageId"])