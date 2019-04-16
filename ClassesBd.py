from peewee import *

# Connect to a Postgres database.
pg_db = PostgresqlDatabase('listenpricing', user='postgres', password='12345678',
                           host='localhost', port=5432)
"""psql_db = PostgresqlDatabase('my_database', user='postgres')"""

class BaseModel(Model):
    class Meta:
        database = pg_db

class Users(BaseModel):
    id_user = AutoField()
    name = TextField()
    email = CharField(50)
    password = CharField(16)

class Rules(BaseModel):
    id_rule = AutoField()
    name = CharField(30)
    frequency = TimeField()
    description = TextField(null=True)

class MonitoringGroup(BaseModel):
    id_group = AutoField()
    name = CharField(30)
    description = TextField(null=True)
    rule = ForeignKeyField(Rules, backref='groups', on_delete='cascade', on_update='cascade')
    user = ForeignKeyField(Users, backref='groups', on_delete='cascade', on_update='cascade')

class Products(BaseModel):
    id_product = AutoField()
    name = CharField(50)
    link = CharField(100)
    tag = TextField()
    group = ForeignKeyField(MonitoringGroup, backref='products', on_delete='cascade', on_update='cascade')

class Prices(BaseModel):
    id_price = AutoField()
    value = DecimalField(6,2)
    date = DateTimeField(default = 'Now')
    product = ForeignKeyField(Products, backref='prices', on_delete='cascade', on_update='cascade')

pg_db.connect()
pg_db.create_tables([Users, Rules, MonitoringGroup, Products, Prices])
pg_db.close()
#user = Users(name = "Gustavo", email = 'Guga@hotmail.com', password='Irineu')
#user.save()
#rule = Rules(name="regra 1", frequency="02:00:00", description="esta regra ira buscar todos os produtos cadastrados")
#rule.save()
#group = MonitoringGroup(name="Grupo numero 1", description="Cozinha", user=1, rule=1)
#group.save()
#for Users in Users.select():
#    print(Users.name)
#rule = Rules(id_rule = 2)
#print(rule.delete_instance())

#print(MonitoringGroup.get().user.name)
#print("Finish")

def create_user(name, email, password):
    pg_db.connect()
    user = Users(name = name, email = email, password=password)
    user.save()
    pg_db.close()
    print('salvo')

def create_rule(name, frequency, description):
    pg_db.connect()
    rule = Users(name = name, frequency = frequency, description = description)
    rule.save()
    pg_db.close()
    print('salvo')

def update_rule(id_rule, name= "", frequency = "", description = ""):
    try:
        pg_db.connect()
        rule = Rules.get(Rules.id_rule == id_rule)
        if(name != ""):
            rule.name = name
        if(frequency != ""):
            rule.frequency = frequency
        if(description != ""):
            rule.description = description
        rule.save()
        pg_db.close()
    except(Exception):
        print("id não encontrado")

def delete_product(id_product):
    try:
        pg_db.connect()
        product = Products.get(Products.id_product == id_product)
        product.delete_instance()
        pg_db.close()
    except(Exception):
        print("produto não encontrado!")


#print(frequency)
#rule = Rules.get(Rules.id_rule == 10000)
#print(rule)

update_rule(id_rule = 1, name = "bbbbbbb")
print('oi')