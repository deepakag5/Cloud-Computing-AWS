# Create a AWS RDS in Private Subnet and access data in it using EC2 in Public Subnet of VPC



# Check VPC configuration


Check if LabVPC DNS Hostname is enabled


![image001](https://user-images.githubusercontent.com/32446623/33729274-171ac4c2-db4b-11e7-9393-a4b4b9c32498.jpg)


Check if LabVPC DNS Resolution is enabled


![image002](https://user-images.githubusercontent.com/32446623/33729275-172f87ae-db4b-11e7-8f34-7311d94f1dec.jpg)


# Create EC2 in Public Subnet


Create a EC2 instance in PublicSubnet1 under LabVPC with security group named as webserversg which allows access from http port 80


![image003](https://user-images.githubusercontent.com/32446623/33729276-17466136-db4b-11e7-9613-39d9a6ef5882.gif)


Details of the above mentioned VPC ID and PublicSubnet1


![image004](https://user-images.githubusercontent.com/32446623/33729277-1752b15c-db4b-11e7-815b-aeebb4fad585.gif)


# Create RDS in Private Subnet


Make a Security Group for DB instance inside LabVPC allowing access from local machine (just to check the connection)


![image005](https://user-images.githubusercontent.com/32446623/33729278-1772c4d8-db4b-11e7-9466-7eef58ddf7d0.jpg)


Add security group of EC2 instance to RDS security group MyDBSecurityGroup inbound rules


![image006](https://user-images.githubusercontent.com/32446623/33729279-1784f748-db4b-11e7-9232-1d323c31ed7f.gif)


Launched an RDS instance with NO public access with MyDBSecurityGroup


![image007](https://user-images.githubusercontent.com/32446623/33729280-179f7104-db4b-11e7-81aa-70d65187e108.gif)


Try to connect PrivateRDS using local machine. It must NOT be accessible. Then try to connect using EC2 created in publicsubnet by 
logging into it. You should be able to access it.



![image008](https://user-images.githubusercontent.com/32446623/33729281-17ac4924-db4b-11e7-82c6-e726b72be843.jpg)


Create the table ssanames inside RDS database G36182176_ssanames


![image009](https://user-images.githubusercontent.com/32446623/33729282-17bb554a-db4b-11e7-909e-4ae07caa7371.jpg)

Download the data 
from the URL on EC2 
instance



![image010](https://user-images.githubusercontent.com/32446623/33729283-17cad1aa-db4b-11e7-95d8-e6af051dd632.jpg)


Create a shell script DataUpload.sh on EC2 to upload the data. Make sure that it is executable.


![image011](https://user-images.githubusercontent.com/32446623/33729284-17ddbbda-db4b-11e7-9506-8a5051699685.jpg)


Upload the data by running above script and check the data in mysql table.


![image012](https://user-images.githubusercontent.com/32446623/33729285-17f18cc8-db4b-11e7-897c-997137df3ffb.jpg)


We can install R and Rstudio Server on EC2 instance and use the same Rscript file with PrivateRDS connection string and execute it to  
generated the required graph. 


![image013](https://user-images.githubusercontent.com/32446623/33729286-17ffd404-db4b-11e7-9d35-4640ff9c9360.gif)
