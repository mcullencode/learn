"""
Database: the containter for all the data you store

in sqlite, the entire database is stored in a single file, however with companies this
is likely not the case

Database Dictionary: provides a comprehensive list of the structure and types of data in
the database

Table: a collection of related data held in the database, i.e. invoices,
contacts could be individual tables

Field: the basic unit of data in a table.

An invoice table has Invoice, Date, Description and Amount fields.

Record: is a row/column which contains a value for Date, Description etc for a single invoice

A flat file database stores all the data in a single table.
This results in a lot of duplication

A View is a selection of rows and columns, possible from more than one table

"""