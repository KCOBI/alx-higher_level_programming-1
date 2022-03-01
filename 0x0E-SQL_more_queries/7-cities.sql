-- creates the database hbtn_0d_usa and the table cities
-- (in the database hbtn_0d_usa) on your MySQL server.
CREATE TABLE IF NOT EXISTS cities (
    id INT UNIQUE PRIMARY KEY AUTO_INCREMENT NOT NULL,
    state_id INT NOT NULL,
    CONSTRAINT FK_STATES_ID FOREIGN KEY (state_id) REFERENCES states(id),
    name VARCHAR(256) NOT NULL
);