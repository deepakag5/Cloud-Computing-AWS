# import boto library
import boto3

# create a s3 resource
s3 = boto3.resource('s3')

# get all the buckets name
for bucket in s3.buckets.all():
    print(bucket.name)

# retrive object name from the given bucket
bucket_name = "census.us.data"
bucket_obj = s3.Bucket(name=bucket_name)

print("bucket "+bucket_name+" has below objects")
for obj in bucket_obj.objects.all():
    print(obj.key)


# downloading a file from bucket
file_name = 'census_data_2017.RData'
s3.Object(bucket_name, file_name).download_file(file_name)

# create a bucket in s3
new_bucket_name = "census.us.data.new"

s3.create_bucket(Bucket=new_bucket_name)


