## Week 3
- Drawing a picture showing relationships between data
- Do not put the same string data twice, use relationship
- never alter the real world data
- need to categorize the data into subcategories
- **Primary Key** points to **Foreign Key**
- **Logical Key** uses **WHERE** and **ORDER BY** clause
**Create Table**
```
CREATE TABLE tblname(
    id      INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name    TEXT
)
```
```
INSERT into tblname(varname) VALUES ('something')
```
```
select tbl1.title, tbl1.name from tbl1 join tbl2 on tbl1.artist_id = tbl1.id
```
