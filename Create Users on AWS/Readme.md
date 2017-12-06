
# AWS User/Group/Role Creation

# Create Users - S3TestUser and EC2TestUser

Create S3TestUser. Provide the name of the user with access type as both access key and password


![image](https://user-images.githubusercontent.com/32446623/33644905-e5612eb6-da15-11e7-9eb9-2a48082cccaf.png)


Provide AmazonS3FullAccess to S3TestUser


![image](https://user-images.githubusercontent.com/32446623/33644923-045c6204-da16-11e7-9197-281583a4406b.png)


Successfully created S3TestUser


![image](https://user-images.githubusercontent.com/32446623/33644928-09feb6f8-da16-11e7-9f87-c5a15aa48d56.png)


Create EC2TestUser. Provide the name of the user with access type as both access key and password


![image](https://user-images.githubusercontent.com/32446623/33644930-0f667a4a-da16-11e7-8977-2a83e52d8dcc.png)


![image](https://user-images.githubusercontent.com/32446623/33644933-152a4b28-da16-11e7-843f-91f56e5d0d28.png)

# Create a Group EC2TestGroup

Create the Group

![image](https://user-images.githubusercontent.com/32446623/33644959-3b04a17c-da16-11e7-8a40-279a333d2ca8.png)

Assign Permissions

![image](https://user-images.githubusercontent.com/32446623/33644964-3f97494c-da16-11e7-9150-acfd7fe2ef9a.png)


![image](https://user-images.githubusercontent.com/32446623/33644967-43f8f972-da16-11e7-99b4-249bbc0e1064.png)

# Add user to the Group

Add User EC2TestUser to the group

![image](https://user-images.githubusercontent.com/32446623/33645115-2fde470c-da17-11e7-9022-115d5d9c6498.png)

# Create a Role EC2Describe

Choose a EC2 role



![image](https://user-images.githubusercontent.com/32446623/33645126-402f132a-da17-11e7-867f-1607c7b603fd.png)

Assign Permission to the Role



![image](https://user-images.githubusercontent.com/32446623/33645138-46d2918e-da17-11e7-9ef1-9bec9b92afda.png)

Assign name to the Role



![image](https://user-images.githubusercontent.com/32446623/33645146-4deb367e-da17-11e7-845c-105ce630ebe3.png)


![image](https://user-images.githubusercontent.com/32446623/33645153-51cf0144-da17-11e7-9fe5-a4dfa09f7cf4.png)


# User Login

Login using S3TestUser Credentials


![image](https://user-images.githubusercontent.com/32446623/33645155-57043814-da17-11e7-9c37-e840496633c5.png)


# User IAM Access Denied

S3TestUser IAM permission fail check


![image](https://user-images.githubusercontent.com/32446623/33645161-5fb9f5c0-da17-11e7-91f4-cb2f406816e4.png)


# User EC2 Service Manipulation Check

S3TestUser EC2 Service Manipulation Check


![image](https://user-images.githubusercontent.com/32446623/33645166-657156a2-da17-11e7-9414-5d347294b7be.png)


# User Bucket Creation

S3TestUser Bucket Created and file uploaded

![image](https://user-images.githubusercontent.com/32446623/33645172-6a1380ae-da17-11e7-90cd-c348b3dd9829.png)


# User Bucket Access Denied

EC2TestUser Bucket Access Denied


![image](https://user-images.githubusercontent.com/32446623/33645176-6f02d358-da17-11e7-8161-4f33dbdda30a.png)




1
