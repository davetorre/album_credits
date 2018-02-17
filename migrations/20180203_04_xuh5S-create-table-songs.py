"""
Create table songs
"""

from yoyo import step

__depends__ = {'20180203_03_UXJVv-create-table-musicians'}

steps = [
    step("create table songs (id serial primary key, name varchar(255));")
]
