## Week 2
---
__Relational Database Terminologies__
- Database, contains many tables
- Relational (table), contains tuples and attributes
- tuple (row), represents an instance of data/example
- attributes (column/field), data information type that is stored

__SQL Language__
- create table
- retrieve data from table
- insert data
- delete data
- update data
- there are called ***CRUD*** functions
<!-- http://sqlitebrowser.org/ -->
***In SQL Lite***

**SQL Code**
contract/rules setting does not accept 129
**CREATE TABLE**
```
CREATE TABLE tblname(
  name VARCHAR(128),
  email VARCHAR(128)
  )
```
**INSERT VALUE**
```
INSERT INTO tblname(col1, col2) VALUES (row1, row2)
```
**DELETE VALUE**
```
DELETE FROM tblname WHERE email="stoang" Evaluates to true statement
```
**UPDATE VALUE**
```
UPDATE tblname SET name="some" WHERE email="gnog" Evaluate to true statement
```
**"*" means all**
**RETRIEVING DATA**
```
SELECT * FROM tblname
SLECT * FROM tblname WHERE email=""
```
**SORTING with ORDER BY**
```
SELECT * FROM tblname ORDER BY email
```
```
SELECT * FROM tblname ORDER BY name
```
