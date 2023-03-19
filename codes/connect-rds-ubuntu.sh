# run the below commands after creating RDS and connecting it to ec2

sudo apt install mysql-client-core-8.0  

mysql -u 'ananay' -p'Password' \
    -h 'database-1.co11wpxyqx7k.ap-south-2.rds.amazonaws.com' -P '3306' \
    -D ananay
    
   # you logged in to mysql now...
   
   # checdk databases 
   
   show databases;
   
   #load sample data
   wget https://www.mysqltutorial.org/wp-content/uploads/2018/03/mysqlsampledatabase.zip
   
   # install and unzip data
   sudo apt-get install unzip -y
   
   # unzip 
   unzip mysqlsampledatabase.zip
   
   # again connect to mysql
   # mysql knows the file where you started it
   # if you forget ; -> gives error file can't be found error 2
   
   mysql -u 'ananay' -p'Password' \
    -h 'database-1.co11wpxyqx7k.ap-south-2.rds.amazonaws.com' -P '3306' \
    -D ananay
    
    # load data 
    source mysqlsampledatabase.sql ;
    
    use database <name> ;
    
    select * from <table> ;
