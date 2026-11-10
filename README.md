# WordWorld 3D — Explore Everything

A visual knowledge encyclopedia for exploring subjects across
space, nature, the human body, science, technology, geography,
and history.

## Technology Stack

- Python
- FastAPI
- HTML, CSS, JavaScript
- SQLite
- SQLAlchemy
- Three.js
- pytest

## Project Status

Currently under development.


1. Is the database approach we're using fundamental?
Yes, but there's an important distinction.

We are using SQLAlchemy ORM, which is one approach to working with databases in Python.

There are several approaches:
Approach 1: Raw SQL

You write SQL statements yourself.
cursor.execute(    "SELECT * FROM subjects")



You communicate with the database using SQL.

Approach 2: SQLAlchemy Core

You use SQLAlchemy's SQL expression tools to construct database operations.
statement = select(subjects)



You construct SQL operations using Python expressions.

Approach 3: SQLAlchemy ORM

You work with Python classes and objects.