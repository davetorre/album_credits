"""
Create table album_songs
"""

from yoyo import step

__depends__ = {'20180203_04_xuh5S-create-table-songs'}

steps = [
    step("create table album_songs (id serial primary key, album_id int4 references albums(id), song_id int4 references songs(id));")
]
