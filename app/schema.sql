set names utf8;
DROP DATABASE IF EXISTS shuzhifenxiang;
CREATE DATABASE IF NOT EXISTS shuzhifenxiang CHARACTER SET 'utf8' COLLATE 'utf8_bin';

SET character_set_server = utf8;
USE shuzhifenxiang;

CREATE TABLE IF NOT EXISTS comment(
  id INTEGER AUTOINCREMENT PREPARE KEY,
  text VARCHAR(256) NOT NULL
)

CREATE TABLE IF NOT EXISTS visit(
  visit_day CHAR(10) PRIMARY KEY ,
  visit_count INTEGER NOT NULL ,
)
