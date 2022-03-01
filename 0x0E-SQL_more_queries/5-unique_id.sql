-- this table have an id that is not null and also uniq for all 

CREATE TABLE IF NOT EXISTS unique_id (id INT NOT NULL DEFAULT(1) UNIQUE, name VARCHAR(256));