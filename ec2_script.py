import boto3

# Connect to EC2
ec2 = boto3.resource('ec2', region_name='ap-south-1')

# Launch instance
instance = ec2.create_instances(
    ImageId='ami-0bc7aabcf58d1e02a',  # Valid AMI
    MinCount=1,
    MaxCount=1,
    InstanceType='t3.micro',
    KeyName='my-key2'   # Your key pair name
)

print("EC2 Instance launched:", instance[0].id)