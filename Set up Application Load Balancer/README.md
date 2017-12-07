# Set up a Appication Load Balancer on AWS



Select a Free Tier Eligible Ubuntu instance from EC2 Dashboard


![image001](https://user-images.githubusercontent.com/32446623/33732620-14e86182-db55-11e7-936b-0c90990e0c5a.jpg)



Attach EC2 to PublicSubnet1 under LabVPC

![image002](https://user-images.githubusercontent.com/32446623/33732621-14f74db4-db55-11e7-899f-582020692006.jpg)



Choose default configurations and existing key pair and launch the instance

![image003](https://user-images.githubusercontent.com/32446623/33732622-1507aa92-db55-11e7-9fe3-7c6996555c13.jpg)

Similarly Select  Another Ubuntu Instance and launch it under PublicSubnet2 under LabVPC 


![image004](https://user-images.githubusercontent.com/32446623/33732623-1524b948-db55-11e7-92fd-66fc75650270.jpg)



Check if both ‘Ubu1’ and ‘Ubu2’ instances are running

![image005](https://user-images.githubusercontent.com/32446623/33732624-15717b48-db55-11e7-95d7-8b3cc21657fc.jpg)

Access ‘Ubu1’ using system linux command line using ssh

![image006](https://user-images.githubusercontent.com/32446623/33732625-157f4fa2-db55-11e7-9587-d9d7b29172de.jpg)



Update the EC2 system files by running command as root user ‘sudo apt-get update’ 

![image007](https://user-images.githubusercontent.com/32446623/33732626-158ea876-db55-11e7-8ce9-9563dfa54ff0.jpg)


After update is finished, install Apache server using command ‘sudo apt-get install apache2’

![image008](https://user-images.githubusercontent.com/32446623/33732628-15fdbaae-db55-11e7-8b17-7e40a9e61d53.jpg)

Similarly access ‘Ubu2’ instance. 

![image009](https://user-images.githubusercontent.com/32446623/33732629-16167d28-db55-11e7-9082-05a18b1bff90.jpg)



After updating system files, install apache server using same command as mentioned earlier.

![image010](https://user-images.githubusercontent.com/32446623/33732630-1625f3a2-db55-11e7-87b0-62a9dcf03eb2.jpg)

Also, make sure that security groups associated with ‘Ubu1’ allows access on HTTP port 80 so that we can 
access it using web browser.

![image011](https://user-images.githubusercontent.com/32446623/33732631-163442d6-db55-11e7-9b6c-415d9011ef97.jpg)



Same security configuration as mentioned above should be available for ‘Ubu2’

![image012](https://user-images.githubusercontent.com/32446623/33732633-164cb866-db55-11e7-813e-caf077b4ca90.jpg)

Try to access ‘Ubu1’ using it’s public ip 13.58.120.234. It must show the default webpage of Apache server.

![image013](https://user-images.githubusercontent.com/32446623/33732634-16614042-db55-11e7-95d1-a2d0a99c8eb3.jpg)



Similarly try to access ‘Ubu2’ using ip 18.221.6.239. It should also show the default page.

![image014](https://user-images.githubusercontent.com/32446623/33732635-166c9d0c-db55-11e7-8ea9-446d5bb2bcfd.jpg)


Go to ELB Dashboard and select Application Load Balancer

![image015](https://user-images.githubusercontent.com/32446623/33732636-1679c504-db55-11e7-87f8-a51cbe6cc92f.jpg)


Create a Load Balancer ‘MyAppELB’ under LabVPC 

![image016](https://user-images.githubusercontent.com/32446623/33732637-1689c7a6-db55-11e7-9fad-e43c44d1e751.jpg)


Add Both Availability Zones and  PublicSubnet1 and PublicSubnet2 attached to our Ubuntu EC2 instances.

![image017](https://user-images.githubusercontent.com/32446623/33732638-169d260c-db55-11e7-900a-cf54c863cf30.jpg)


Assign default security group to the ELB

![image018](https://user-images.githubusercontent.com/32446623/33732639-16c159b4-db55-11e7-965a-eb30dc9f333c.jpg)


Choose Default Routing Settings and move forward

![image019](https://user-images.githubusercontent.com/32446623/33732640-16d03894-db55-11e7-8654-9c3ac5aa376c.jpg)


Register both Ubuntu EC2 instances ‘Ubu1’ and ‘Ubu2’ as Targets to Application Load Balancer

![image020](https://user-images.githubusercontent.com/32446623/33732642-16f0c3ac-db55-11e7-8a05-a00af36d9f0f.jpg)


Review the settings

![image021](https://user-images.githubusercontent.com/32446623/33732643-1704bfd8-db55-11e7-8be0-ca0a9aea12b8.jpg)


Application Load Balancer Created Successfully

![image022](https://user-images.githubusercontent.com/32446623/33732644-1714d4fe-db55-11e7-989e-06cc70cf490e.jpg)


Check if both Ubuntu instances are part of Target Group created earlier

![image023](https://user-images.githubusercontent.com/32446623/33732645-17258c22-db55-11e7-8b7e-76d1cff6db60.jpg)


After Application Load Balancer is successfully provisioned and is active, try to access it using its DNS name in 
Web Browser. Default Apache server page must be displayed.

![image024](https://user-images.githubusercontent.com/32446623/33732647-173e8f60-db55-11e7-9b8b-ba82a9c52f1d.jpg)


Stop one EC2 instance. Here we have stopped ‘Ubu2’ and again try to access ‘MyAppELB’. Again server default 
page must be displayed.

![image025](https://user-images.githubusercontent.com/32446623/33732648-177bacb0-db55-11e7-9711-50a0e1606c65.jpg)


Stop the other instance ‘Ubu1’ and again try to access ‘MyAppELB’. This time default server page must not be 
accessible.

![image026](https://user-images.githubusercontent.com/32446623/33732649-178d02ee-db55-11e7-89bc-294997a78c28.jpg)



