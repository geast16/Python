import boto3

s3 = boto3.client('s3')

s3.put_object(Bucket="geast-boto3-05062024", 
              Key="folder/foldera/folder1/test_text_spring", #create an object in a nested folder
              Body="Hey this is a string, not a spring.",
              ContentType="text/plain")