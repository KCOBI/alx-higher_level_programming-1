-- this will create database and also states which its id and name not null and also incriment
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (id INT NOT NULL AUTO_INCREMENT  PRIMARY KEY  UNIQUE , state_id INT NOT NULL , FOREIGN KEY(state_id) 
                                   REFERENCES state(id) ,name VARCHAR(256) NOT NULL );
