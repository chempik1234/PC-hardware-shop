import datetime
import sqlalchemy
# from . import sockets
# from sqlalchemy import orm, ForeignKeyConstraint
from sqlalchemy_serializer import *
from .db_session import SqlAlchemyBase, global_init, create_session
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


class Motherboard(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'motherboard'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    warranty = sqlalchemy.Column(sqlalchemy.String)
    country = sqlalchemy.Column(sqlalchemy.String)
    title = sqlalchemy.Column(sqlalchemy.String)
    year = sqlalchemy.Column(sqlalchemy.Integer)
    form_factor = sqlalchemy.Column(sqlalchemy.String)
    width = sqlalchemy.Column(sqlalchemy.Integer)
    height = sqlalchemy.Column(sqlalchemy.String)
    socket = sqlalchemy.Column(sqlalchemy.String)
    chipset = sqlalchemy.Column(sqlalchemy.String)
    built_in_cpu = sqlalchemy.Column(sqlalchemy.Boolean)
    title_built_in_cpu = sqlalchemy.Column(sqlalchemy.String)
    memory_slots_amount = sqlalchemy.Column(sqlalchemy.Integer)
    memory_type = sqlalchemy.Column(sqlalchemy.String)
    ram_freq = sqlalchemy.Column(sqlalchemy.String)
    max_memory = sqlalchemy.Column(sqlalchemy.Integer)
    memory_channels_amount = sqlalchemy.Column(sqlalchemy.Integer)
    memory_form_factor = sqlalchemy.Column(sqlalchemy.String)
    m2_slots_amount = sqlalchemy.Column(sqlalchemy.Integer)
    sata_slots_amount = sqlalchemy.Column(sqlalchemy.Integer)
    nvme_support = sqlalchemy.Column(sqlalchemy.Boolean)
    sata_raid_mode = sqlalchemy.Column(sqlalchemy.String)
    m2_slots = sqlalchemy.Column(sqlalchemy.String)
    m2_form_factor = sqlalchemy.Column(sqlalchemy.String)
    other_drive_slots = sqlalchemy.Column(sqlalchemy.String)
    pci_express_version = sqlalchemy.Column(sqlalchemy.String)
    pci_e_x1_slots_amount = sqlalchemy.Column(sqlalchemy.Integer)
    pci_e_x16_slots_amount = sqlalchemy.Column(sqlalchemy.Integer)
    sli_crossfire_support = sqlalchemy.Column(sqlalchemy.Boolean)
    other_expansion_slots = sqlalchemy.Column(sqlalchemy.String)
    video_outputs = sqlalchemy.Column(sqlalchemy.String)
    usb_amount_and_type = sqlalchemy.Column(sqlalchemy.String)
    digital_and_audio_ports_s_pdif = sqlalchemy.Column(sqlalchemy.String)
    other_slots_on_back_panel = sqlalchemy.Column(sqlalchemy.String)
    network_ports_amount_rj45 = sqlalchemy.Column(sqlalchemy.Integer)
    fan_4pin_connectors = sqlalchemy.Column(sqlalchemy.Integer)
    internal_connectors_on_usb_plate_amount_and_type = sqlalchemy.Column(sqlalchemy.String)
    cpu_cooler_power_slot = sqlalchemy.Column(sqlalchemy.String)
    m2_e_key = sqlalchemy.Column(sqlalchemy.Boolean)
    lpt_interface = sqlalchemy.Column(sqlalchemy.Boolean)
    sound_adapter_chipset = sqlalchemy.Column(sqlalchemy.String)
    sound_scheme = sqlalchemy.Column(sqlalchemy.String)
    built_in_wifi_adapter = sqlalchemy.Column(sqlalchemy.String)
    bluetooth = sqlalchemy.Column(sqlalchemy.String)
    network_adapter_speed = sqlalchemy.Column(sqlalchemy.String)
    network_adapter_chipset = sqlalchemy.Column(sqlalchemy.String)
    power_phases_amount = sqlalchemy.Column(sqlalchemy.Integer)
    cpu_power_slot = sqlalchemy.Column(sqlalchemy.String)
    passive_cooling = sqlalchemy.Column(sqlalchemy.String)
    main_power_slot = sqlalchemy.Column(sqlalchemy.String)
    illumination = sqlalchemy.Column(sqlalchemy.Boolean)
    description = sqlalchemy.Column(sqlalchemy.String)
    price = sqlalchemy.Column(sqlalchemy.Integer)
    rating = sqlalchemy.Column(sqlalchemy.Integer)
    rates = sqlalchemy.Column(sqlalchemy.Integer)


class RAM_DIMM(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'ram_dimm'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    warranty = sqlalchemy.Column(sqlalchemy.String)
    country = sqlalchemy.Column(sqlalchemy.String)
    title = sqlalchemy.Column(sqlalchemy.String)
    year = sqlalchemy.Column(sqlalchemy.Integer)
    common_type = sqlalchemy.Column(sqlalchemy.String)
    type_ddr = sqlalchemy.Column(sqlalchemy.String)
    one_module_memory = sqlalchemy.Column(sqlalchemy.Integer)
    all_memory = sqlalchemy.Column(sqlalchemy.Integer)
    modules_amount = sqlalchemy.Column(sqlalchemy.Integer)
    ecc_memory = sqlalchemy.Column(sqlalchemy.Boolean)
    rang = sqlalchemy.Column(sqlalchemy.Integer)
    register_memory = sqlalchemy.Column(sqlalchemy.Boolean)
    freq = sqlalchemy.Column(sqlalchemy.Integer)
    intel_xpm_profiles = sqlalchemy.Column(sqlalchemy.String)
    modes = sqlalchemy.Column(sqlalchemy.Integer)
    cas_latency_cl = sqlalchemy.Column(sqlalchemy.Float)
    ras_to_cas_delay_trcd = sqlalchemy.Column(sqlalchemy.Integer)
    row_precharge_delay_trp = sqlalchemy.Column(sqlalchemy.Integer)
    has_radiator = sqlalchemy.Column(sqlalchemy.Boolean)
    illumination = sqlalchemy.Column(sqlalchemy.Boolean)
    height = sqlalchemy.Column(sqlalchemy.Integer)
    radiator_color = sqlalchemy.Column(sqlalchemy.String)
    low_profile = sqlalchemy.Column(sqlalchemy.Boolean)
    power_voltage = sqlalchemy.Column(sqlalchemy.Float)
    description = sqlalchemy.Column(sqlalchemy.String)
    price = sqlalchemy.Column(sqlalchemy.Integer)
    rating = sqlalchemy.Column(sqlalchemy.Integer)
    rates = sqlalchemy.Column(sqlalchemy.Integer)


class RAM_SO_DIMM(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'ram_so_dimm'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    warranty = sqlalchemy.Column(sqlalchemy.String)
    country = sqlalchemy.Column(sqlalchemy.String)
    title = sqlalchemy.Column(sqlalchemy.String)
    common_type = sqlalchemy.Column(sqlalchemy.String)
    type_ddr = sqlalchemy.Column(sqlalchemy.String)
    one_module_memory = sqlalchemy.Column(sqlalchemy.Integer)
    all_memory = sqlalchemy.Column(sqlalchemy.Integer)
    modules_amount = sqlalchemy.Column(sqlalchemy.Integer)
    freq = sqlalchemy.Column(sqlalchemy.Integer)
    ras_to_cas_delay_trcd = sqlalchemy.Column(sqlalchemy.Integer)
    row_precharge_delay_trp = sqlalchemy.Column(sqlalchemy.Integer)
    cas_latency_cl = sqlalchemy.Column(sqlalchemy.Float)
    chips_amount = sqlalchemy.Column(sqlalchemy.Integer)
    double_sided_chips_setup = sqlalchemy.Column(sqlalchemy.Boolean)
    power_voltage = sqlalchemy.Column(sqlalchemy.Float)
    description = sqlalchemy.Column(sqlalchemy.String)
    price = sqlalchemy.Column(sqlalchemy.Integer)
    rating = sqlalchemy.Column(sqlalchemy.Integer)
    rates = sqlalchemy.Column(sqlalchemy.Integer)


class SSD(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'ssd'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    warranty = sqlalchemy.Column(sqlalchemy.Integer)
    title = sqlalchemy.Column(sqlalchemy.String)
    year = sqlalchemy.Column(sqlalchemy.Integer)
    ssd_type = sqlalchemy.Column(sqlalchemy.String)
    memory = sqlalchemy.Column(sqlalchemy.Integer)
    phys_interface = sqlalchemy.Column(sqlalchemy.String)
    bit_per_cell_amount = sqlalchemy.Column(sqlalchemy.String)
    memory_structure = sqlalchemy.Column(sqlalchemy.String)
    DRAM_buffer = sqlalchemy.Column(sqlalchemy.Boolean)
    max_cons_reading_speed = sqlalchemy.Column(sqlalchemy.Integer)
    max_cons_writing_speed = sqlalchemy.Column(sqlalchemy.Integer)
    max_writing_resource_TBW = sqlalchemy.Column(sqlalchemy.Integer)
    DWPD = sqlalchemy.Column(sqlalchemy.Float)
    hardware_data_encryption = sqlalchemy.Column(sqlalchemy.Boolean)
    width = sqlalchemy.Column(sqlalchemy.Integer)
    form_factor = sqlalchemy.Column(sqlalchemy.Boolean)  # 2.5'' - 0, msata - 1
    description = sqlalchemy.Column(sqlalchemy.String)
    price = sqlalchemy.Column(sqlalchemy.Integer)
    rating = sqlalchemy.Column(sqlalchemy.Integer)
    rates = sqlalchemy.Column(sqlalchemy.Integer)


class HDD35(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'hdd35'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    warranty = sqlalchemy.Column(sqlalchemy.Integer)
    country = sqlalchemy.Column(sqlalchemy.String)
    title = sqlalchemy.Column(sqlalchemy.String)
    year = sqlalchemy.Column(sqlalchemy.Integer)
    memory_bits = sqlalchemy.Column(sqlalchemy.Integer)
    rotation_speed = sqlalchemy.Column(sqlalchemy.Integer)
    cash_memory_bits = sqlalchemy.Column(sqlalchemy.Integer)
    raid_massives_optimization = sqlalchemy.Column(sqlalchemy.Boolean)
    helium_fill = sqlalchemy.Column(sqlalchemy.Boolean)
    noise_dba = sqlalchemy.Column(sqlalchemy.Integer)
    writing_tech_CMR_SMR = sqlalchemy.Column(sqlalchemy.Boolean)  # cmr - 0, smr - 1
    position_park_cycles_amount = sqlalchemy.Column(sqlalchemy.Integer)
    width = sqlalchemy.Column(sqlalchemy.Integer)
    length = sqlalchemy.Column(sqlalchemy.Integer)
    height = sqlalchemy.Column(sqlalchemy.Integer)
    description = sqlalchemy.Column(sqlalchemy.String)
    price = sqlalchemy.Column(sqlalchemy.Integer)
    rating = sqlalchemy.Column(sqlalchemy.Integer)
    rates = sqlalchemy.Column(sqlalchemy.Integer)


class Opinion(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'opinion'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer)
    text = sqlalchemy.Column(sqlalchemy.String)
    image = sqlalchemy.Column(sqlalchemy.String)
    pr_type = sqlalchemy.Column(sqlalchemy.Integer)  # cpu gpu motherboard ramDIMM ramSODIMM ssd hdd
    pr_title = sqlalchemy.Column(sqlalchemy.String)
