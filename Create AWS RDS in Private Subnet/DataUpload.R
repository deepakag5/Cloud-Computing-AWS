
# Load the required libraries - Download the packages DBI and RMySQL if not already downloaded
library(DBI)
library(RMySQL)


# Make the AWS connection

conn_aws = dbConnect(MySQL(),
                     user='RDS Username', password='Your RDS Password',
                     host='RDS endpoint',
                     dbname="RDS Databasename",  port=3306);


df <- read.csv("name.csv")



head(df)


################ Change DB Name and Table name as per your RDS in below loops

# Check for 1 record

for(i in 1)
{
  query <- paste("INSERT INTO RDSDBNAME.TABLENAME(Frequency,Gender,Name,Year) 
VALUES (",paste(df[i,c(3)], collapse = ", "), ",", paste0("\"",df[i,c(2)],"\""), ",", paste0("\"",df[i,c(1)],"\""), ",", paste0("\"",df[i,c(4)],"\""), ") 
               ON DUPLICATE KEY UPDATE 
               Name = VALUES(name),
               Frequency=VALUES(Frequency),
               Gender = VALUES(Gender),
               Year =VALUES(Year)")
  
  cat(query)
  
  dbGetQuery(conn_aws, query)
}

# Populate all other records

for(i in 2:nrow(df))
{
  query <- paste("INSERT INTO RDSDBNAME.TABLENAME(Frequency,Gender,Name,Year) 
VALUES (",paste(df[i,c(3)], collapse = ", "), ",", paste0("\"",df[i,c(2)],"\""), ",", paste0("\"",df[i,c(1)],"\""), ",", paste0("\"",df[i,c(4)],"\""), ") 
               ON DUPLICATE KEY UPDATE 
               Name = VALUES(name),
               Frequency=VALUES(Frequency),
               Gender = VALUES(Gender),
               Year =VALUES(Year)")
  
  #cat(query)
  
  dbGetQuery(conn_aws, query)
}
