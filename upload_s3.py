import boto3

s3 = boto3.client('s3')

bucket_name = "sarthak-bucket-9216"

file_name = "localfile.txt"
s3_file_name = "uploadedfile.txt"

s3.upload_file(file_name, bucket_name, s3_file_name)

print("File uploaded successfully to S3 🚀")