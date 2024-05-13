import boto3

ec2 = boto3.client('ec2')


response = ec2.deregister_image(
    ImageId='ami-0615d2381591490c6'
)