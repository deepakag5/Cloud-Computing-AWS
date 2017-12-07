# Remove the existing objects from the environment
rm(list=ls());

# Clear the command line console
cat("\014")

# Load the required libraries
library(DBI)
library(RMySQL)
library(lubridate)
library(ggplot2)

# Make the AWS connection

conn_aws = dbConnect(MySQL(),
                     user='G3', password='12345678',
                     host='g36182176.cv0flyvrlwcj.us-east-2.rds.amazonaws.com',
                     dbname="G3",  port=3306);



# Fetch the year and gender wise total frequency 

data <- dbGetQuery(conn_aws,"SELECT `year`,gender,sum(frequency) FROM G3.ssanames group by gender,`year` order by `year`")


# Change the column names

colnames(data) <- c("year","sex","frequency")

# Change the datatype of year to numeric for plotting scales on x-axis

data$year <- as.numeric(data$year)

# Plot the graph and scale the x-axis

ggplot(data = data, aes(x = year, y = frequency, color = sex)) +       
  geom_line(aes(group = sex)) +scale_x_continuous(breaks = data$year[c(TRUE, rep(FALSE, 39))])

ggplotly()


# Disconnect the connections 

all_cons <- dbListConnections(MySQL())
all_cons

for(con in all_cons)
  dbDisconnect(con)
