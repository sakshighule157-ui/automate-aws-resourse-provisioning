import boto3

s3 = boto3.client('s3')

bucket_name = "sarthak-bucket-9216"

response = s3.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={
        'LocationConstraint': 'ap-south-1'
    }
)

print("S3 Bucket created:", bucket_name)