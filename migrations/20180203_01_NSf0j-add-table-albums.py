"""
Add table albums
"""

from yoyo import step

__depends__ = {}

steps = [
    step("create table albums (id serial primary key, name varchar(255));")
]
