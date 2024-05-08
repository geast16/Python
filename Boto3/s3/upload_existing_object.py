import boto3

s3 =  boto3.client('s3')

s3.upload_file('test_text.txt', 'geast-boto3-05062024', 'test_text_upload.txt', ExtraArgs={"ContentType":"text/plain"}) #Extra Args is a dictionary, key value pair.