from peewee import Model, CharField, TextField
from . import db  # importer l'objet db de __init__.py

class BaseModel(Model):
    class Meta:
        database = db

class Article(BaseModel):
    title = CharField()
    summary = TextField()
    content = TextField()
