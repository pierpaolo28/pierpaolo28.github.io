---
layout: post
date: 2020-10-10
---

# PostgreSQL Commands
PostgreSQL is a robust, open-source, high-performance database system.
- Postgres = database engine.
- SQL = structured query language which enable us to interact with relational databases.

In databases, data is stored in tables. Each table is then formed by columns and rows. Different tables in a database
can then connected to each other by taking advantage of some form of relationship (e.g. identifier column in common between
the different tables).

It can be possible for us to connect to a database either trough: Command Line, GUI Client or an Application. Two example of GUI clients are: PgAdmin (Windows) and Postico (Linux). By default Postgres comes with a database called **postgres** (with username called postgres) and port equal to 5432. When installing postgres, we will also be prompted to assign a password for this default database.

One common approach used in order to identify uniquely each row in a table, is by the use of a primary key (e.g. ID column using BIGSERIAL). In order to work with multiple different tables, foreign keys are used. A foreign key is a column that references a primary key in another table.

## Joins

- Inner Joins are used in order to take the parts in common between different tables.
- Left Joins includes all the rows from the first table as well as the records from the other tables that have or not a corresponding relationship.

## Commands

- Access PostgreSQL default database through terminal:
```
psql -U postgres
```

- Quit PostgreSQL database:
```
\q
```

- Get commands help:
```
# psql help
psql --help
# database help
help
```

- List databases available:
```
\l
```

- Creating a database:
```
CREATE DATABASE <NAME>;
```

- Entering a created database from CMD:
```
psql -h <IP-Address> -p <Port> -U <username> <database_name>
# example
psql -h localhost -p 5432 -U postgres database_name;
# Alternatively, if already in a database, can switch to another using:
\c <database_name>
```

- Deleting a database:
```
DROP DATABASE <NAME>;
```

- Creating a table with Postgres:
```
CREATE TABLE <NAME> (<COLUMN NAME> <DATA TYPE> <POSSIBLE CONSTRAINTS>,)
# example
CREATE TABLE ex (
  id BIGSERIAL NOT NULL PRIMARY KEY,
  name VARCHAR(30) NOT NULL,
  date TIMESTAMP NOT NULL,
  foreign_id BIGINT REFERENCES <SECOND-TABLE-NAME> (<REFERENCED-COLUMN>)
  )
```

- Visualizing all tables in a Database:
```
\d
# To visualize a specific table use:
\d <table_name>
```

- Insert a row into a table:
```
INSERT INTO <TABLE-NAME> (
  <LIST-OF-COLUMNS-NAMES>
  )
VALUES (<LIST-OF-ROW-VALUES>);
# example
INSERT INTO <TABLE-NAME> (
  name,
  date
  )
VALUES ('Francesco', DATE '1995-03-12');
# To update an already present record, add at the end of the query DO UPDATE SET
```

- Execute commands from a file (e.g. import data):
```
\i <FILE-DESTINATION-PATH>
```

- Visualize all records from a table:
```
SELECT * FROM <TABLE-NAME>;
# * = select every column from table
# to select specific columns comma (,) separate each column name
```

- Sort records from a table:
```
SELECT * FROM <TABLE-NAME>
ORDER BY <COLUMN-NAME-TO-SORT-DATA-FROM>;
# By default data is sorted in ascending order (ASC),
# for descending order specify (DESC).
```

- Display column record whiteout duplicates and sort by ascending order:
```
SELECT DISTINCT <COLUMN-NAME> FROM <TABLE-NAME>
ORDER BY <COLUMN-NAME-TO-SORT-DATA-FROM>;
```

- Where clause and conditions:
```
SELECT * FROM <TABLE-NAME>
WHERE <COLUMN-NAME> = <SOME-VALUE> AND (<SECOND-COLUMN-NAME> = <SOME-VALUE> OR <SECOND-COLUMN-NAME> = <SOME-OTHER-VALUE>);
# Instead of using =, other comparison operators can be used such as <, >=, <=, >, <> (not equal).
```

- Limit the number of rows to return and add initial offset (row to skip at the beginning):
```
SELECT * FROM <TABLE-NAME> OFFSET <NUMBER-OF-ROWS-TO-SKIP> LIMIT <NUMBER-OF-ROWS>;
```

- Return rows having a column value matching one of the elements in a list:
```
SELECT * FROM <TABLE-NAME> WHERE <COLUMN-NAME> IN (<COMMA-SEPARATED-LIST>);
```

- Select Data Between a Range:
```
SELECT * FROM <TABLE-NAME> WHERE <COLUMN-NAME> BETWEEN <RANGE-START> AND <RANGE-END>;
```

- Select Data which meets a certain pattern:
```
SELECT * FROM <TABLE-NAME> WHERE <COLUMN-NAME> LIKE <CHOSEN-PATTERN>;
# % can be used as variable for identifying patterns (eg. %google.com finds
# every string which ends in google.com). To work with single variable character,
# an underscore (_) can be used.
# If when searching for a pattern, we want the search to not be case sensitive,
# we can then use ILIKE instead of LIKE.
```

- Calculate counts for each distinct element in a column:
```
SELECT <COLUMN-NAME>, COUNT(*) FROM <TABLE-NAME> GROUP BY <COLUMN-NAME>;
```

- Calculate counts for each distinct element in a column and filter the result by a condition:
```
SELECT <COLUMN-NAME>, COUNT(*) FROM <TABLE-NAME> GROUP BY <COLUMN-NAME> HAVING COUNT(*) <PREFERRED-CONDITION>;
```

- Aggregate Functions examples:
```
SELECT MAX(<COLUMN-NAME>) FROM <TABLE-NAME>;
# other examples are: MIN(), AVG(), SUM() ...
```

- Renaming a column:
```
SELECT MAX(<COLUMN-NAME>) AS <NEW-COLUMN-NAME> FROM <TABLE-NAME>;
```

- Assign a default value in case of NaN:
```
SELECT COALESCE(<COLUMN-NAME>, <PREFERRED-DEFAULT-VALUE>) FROM <TABLE-NAME>;
```

- Assign a default value in case of division by zero:
```
# calculated example, if two values in nullif are equal a null value
# is returned. In coalesce, the null value is then replaced with a
# 0 default value.
SELECT COALESCE(10/NULLIF(0, 0), 0);
```

- Adding and subtracting dates:
```
SELECT NOW()::DATE + INTERVAL 'Preferred Interval')::DATE;
# example: SELECT NOW()::DATE + INTERVAL '10 YEARS')::DATE;
```

- Extract field from dates:
```
SELECT EXTRACT(<FIELD> FROM <DATE>);
# example: SELECT EXTRACT(MONTH FROM NOW());
# other field options can be YEAR, DAY, etc..
```

- Modify constraints of a table:
```
# Add constraint
ALTER TABLE <TABLE-NAME> ADD CONSTRAINT <CONSTRAINT-NAME-AND-TYPE>;
# Remove constraint
ALTER TABLE <TABLE-NAME> DROP CONSTRAINT <CONSTRAINT-NAME-AND-TYPE>;
```

- Update records in a table:
```
UPDATE <TABLE-NAME> SET <COLUMN-TO-UPDATE>= <PREFERRED VALUE> WHERE <IDENTIFIER-COLUMN>=<PREFERRED-VALUE>;
```

- Inner Join:
```
SELECT * FROM <TABLE-NAME> JOIN <SECOND-TABLE-NAME> ON <TABLE-NAME>.<COMMON-COLUMN> = <SECOND-TABLE-NAME>.<SECOND-COMMON-COLUMN>;
```

- Left Join:
```
SELECT * FROM <TABLE-NAME> LEFT JOIN <SECOND-TABLE-NAME> ON <TABLE-NAME>.<COMMON-COLUMN> = <SECOND-TABLE-NAME>.<SECOND-COMMON-COLUMN>;
```

- Exporting a query to CSV:
```
\copy(<AN-SQL-QUERY-OF-YOUR-CHOICE>) TO <LOCAL-PATH-To-SAVED-FILE> DELIMITER ',' CSV HEADER
```

## Useful Links
- [SQL Tutorial PostgreSQL Full Course](https://www.youtube.com/watch?v=4smnWU0BhrA&ab_channel=Amigoscode)
