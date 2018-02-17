"""
Create table musicians
"""

from yoyo import step

__depends__ = {'20180203_02_gzbNu-create-table-instruments'}

steps = [
    step("create table musicians (id serial primary key, name varchar(255), instrument_id int4 references instruments(id));")
]
