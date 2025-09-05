from peewee import *

db = SqliteDatabase("database")

class Model(Model):
    class Meta:
        database = db
