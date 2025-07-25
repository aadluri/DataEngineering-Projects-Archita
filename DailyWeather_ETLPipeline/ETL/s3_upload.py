import boto3

s3 = boto3.client('s3')

def upload_to_s3(local_path, bucket, s3_path):
    s3.upload_file(local_path, bucket, s3_path)