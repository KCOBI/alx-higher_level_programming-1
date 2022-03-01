-- this will create a database and a user wich only have select acess on new Db
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
REVOKE ALL PRIVILEGES ON *.* FROM 'user_0d_2'@'localhost';

GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';