import boto3

# create a s3 resource
s3 = boto3.resource('s3')

# get all the buckets name
for bucket in s3.buckets.all():
    print(bucket.name)

