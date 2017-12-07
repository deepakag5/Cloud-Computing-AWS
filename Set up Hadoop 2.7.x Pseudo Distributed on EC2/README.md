# Set up Hadoop 2.7.x on Amazon EC2 in Pseudo Distributed Mode



Choose appropriate Ubuntu EC2 AMI



![image001](https://user-images.githubusercontent.com/32446623/33734718-4cf0bbc8-db5b-11e7-9a1b-7b92da5ea0d4.jpg)



Select configuration – LabVPC, PublicSubnet1 and Auto-Assign IP as enabled



![image002](https://user-images.githubusercontent.com/32446623/33734720-4d245d52-db5b-11e7-9eec-91e6fcf082c9.jpg)



Add Security Group with all ports opened and accessible from anywhere and launch the EC2



![image003](https://user-images.githubusercontent.com/32446623/33734721-4d3256be-db5b-11e7-97e4-3bbe63103659.jpg)



Check if EC2 (‘HadoopEC2’) is running


![image004](https://user-images.githubusercontent.com/32446623/33734723-4d8039c4-db5b-11e7-8568-e40b4d81c4bc.jpg)



Login to the EC2 using ssh 



![image005](https://user-images.githubusercontent.com/32446623/33734724-4da0204a-db5b-11e7-986d-7ae13416c4ce.jpg)




Create a bash script to update system, install pdsh(to run commands in parallel on multiple hosts) and install Java 
Development Kit. Make the script executable and run it using command ./script.sh



![image006](https://user-images.githubusercontent.com/32446623/33734725-4db3d93c-db5b-11e7-8a17-6486416a71c6.jpg)




Check if java is installed successfully. Export the path of Jvm to bashrc and source it to save the changes. Also download 
the Apache hadoop tar file and then unzip it using command tar -xvf hadoop-2.7.4.tar.gz



![image007](https://user-images.githubusercontent.com/32446623/33734726-4dc91aae-db5b-11e7-8979-8786075be6d5.jpg)




Check the system ip address using command ifconfig. Note it down



![image008](https://user-images.githubusercontent.com/32446623/33734727-4dd904c8-db5b-11e7-810f-2c7b938c6b8e.jpg)




Update /etc/hosts file with IP address noted above and DNS IPv4 name instead of default ip and localhost



![image009](https://user-images.githubusercontent.com/32446623/33734728-4deb39a4-db5b-11e7-9508-770a56fe7b0b.jpg)



Type hostname to confirm if the hostname has been successfully updated. Also generate the rsa public-private key pair. 
Export public rsa key to authorized keys. Also ssh the localhost.



![image010](https://user-images.githubusercontent.com/32446623/33734729-4e007742-db5b-11e7-8c2f-0fee373836ca.jpg)




Update JAVA_HOME in hadoop-env.sh and save it



![image011](https://user-images.githubusercontent.com/32446623/33734730-4e1c02dc-db5b-11e7-8c77-6fb55c992c47.jpg)






Checked hadoop configuration. It recognizes the command and is working fine



![image012](https://user-images.githubusercontent.com/32446623/33734731-4e335a9a-db5b-11e7-9f18-4e1d7534bb18.jpg)




Update core-site.xml with property name fs.defaultFS to allow dfs commands without providing full site name in the 
command  .



![image013](https://user-images.githubusercontent.com/32446623/33734732-4e635c54-db5b-11e7-9340-6d52e2f420a4.jpg)



Update hdfs-site.xml with replication factor 1



![image014](https://user-images.githubusercontent.com/32446623/33734733-4e798524-db5b-11e7-85fc-414a131122fc.jpg)





Format the filesystem using command bin/hdfs namenode -format. (This will format the meta-data related to data-nodes. 
By doing that, all the information on the datanodes are lost and they can be reused for new data.)


![image015](https://user-images.githubusercontent.com/32446623/33734735-4e90bf0a-db5b-11e7-9b65-ff2ba3dcf6d4.jpg)



Start hadoop services by using start-dsf.sh command. Also use ‘jps’ command to check whether hadoop services are 
running.


![image016](https://user-images.githubusercontent.com/32446623/33734736-4ea23e2e-db5b-11e7-80df-5caa8855790e.jpg)



Use case – Run hadoop command on xml files. For this create directories user,ubuntu and input. Copy all the xml files 
from etc/hadoop to input directory.



![image017](https://user-images.githubusercontent.com/32446623/33734737-4eb50efa-db5b-11e7-9931-3145a228200c.jpg)





Run a hadoop job using appropriate command



![image018](https://user-images.githubusercontent.com/32446623/33734738-4ede2a2e-db5b-11e7-94cf-e9f11e011233.jpg)



Check if job is completed successfully.



![image019](https://user-images.githubusercontent.com/32446623/33734739-4ef2dbcc-db5b-11e7-9a61-76da194ae418.jpg)



Check the results in output directory and print it to the console



![image020](https://user-images.githubusercontent.com/32446623/33734740-4f118fae-db5b-11e7-9f17-7ad3cc6dc1b9.jpg)



Check the Hadoop UI using DNS IPv4 followed by port 50070.



![image021](https://user-images.githubusercontent.com/32446623/33734741-4f1ed772-db5b-11e7-8a8e-c3d015939306.jpg)



Browse the filesystem under utilities and navigate to output folder to download mapreduce output file.



![image022](https://user-images.githubusercontent.com/32446623/33734742-4f359af2-db5b-11e7-88ad-ae8caaf1eaa8.jpg)



Open the downloaded file and check the results.



![image023](https://user-images.githubusercontent.com/32446623/33734743-4f476d7c-db5b-11e7-9d07-18be5629c317.jpg)



Wordcount Sample Program on mobydick text file. Download the mobydick text file ‘moby10b.txt’ from the web in EC2 
home folder.



![image024](https://user-images.githubusercontent.com/32446623/33734744-4f54ea9c-db5b-11e7-8da8-eb17b4bacc33.jpg)




Copy the file into the input folder of hdfs



![image025](https://user-images.githubusercontent.com/32446623/33734745-4f608b4a-db5b-11e7-8711-f0c099ab1053.jpg)




Run the mapreduce program on ‘moby10b.txt’ file using appropriate command.



![image026](https://user-images.githubusercontent.com/32446623/33734746-4f744518-db5b-11e7-82b9-2245389d71f5.jpg)



Once the job is completed. Check if the output directory got created and the result file got generated in it. 



![image027](https://user-images.githubusercontent.com/32446623/33734747-4f903552-db5b-11e7-96df-542712c4e009.jpg)



Download the file by navigating into output folder through the UI and open it to check the results.



![image028](https://user-images.githubusercontent.com/32446623/33734748-4fa8aef2-db5b-11e7-842b-7269b6968988.jpg)






