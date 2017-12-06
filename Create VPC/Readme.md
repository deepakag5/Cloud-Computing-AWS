
# Create VPC on AWS

Opened the VPC Dashboard

![1_vpc_dash](https://user-images.githubusercontent.com/32446623/33646154-5fbb82e6-da1c-11e7-897b-754d27f7520c.JPG)

Create VPC Connection with Name as LabVPC and appropriate CIDR block 

![2_create_vpc](https://user-images.githubusercontent.com/32446623/33646165-689e1400-da1c-11e7-9807-bfafe817bb97.JPG)

LabVPC successfully created

![3_vpc_info](https://user-images.githubusercontent.com/32446623/33646166-68a72306-da1c-11e7-97e7-6e4a38697509.JPG)

Create Internet Gateway and name it as LabVPCGateway

![4_create_gateway](https://user-images.githubusercontent.com/32446623/33646167-68afb854-da1c-11e7-8911-ee0698f20ed7.JPG)

Attach above created Gateway to our LabVPC

![5_attach_gate_vpc](https://user-images.githubusercontent.com/32446623/33646159-682de036-da1c-11e7-8d44-fa3394072752.JPG)

LabGateway attached to LabVPC

![6_attached_gate_vpc](https://user-images.githubusercontent.com/32446623/33646160-6837812c-da1c-11e7-8797-95a08348499f.JPG)

Create PublicSubnet1 under LabVPC by selecting AZ and giving appropriate CIDR Block (10.200.6.0/24)	 

![7_create_public_subnet](https://user-images.githubusercontent.com/32446623/33646161-68402aac-da1c-11e7-9d2b-1872011187e3.JPG)
PublicSubnet1 created successfully under LabVPC	 
![8_created_public_subnet](https://user-images.githubusercontent.com/32446623/33646162-6848e6b0-da1c-11e7-867f-a8ab8a852a08.JPG)
Create PrivateSubnet1 under LabVPC by selecting same AZ and giving appropriate CIDR Block (10.200.50.0/24)	 

![9_create_private_subnet](https://user-images.githubusercontent.com/32446623/33646163-688cd1b8-da1c-11e7-9459-c5e3cdeac870.JPG)

PrivateSubnet1 created successfully under LabVPC	 
![10_created_private_subnet](https://user-images.githubusercontent.com/32446623/33646164-6895428a-da1c-11e7-8c73-59af73ead753.JPG)
Create Route Table under LabVPC	 
![11_create_public_route](https://user-images.githubusercontent.com/32446623/33646198-81aa3208-da1c-11e7-8022-8f0bc15e7b35.JPG)
PublicRoute Created Successfully	 
![12_created_public_route](https://user-images.githubusercontent.com/32446623/33646199-81b57a6e-da1c-11e7-9721-16bf1d663294.JPG)
Attach LabVPCGateway to the PublicRoute Route Table with destination as 0.0.0.0/0 	 
![13_add_vpc_public_route](https://user-images.githubusercontent.com/32446623/33646200-81bfa502-da1c-11e7-8c38-88acf32c984a.jpg)
LabVPCGateway Attached Sucessfully to PublicRoute 	 
![14_added_vpc_public_route](https://user-images.githubusercontent.com/32446623/33646201-81c8581e-da1c-11e7-9ad2-de78a8a2e64d.JPG)
Attach PublicSubnet1 to this PublicRoute Table under Subnet Associations Tab	 

![15_add_public_subnet_public_route](https://user-images.githubusercontent.com/32446623/33646202-81d1d380-da1c-11e7-83fb-727f4dc68942.JPG)
PublicSubnet1 attached successfully to PublicRoute	 


![16_added_public_subnet_public_route](https://user-images.githubusercontent.com/32446623/33646203-81db16fc-da1c-11e7-940f-4a6ec50647d7.JPG)

Create another Route Table under LabVPC, name it as PrivateRoute	 

![17_create_private_route](https://user-images.githubusercontent.com/32446623/33646204-81e416c6-da1c-11e7-9673-ea442c17e563.JPG)

Attach PrivateSubnet1 to this PrivateRoute Table under Subnet Associations Tab	 


![18_added_private_subnet_private_route](https://user-images.githubusercontent.com/32446623/33646205-81ecd8c4-da1c-11e7-89ea-00d20056f1f5.JPG)

Select a ‘General Purpose’ free tier eligible t2.micro EC2 Instance, click on ‘Configure Instance Details’

![19_create_ec2](https://user-images.githubusercontent.com/32446623/33646206-81f75efc-da1c-11e7-98f7-2562b75d532a.JPG)

Choose Network as LabVPC, subnet as PublicSubnet1 and Enable Auto-assign IP, scroll below and Expand the ‘Advanced Details’ Tab

![20_create_ec2_config](https://user-images.githubusercontent.com/32446623/33646207-8251fa1a-da1c-11e7-8db8-9aa6bf86aab1.JPG)

Copy the shell script as text under the advanced details tab, then click on Add Storage

![21_create_ec2_script](https://user-images.githubusercontent.com/32446623/33646208-825a7492-da1c-11e7-85e7-e8fdb9e7e50c.JPG)

Accept the default values and click on ‘Add Tags’

![22_create_ec2_storage](https://user-images.githubusercontent.com/32446623/33646209-8262ad9c-da1c-11e7-84f8-f752b0bafa27.JPG)

Provide Key as ‘Name’ and Value as ‘NAT’ and click on ‘Configure Security Group’

![23_create_ec2_add_tag](https://user-images.githubusercontent.com/32446623/33646211-8275ace4-da1c-11e7-9666-e365581becc0.JPG)


Create a new Security Group Named as ‘NATSB’ and provide appropriate description. Add Rule as ‘All Traffic’ and Source as ‘Anywhere’
![23_create_ec2_add_security_group](https://user-images.githubusercontent.com/32446623/33646210-826b4cc2-da1c-11e7-99e3-664b4fc95e8d.JPG)

Reviewed and Launched the NAT instance. Download the ‘key-pair’ pem file by providing name as ‘publickey.pem’
![24_public_key_created](https://user-images.githubusercontent.com/32446623/33646212-829d6b76-da1c-11e7-9845-928257a0ccfc.JPG)

Provides the name of the key attached with NAT Instance
![25_ec2_launched](https://user-images.githubusercontent.com/32446623/33646213-82a709c4-da1c-11e7-80ff-9cec57180b1a.JPG)

NAT Instance Running
![26_ec2_networking](https://user-images.githubusercontent.com/32446623/33646214-82b2dec0-da1c-11e7-869a-3907c6ee7696.jpg)

Here Click on ‘Yes, Disable’ to Disable Source/Destination Check

![27_ec2_networking_diable_source](https://user-images.githubusercontent.com/32446623/33646215-82bb94de-da1c-11e7-8a43-be0e9034053a.JPG)

In Route Table, select PrivateRoute and then Edit the ‘Routes’

![28_private_route_table](https://user-images.githubusercontent.com/32446623/33646216-82c52710-da1c-11e7-9997-6bf4d26a1182.JPG)
Add another route as NAT with Destination as 0.0.0.0/0 so that NAT has access to PrivateRoute	 

![29_add_private_route_nat](https://user-images.githubusercontent.com/32446623/33646217-82cd190c-da1c-11e7-8b43-cd5af3375d5b.jpg)
NAT Route added to PrivateRoute

![30_added_private_route_nat](https://user-images.githubusercontent.com/32446623/33646218-82d5d2ea-da1c-11e7-9ed4-587caa4db7c7.JPG)

Select a ‘General Purpose’ free tier eligible t2.micro EC2 Instance, click on ‘Configure Instance Details’	
Choose Network as LabVPC, subnet as PrivateSubnet1 and Disable Auto-assign IP, Scroll below and click on Add Storage and accept the default values and then click on ‘Add Tags’	 

![31_create_ec2_config](https://user-images.githubusercontent.com/32446623/33646219-82de7120-da1c-11e7-9956-7cc5e4a8ad84.JPG)

Under this add key as ‘Value’ and Value as ‘PrivateEC2’, click on ‘Configure Security Group’

![32_create_ec2_add_tag](https://user-images.githubusercontent.com/32446623/33646220-82e7a416-da1c-11e7-874f-324d1f386910.JPG)

Create a new security group named as ‘PrivateEC2’ and provide appropriate description. Under SSH Rule which is already there select source as ‘Custom’ and attach ‘NATSB’ security group to it created earlier

![33_create_ec2_add_security_group](https://user-images.githubusercontent.com/32446623/33646221-82f2184c-da1c-11e7-8c0b-d6afc0de5400.JPG)
Review and Launch the ‘PrivateEC2Instance’. Attach the ‘publickey.pem’ created earlier by choosing ‘choose an existing key-pair’ option. As we can see both instances are running on AWS	 


![34_both_ec2_running](https://user-images.githubusercontent.com/32446623/33646222-82fcad66-da1c-11e7-94ec-aebba84a466f.jpg)

Installed Putty, Puttygen and Pageant. Successfully generated ‘publickey.ppk’ file using Puttygen. Saved the file as private key.	 
![key](https://user-images.githubusercontent.com/32446623/33646226-8323574a-da1c-11e7-88b0-0211b5416c22.JPG)

![puttygen](https://user-images.githubusercontent.com/32446623/33646228-83640d3a-da1c-11e7-8b3b-3f72d95e14d9.JPG)

Added the generated .ppk key to Pageant Key List	 
![pageant](https://user-images.githubusercontent.com/32446623/33646227-835af7e0-da1c-11e7-83f2-b13b70effce6.JPG)


After doing proper configurations for NAT Instance in Putty, successfully logged in as ec2-user	 
![35_login_nat_using_putty](https://user-images.githubusercontent.com/32446623/33646223-8306021c-da1c-11e7-9d40-2eb33a47ee89.jpg)


Succesfully pinged ietf.org	 
![36_nat_ec2_ping](https://user-images.githubusercontent.com/32446623/33646224-83115aea-da1c-11e7-83f0-c80f2d424c84.jpg)

Performed SSH from NAT to Private EC2Intance using its private IP (10.200.50.122)
![37_connect_nat_to_private_instance](https://user-images.githubusercontent.com/32446623/33646225-831a71ca-da1c-11e7-81b3-382e110c00f0.JPG)


![t2_1_create_publicsubnet2](https://user-images.githubusercontent.com/32446623/33646229-836df700-da1c-11e7-927a-810747fe6385.jpg)

Attach PublicSubnet2 to existing PublicRoute Table
![t2_2_create_privatesubnet2](https://user-images.githubusercontent.com/32446623/33646230-839b7d88-da1c-11e7-90a0-bb6a0b3ea76e.jpg)
Create PrivateSubnet2 under same AZ as PublicSubnet2. Attach PrivateSubnet2 to LabVPC and enter appropriate CIDR blocks (10.200.55.0/24)
![t2_3_publicsubnet2_added](https://user-images.githubusercontent.com/32446623/33646231-83a4ff3e-da1c-11e7-820d-ef68d0589ebf.jpg)
Attach PrivateSubnet2 to existing PrivateRoute Table
![t2_4_privatesubnet_added](https://user-images.githubusercontent.com/32446623/33646232-83ae3b94-da1c-11e7-99e8-12f6a2cfe8c7.jpg)



