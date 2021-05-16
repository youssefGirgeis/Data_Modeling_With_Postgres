# Project: Data Modeling with Postgres

## Purpose
A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app.
The analytics team is particularly interested in understanding what songs users are listening to. Currently, 
they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, 
as well as a directory with JSON metadata on the songs in their app.

## Tasks
<ol>
<li>Create a database schema</li>
<li>ETL pipeline for the analysis</li>
</ol>

### Task #1: Database
The database consists of five tables, one fact table (songplays) and four dimension tables (users, artists, songs, and time) for **star** schema. Two files are used to create the database schema and populate the tables with data. In the "create_tables.py" file, we reset the the five tables before each time you run your ETL scripts by dropping and creating the tables. I also have "sql_queries.py" file, which contains all the sql queries.

### Task #2: ETL pipeline
Currently the data resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app. My task now is write an ETL pipeline that transfers data from files in the two directories into the tables mentioned above using Python and SQL. We created a file (etl.py) to perform the ETL process. It reads and processes files from song_data and log_data directories and loads them into the five tables. For testing purposes, I created two notebooks (etl.ipynb and test.ipynb) to test the ETL piepline.


