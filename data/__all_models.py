import datetime
import sqlalchemy
# from . import sockets
# from sqlalchemy import orm, ForeignKeyConstraint
from sqlalchemy_serializer import *
from .db_session import SqlAlchemyBase
from flask_login import UserMixin


class User(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    surname = sqlalchemy.Column(sqlalchemy.String)
    name = sqlalchemy.Column(sqlalchemy.String)
    email = sqlalchemy.Column(sqlalchemy.String, unique=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String)
    modified_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                      default=datetime.datetime.now)

    def check_password(self, password):
        return password == self.hashed_password


class CPU(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'cpu'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    warranty = sqlalchemy.Column(sqlalchemy.Integer)
    country = sqlalchemy.Column(sqlalchemy.String)
    title = sqlalchemy.Column(sqlalchemy.String)
    generation = sqlalchemy.Column(sqlalchemy.String)
    year = sqlalchemy.Column(sqlalchemy.Integer)
    # sockets = orm.relation("Sockets",
    #                        secondary="association",
    #                        backref="cpu")
    socket = sqlalchemy.Column(sqlalchemy.String)
    has_cooling = sqlalchemy.Column(sqlalchemy.Boolean)
    term_interface = sqlalchemy.Column(sqlalchemy.Boolean)
    cores = sqlalchemy.Column(sqlalchemy.Integer)
    threads = sqlalchemy.Column(sqlalchemy.Integer)
    tech_process = sqlalchemy.Column(sqlalchemy.Integer)
    core = sqlalchemy.Column(sqlalchemy.String)
    cash_l1_instructions_bits = sqlalchemy.Column(sqlalchemy.Integer)
    cash_l1_data_bits = sqlalchemy.Column(sqlalchemy.Integer)
    cash_l2_bits = sqlalchemy.Column(sqlalchemy.Integer)
    cash_l3_bits = sqlalchemy.Column(sqlalchemy.Integer)
    base_freq = sqlalchemy.Column(sqlalchemy.Integer)
    max_freq = sqlalchemy.Column(sqlalchemy.Integer)
    free_mult = sqlalchemy.Column(sqlalchemy.Boolean)
    memory = sqlalchemy.Column(sqlalchemy.String)
    max_mem_bits = sqlalchemy.Column(sqlalchemy.Integer)
    channels = sqlalchemy.Column(sqlalchemy.Integer)
    min_RAM_freq = sqlalchemy.Column(sqlalchemy.Integer)
    max_RAM_freq = sqlalchemy.Column(sqlalchemy.Integer)
    ECC = sqlalchemy.Column(sqlalchemy.Boolean)
    TDP = sqlalchemy.Column(sqlalchemy.Integer)
    custom_TDP = sqlalchemy.Column(sqlalchemy.Boolean)
    max_temp = sqlalchemy.Column(sqlalchemy.Integer)
    has_graphics = sqlalchemy.Column(sqlalchemy.Boolean)
    PCI = sqlalchemy.Column(sqlalchemy.String)
    PCI_amount = sqlalchemy.Column(sqlalchemy.Integer)
    bandwidth = sqlalchemy.Column(sqlalchemy.Float)
    support_x64 = sqlalchemy.Column(sqlalchemy.String)
    multi_thread = sqlalchemy.Column(sqlalchemy.Boolean)
    add_freq_tech = sqlalchemy.Column(sqlalchemy.String)
    energy_save_tech = sqlalchemy.Column(sqlalchemy.String)
    description = sqlalchemy.Column(sqlalchemy.String)
    price = sqlalchemy.Column(sqlalchemy.Integer)
    rating = sqlalchemy.Column(sqlalchemy.Float)
