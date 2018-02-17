"""
Create table album_song_musicians
"""

from yoyo import step

__depends__ = {'20180203_05_S7xdB-create-table-album-songs'}

steps = [
    step("create table album_song_musicians (id serial primary key, album_song_id int4 references album_songs(id), musician_id int4 references musicians(id));")
]
