DROP DATABASE IF EXISTS nba_db;
CREATE DATABASE nba_db;
CREATE USER nba_user WITH PASSWORD 'nba_pass';
ALTER ROLE nba_user SET client_encoding TO 'utf8';
ALTER ROLE nba_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE nba_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE nba_db TO nba_user;