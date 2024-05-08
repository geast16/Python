import boto3

def filter_objects_extension(client, bucket, extention):
    keys = []
    response = client.list_objects_v2(Bucket=bucket)
    for content in response["Contents"]:
        if(extention in content ["Key"][-(len(extention)):]):
            keys.append(content["Key"])
    return keys

def list_object_keys(client, bucket, prefix=""): #Function being defined
    keys = []
    response = client.list_objects_v2(Bucket=bucket, Prefix=prefix)
    for content in response["Contents"]:#for loop
        keys.append(content["Key"])
    return keys

if __name__ == "__main__":
    s3 = boto3.client("s3")

    response = list_object_keys(s3, "geast-boto3-05062024", "folder/")
    print(response)

    response = filter_objects_extension(s3, "geast-boto3-05062024", "/")
    print(response)