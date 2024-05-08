import boto3
s3 = boto3.client("s3")

response = s3.generate_presigned_url('get_object', Params={'Bucket': "geast-boto3-05062024", 'Key': "test_text.txt"}, ExpiresIn=300) #Expiration is in seconds 300 = 5 mins.

print(response)