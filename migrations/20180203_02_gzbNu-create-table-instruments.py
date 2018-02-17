"""
Create table instruments
"""

from yoyo import step

__depends__ = {'20180203_01_NSf0j-add-table-albums'}

steps = [
    step("create table instruments (id serial primary key, name varchar(255));")
]
