-- create a database hbtn_0d_2 and a user user_0d_2.
-- user_0d_2 must have the only SELECT privilege in a database hbtn_0d_2
-- user_0d_2 the password must be set to the user_0d_2_pwd
-- When a database hbtn_0d_2 already exists your script must not fail
-- When a user user_0d_2 already exists your script must not fail

CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON `hbtn_0d_2`.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
