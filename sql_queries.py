# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = (""" 
    CREATE TABLE IF NOT EXISTS songplays( 
        songplay_id SERIAL PRIMARY KEY, 
        session_id smallint, 
        location varchar, 
        user_agent varchar, 
        level varchar,
        start_time timestamp REFERENCES time(start_time),
        user_id VARCHAR REFERENCES users(user_id),
        song_id VARCHAR REFERENCES songs(song_id),
        artist_id VARCHAR REFERENCES artists(artist_id)
    )
""")

user_table_create = (""" 
    CREATE TABLE IF NOT EXISTS users( 
        user_id VARCHAR PRIMARY KEY, 
        first_name varchar, 
        last_name varchar, 
        gender varchar, 
        level varchar 
    )
""")

artist_table_create = (""" 
    CREATE TABLE IF NOT EXISTS artists( 
        artist_id VARCHAR PRIMARY KEY, 
        name VARCHAR, 
        location VARCHAR, 
        latitude numeric, 
        longitude numeric 
    )
""")

song_table_create = (""" 
    CREATE TABLE IF NOT EXISTS songs( 
        song_id VARCHAR PRIMARY KEY, 
        title varchar, 
        year smallint, 
        duration numeric,
        artist_id VARCHAR
    )
""")

time_table_create = (""" 
    CREATE TABLE IF NOT EXISTS time( 
        start_time TIMESTAMP PRIMARY KEY, 
        hour SMALLINT, 
        day SMALLINT, 
        week varchar, 
        month SMALLINT, 
        year SMALLINT, 
        weekday VARCHAR 
    )
""")

# INSERT RECORDS

songplay_table_insert = ("""
    INSERT INTO songplays(session_id, location, user_agent, level, start_time, user_id, song_id, artist_id)
    VALUES(%s, %s, %s, %s, %s, %s, %s, %s)
""")

user_table_insert = ("""
    INSERT INTO users(user_id, first_name, last_name, gender, level)
    VALUES(%s, %s, %s, %s, %s)
    ON CONFLICT(user_id)
    DO UPDATE SET level = EXCLUDED.level
""")

song_table_insert = ("""
    INSERT INTO songs(song_id, title, year, duration, artist_id)
    VALUES(%s, %s, %s, %s, %s)
    ON CONFLICT (song_id) 
    DO NOTHING
""")

artist_table_insert = ("""
    INSERT INTO artists(artist_id, name, location, latitude, longitude)
    VALUES(%s, %s, %s, %s, %s)
    ON CONFLICT (artist_id) 
    DO NOTHING
""")


time_table_insert = ("""
    INSERT INTO time (start_time, hour, day, week, month, year, weekday)
    VALUES(%s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (start_time) 
    DO NOTHING
""")

# FIND SONGS

song_select = ("""
    SELECT 
        s.song_id,
        a.artist_id
    FROM songs s
    JOIN artists a
    ON s.artist_id = a.artist_id
    WHERE s.title = %s AND a.name = %s AND s.duration = %s 
""")

# QUERY LISTS

create_table_queries = [user_table_create, artist_table_create, song_table_create, time_table_create, songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]