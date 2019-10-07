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

# upload a file to the bucket in s3 and also provide encryption and Access Control for public read
s3.Object(new_bucket_name, file_name).upload_file(file_name, ExtraArgs={'ServerSideEncryption':'AES256', 'ACL':'public-read'})


# copying file between buckets
def copy_to_bucket(bucket_from, bucket_to, file_name):
    copy_resource = {
        'Bucket' : bucket_from,
        'Key' : file_name
    }

    s3.Object(bucket_to, file_name).copy(copy_resource)


FILE_TO_COPY = "20190303_cnty_acs_2013_2017_absolute_values.csv"
copy_to_bucket(bucket_name,new_bucket_name,FILE_TO_COPY)


# deleting a object (file) from s3
FILE_TO_DELETE = "20190303_cnty_acs_2013_2017_absolute_values.csv"
s3.Object(new_bucket_name, FILE_TO_DELETE).delete()

## delete a bucket

# to delete a non-empty bucket all its objects and their versions must be removed
def delete_all_obj(bucket_name):

    # create a empty list to hold objects
    list_obj = []

    # get the bucket name
    bucket = s3.Bucket(bucket_name)

    # get name of all the objects along with their versions
    for obj_ver in bucket.object_versions.all():
        list_obj.append({'Key':obj_ver.object_key,
                         'VersionId':obj_ver.id})

    # print list of objects to be deleted
    print(list_obj)

    # delete all objects
    bucket.delete_objects(Delete={'Objects':list_obj})


delete_all_obj(new_bucket_name)


# delete the empty bucket
s3.Bucket(new_bucket_name).delete()