-- creates the database hbtn_0d_usa and the table states.

CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
name VARCHAR(256) NOT NULL);
