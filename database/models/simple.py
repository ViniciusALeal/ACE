"""
ID_genoma
fk_TB_Script_script
"""
from peewee import *
from database.database import *
from database.models.TB_Script import*
from database.models.TB_Genoma import *

class simple(Model):
    script = ForeignKeyField (TB_script)
    ID_genoma = ForeignKeyField(tb_genoma)