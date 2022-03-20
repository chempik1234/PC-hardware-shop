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
    rating = sqlalchemy.Column(sqlalchemy.Integer)
    rates = sqlalchemy.Column(sqlalchemy.Integer)


class GPU(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'gpu'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    warranty = sqlalchemy.Column(sqlalchemy.String)
    country = sqlalchemy.Column(sqlalchemy.String)
    title = sqlalchemy.Column(sqlalchemy.String)
    year = sqlalchemy.Column(sqlalchemy.Integer)
    manufacturer_code = sqlalchemy.Column(sqlalchemy.String)
    is_for_mining = sqlalchemy.Column(sqlalchemy.Boolean)
    LHR = sqlalchemy.Column(sqlalchemy.Boolean)
    memory = sqlalchemy.Column(sqlalchemy.Integer)
    memory_type = sqlalchemy.Column(sqlalchemy.String)
    bandwidth = sqlalchemy.Column(sqlalchemy.Float)
    band_64x_32x = sqlalchemy.Column(sqlalchemy.String)
    max_mem_bandwidth = sqlalchemy.Column(sqlalchemy.Float)
    micro_arc = sqlalchemy.Column(sqlalchemy.String)
    graph_cpu = sqlalchemy.Column(sqlalchemy.String)
    techprocess = sqlalchemy.Column(sqlalchemy.Integer)
    chip_freq = sqlalchemy.Column(sqlalchemy.Integer)
    ALU = sqlalchemy.Column(sqlalchemy.Integer)
    texture_blocks = sqlalchemy.Column(sqlalchemy.Integer)
    raster_blocks = sqlalchemy.Column(sqlalchemy.Integer)
    max_temp = sqlalchemy.Column(sqlalchemy.Integer)
    RTX = sqlalchemy.Column(sqlalchemy.Boolean)
    appart_accelerate_RT = sqlalchemy.Column(sqlalchemy.Boolean)
    tenz_cores = sqlalchemy.Column(sqlalchemy.Integer)
    max_efficiency_FP32 = sqlalchemy.Column(sqlalchemy.Float)
    connectors = sqlalchemy.Column(sqlalchemy.String)
    HDMI_version = sqlalchemy.Column(sqlalchemy.String)
    max_resolution = sqlalchemy.Column(sqlalchemy.String)
    max_monitors = sqlalchemy.Column(sqlalchemy.Integer)
    connection_interface = sqlalchemy.Column(sqlalchemy.String)
    PCI_version = sqlalchemy.Column(sqlalchemy.String)
    support_mult_cpu_config = sqlalchemy.Column(sqlalchemy.String)
    need_extra_power = sqlalchemy.Column(sqlalchemy.Boolean)
    extra_power_connections = sqlalchemy.Column(sqlalchemy.Boolean)
    max_consuming_power = sqlalchemy.Column(sqlalchemy.Float)
    recommended_power = sqlalchemy.Column(sqlalchemy.Integer)
    cooling = sqlalchemy.Column(sqlalchemy.String)
    type_and_amount_fans = sqlalchemy.Column(sqlalchemy.String)
    fan_speed_control = sqlalchemy.Column(sqlalchemy.Boolean)
    low_profile = sqlalchemy.Column(sqlalchemy.Boolean)
    needed_slots = sqlalchemy.Column(sqlalchemy.Integer)
    length = sqlalchemy.Column(sqlalchemy.Integer)
    width = sqlalchemy.Column(sqlalchemy.Integer)
    weight = sqlalchemy.Column(sqlalchemy.Integer)
    illumination = sqlalchemy.Column(sqlalchemy.Boolean)
    synch_RGB = sqlalchemy.Column(sqlalchemy.Boolean)
    LCD = sqlalchemy.Column(sqlalchemy.Boolean)
    BIOS_switch = sqlalchemy.Column(sqlalchemy.Boolean)
    description = sqlalchemy.Column(sqlalchemy.String)
    price = sqlalchemy.Column(sqlalchemy.Integer)
    rating = sqlalchemy.Column(sqlalchemy.Integer)
    rates = sqlalchemy.Column(sqlalchemy.Integer)