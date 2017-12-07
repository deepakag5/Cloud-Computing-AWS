# Set up Elastic Map Reduce Cluster on Amazon Web Services



Create a bucket in Amazon S3 to store program, data and output. Provide appropriate  name and region.


![1](https://user-images.githubusercontent.com/32446623/33733628-4c9f4f20-db58-11e7-990a-2606d4fe5006.png)


Use default properties of bucket



![2](https://user-images.githubusercontent.com/32446623/33733629-4cc50d82-db58-11e7-8c36-1e9273db9cdd.png)



Upload mapper, reducer and text files



![3](https://user-images.githubusercontent.com/32446623/33733630-4cd33704-db58-11e7-8f9f-57324116b6ab.png)



Choose EMR default software configuration



![4](https://user-images.githubusercontent.com/32446623/33733631-4d279d12-db58-11e7-9d1c-7ed660b65034.png)



Choose 1 Master and 2 Core Nodes



![5](https://user-images.githubusercontent.com/32446623/33733632-4d3cd628-db58-11e7-9bc7-b646db8e386d.png)



Provide appropriate EMR name and select bucket folder for logs. Also, uncheck Debugging option. Provide Tags as well.



![6](https://user-images.githubusercontent.com/32446623/33733633-4d530cf4-db58-11e7-8be7-db5f3c6248ba.png)



Choose default security options and create cluster.



![7](https://user-images.githubusercontent.com/32446623/33733634-4d67916a-db58-11e7-9e3b-6e3c0080253d.png)



Check if the cluster is up and running.



![8](https://user-images.githubusercontent.com/32446623/33733635-4d7921d2-db58-11e7-9017-ddf22c075b03.png)



Go to ‘Add Step’ and select step type as  Customer Jar  and name as Streaming Program. As we are providing hadoop 
streaming command by ourselves we need to specify Jar location as command-runner.jar 



![9](https://user-images.githubusercontent.com/32446623/33733636-4d8d44e6-db58-11e7-8475-ebdc1d11ffde.png)



Check if the step Status is ‘Completed’.



![10](https://user-images.githubusercontent.com/32446623/33733637-4da577a0-db58-11e7-8512-51846b282f07.png)



Go to the bucket to check if output directory has been created and must have success file in it. We have successfully 
run a wordcount program using python on AWS Hadoop EMR.



![11](https://user-images.githubusercontent.com/32446623/33733638-4db816da-db58-11e7-94ff-29fa9a1e9da1.png)



Let’s not forget to terminate the cluster ! (To avoid incurring unnecessary charges $$$)



![12](https://user-images.githubusercontent.com/32446623/33733639-4dcefbfc-db58-11e7-912a-2131a2f98544.png)






