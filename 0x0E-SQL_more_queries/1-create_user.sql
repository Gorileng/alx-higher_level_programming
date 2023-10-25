-- Create a MySQL server user user_0d_1.
-- user_0d_1 must have all the privileges on your MySQL server
-- user_0d_1 the password must be set to the user_0d_1_pwd
-- When a user user_0d_1 already exists your script must not fail

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

