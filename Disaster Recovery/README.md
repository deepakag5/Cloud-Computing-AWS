# Copy a AMI of EC2 in another region


Create a new Ubuntu EC2 in US East Region


![1](https://user-images.githubusercontent.com/32446623/33735527-925b43f2-db5d-11e7-9b0c-59e3df42ddbf.png)



Choose appropriate configuration


![2](https://user-images.githubusercontent.com/32446623/33735528-926e788c-db5d-11e7-9755-6ac8db6e775f.png)


Make sure SSH port (22) and HTTP port (80) are open


![3](https://user-images.githubusercontent.com/32446623/33735529-9288efaa-db5d-11e7-9bea-40d0076525db.png)


Launch the instance and login using SSH. Update and install apache2


![4](https://user-images.githubusercontent.com/32446623/33735530-92973aba-db5d-11e7-9311-da42675613c6.png)



Try to access public ipv4 of the instance using browser. Default apache web page must be displayed.



![5](https://user-images.githubusercontent.com/32446623/33735531-92a3d6da-db5d-11e7-9d44-d77850874f05.png)



Create a snapshot of the volume of our newly created Ubuntu instance i.e. “UbuEast”



![6](https://user-images.githubusercontent.com/32446623/33735532-92b367b2-db5d-11e7-8df1-4a9a31174789.png)



Create image of the snapshot Name this AMI as “UbuEast SnapShot”. Make sure you select correct Virtualization Type.


![7](https://user-images.githubusercontent.com/32446623/33735533-92d4d6a4-db5d-11e7-9dba-b4048c2b5f2d.png)


Copy the above AMI to US West Region.


![8](https://user-images.githubusercontent.com/32446623/33735534-92e22584-db5d-11e7-8928-ddbfe046f65c.png)


Go to US West EC2 Dashboard and launch an EC2 instance using the copied AMI.


![9](https://user-images.githubusercontent.com/32446623/33735535-92f24734-db5d-11e7-9bbe-a441d9789279.png)


After selecting default configuration  provide access to SSH and HTTP ports.



![10](https://user-images.githubusercontent.com/32446623/33735537-93030402-db5d-11e7-9182-164559e20832.png)



Launch the instance and it should be running successfully.



![11](https://user-images.githubusercontent.com/32446623/33735538-931112e0-db5d-11e7-9002-f3429a0ae764.png)



Perform a SSH to the US West Ubuntu Instance. Also, check if Apache Server is running.



![12](https://user-images.githubusercontent.com/32446623/33735539-93262996-db5d-11e7-9d2a-31c08e2f67b1.png)



Try to access public ipv4 of the instance using browser. Default apache web page must be displayed.



![13](https://user-images.githubusercontent.com/32446623/33735540-9334e346-db5d-11e7-8a49-da798e1c05b0.png)




