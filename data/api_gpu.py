import flask
from data.__all_models import *
from flask import request
from data import db_session


blueprint = flask.Blueprint('gpu_api', __name__, template_folder='templates')


@blueprint.route('/api/gpu', methods=['GET'])
def get_gpus():
    db_sess = db_session.create_session()
    gpu = db_sess.query(GPU).all()
    return flask.jsonify({'gpu': [item.to_dict(
        only=("id", "warranty",
              "country", "title",
              "year", "manufacturer_code",
              "is_for_mining", "LHR",
              "memory", "memory_type",
              "bandwidth", "band_64x_32x",
              "max_mem_bandwidth", "micro_arc",
              "graph_cpu", "techprocess",
              "chip_freq", "ALU",
              "texture_blocks", "raster_blocks",
              "max_temp", "RTX",
              "appart_accelerate_RT", "tenz_cores",
              "max_efficiency_FP32", "connectors",
              "HDMI_version", "max_resolution",
              "max_monitors", "connection_interface",
              "PCI_version", "support_mult_cpu_config",
              "need_extra_power", "extra_power_connections",
              "max_consuming_power", "recommended_power",
              "cooling", "type_and_amount_fans",
              "fan_speed_control", "low_profile",
              "needed_slots", "length", "width",
              "weight", "illumination", "synch_RGB",
              "LCD", "BIOS_switch", "description",
              "price", "rating", "rates"))
        for item in gpu]})


@blueprint.route('/api/gpu_add', methods=['POST'])
def add_gpu():
    db_sess = db_session.create_session()
    if not request.json:
        return flask.jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ["id", "warranty", "country",
                  "title", "year", "manufacturer_code",
                  "is_for_mining", "LHR", "memory",
                  "memory_type", "bandwidth", "band_64x_32x",
                  "max_mem_bandwidth", "micro_arc", "graph_cpu",
                  "techprocess", "chip_freq", "ALU",
                  "texture_blocks", "raster_blocks",
                  "max_temp", "RTX", "appart_accelerate_RT",
                  "tenz_cores", "max_efficiency_FP32",
                  "connectors", "HDMI_version",
                  "max_resolution", "max_monitors",
                  "connection_interface", "PCI_version",
                  "support_mult_cpu_config", "need_extra_power",
                  "extra_power_connections", "max_consuming_power",
                  "recommended_power", "cooling",
                  "type_and_amount_fans", "fan_speed_control",
                  "low_profile", "needed_slots", "length",
                  "width", "weight", "illumination",
                  "synch_RGB", "LCD", "BIOS_switch",
                  "description", "price", "rating", "rates"]):
        return flask.jsonify({'error': 'Bad request'})
    elif db_sess.query(GPU).filter(GPU.id == request.json['id']).first():
        return flask.jsonify({'error': 'Id already exists'})
    gpu = GPU(
        id=request.json['id'],
        warranty=request.json.get("warranty"),
        country=request.json.get("country"),
        title=request.json.get("title"),
        year=request.json.get("year"),
        manufacturer_code=request.json.get("manufacturer_code"),
        is_for_mining=request.json.get("is_for_mining"),
        LHR=request.json.get("LHR"),
        memory=request.json.get("memory"),
        memory_type=request.json.get("memory_type"),
        bandwidth=request.json.get("bandwidth"),
        band_64x_32x=request.json.get("band_64x_32x"),
        max_mem_bandwidth=request.json.get("max_mem_bandwidth"),
        micro_arc=request.json.get("micro_arc"),
        graph_cpu=request.json.get("graph_cpu"),
        techprocess=request.json.get("techprocess"),
        chip_freq=request.json.get("chip_freq"),
        ALU=request.json.get("ALU"),
        texture_blocks=request.json.get("texture_blocks"),
        raster_blocks=request.json.get("raster_blocks"),
        max_temp=request.json.get("max_temp"),
        RTX=request.json.get("RTX"),
        appart_accelerate_RT=request.json.get("appart_accelerate_RT"),
        tenz_cores=request.json.get("tenz_cores"),
        max_efficiency_FP32=request.json.get("max_efficiency_FP32"),
        connectors=request.json.get("connectors"),
        HDMI_version=request.json.get("HDMI_version"),
        max_resolution=request.json.get("max_resolution"),
        max_monitors=request.json.get("max_monitors"),
        connection_interface=request.json.get("connection_interface"),
        PCI_version=request.json.get("PCI_version"),
        support_mult_cpu_config=request.json.get("support_mult_cpu_config"),
        need_extra_power=request.json.get("need_extra_power"),
        extra_power_connections=request.json.get("extra_power_connections"),
        max_consuming_power=request.json.get("max_consuming_power"),
        recommended_power=request.json.get("recommended_power"),
        cooling=request.json.get("cooling"),
        type_and_amount_fans=request.json.get("type_and_amount_fans"),
        fan_speed_control=request.json.get("fan_speed_control"),
        low_profile=request.json.get("low_profile"),
        needed_slots=request.json.get("needed_slots"),
        length=request.json.get("length"),
        width=request.json.get("width"),
        weight=request.json.get("weight"),
        illumination=request.json.get("illumination"),
        synch_RGB=request.json.get("synch_RGB"),
        LCD=request.json.get("LCD"),
        BIOS_switch=request.json.get("BIOS_switch"),
        description=request.json.get("description"),
        price=request.json.get("price"),
        rating=request.json.get("rating"),
        rates=request.json.get("rates")
    )
    db_sess.add(gpu)
    db_sess.commit()
    return flask.jsonify({'success': 'OK'})


@blueprint.route('/api/gpu_get/<int:_id>', methods=['GET'])
def get_gpu(_id):
    db_sess = db_session.create_session()
    gpu = db_sess.query(GPU).filter(GPU.id == _id).first()
    if not gpu:
        return flask.jsonify({'error': 'Not found'})
    return flask.jsonify(
        {
            'gpu': gpu.to_dict(only=(
                "id", "warranty",
                "country", "title",
                "year", "manufacturer_code",
                "is_for_mining", "LHR",
                "memory", "memory_type",
                "bandwidth", "band_64x_32x",
                "max_mem_bandwidth", "micro_arc",
                "graph_cpu", "techprocess",
                "chip_freq", "ALU",
                "texture_blocks", "raster_blocks",
                "max_temp", "RTX",
                "appart_accelerate_RT", "tenz_cores",
                "max_efficiency_FP32", "connectors",
                "HDMI_version", "max_resolution",
                "max_monitors", "connection_interface",
                "PCI_version", "support_mult_cpu_config",
                "need_extra_power", "extra_power_connections",
                "max_consuming_power", "recommended_power",
                "cooling", "type_and_amount_fans",
                "fan_speed_control", "low_profile",
                "needed_slots", "length", "width",
                "weight", "illumination", "synch_RGB",
                "LCD", "BIOS_switch", "description",
                "price", "rating", "rates")
            )
        }
    )


@blueprint.route('/api/gpu_delete/<int:_id>', methods=['DELETE'])
def delete_gpu(_id):
    db_sess = db_session.create_session()
    gpu = db_sess.query(GPU).get(_id)
    if not gpu:
        return flask.jsonify({'error': 'Not found'})
    db_sess.delete(gpu)
    db_sess.commit()
    return flask.jsonify({'success': 'OK'})


@blueprint.route('/api/cpu_edit/', methods=['PUT'])
def edit_cpu():
    db_sess = db_session.create_session()
    keyss = ["id", "warranty",
             "country", "title",
             "year", "manufacturer_code",
             "is_for_mining", "LHR",
             "memory", "memory_type",
             "bandwidth", "band_64x_32x",
             "max_mem_bandwidth", "micro_arc",
             "graph_cpu", "techprocess",
             "chip_freq", "ALU",
             "texture_blocks", "raster_blocks",
             "max_temp", "RTX",
             "appart_accelerate_RT", "tenz_cores",
             "max_efficiency_FP32", "connectors",
             "HDMI_version", "max_resolution",
             "max_monitors", "connection_interface",
             "PCI_version", "support_mult_cpu_config",
             "need_extra_power", "extra_power_connections",
             "max_consuming_power", "recommended_power",
             "cooling", "type_and_amount_fans",
             "fan_speed_control", "low_profile",
             "needed_slots", "length", "width",
             "weight", "illumination", "synch_RGB",
             "LCD", "BIOS_switch", "description",
             "price", "rating", "rates"]
    if not request.json:
        return flask.jsonify({'error': 'Empty request'})
    elif 'id' not in request.json or not all(key in keyss for key in request.json):
        return flask.jsonify({'error': 'Bad request'})
    elif not db_sess.query(GPU).filter(GPU.id == request.json['id']).first():
        return flask.jsonify({'error': 'Id does not exist'})
    gpu = GPU(
        id=request.json['id'],
        warranty=request.json.get("warranty"),
        country=request.json.get("country"),
        title=request.json.get("title"),
        year=request.json.get("year"),
        manufacturer_code=request.json.get("manufacturer_code"),
        is_for_mining=request.json.get("is_for_mining"),
        LHR=request.json.get("LHR"),
        memory=request.json.get("memory"),
        memory_type=request.json.get("memory_type"),
        bandwidth=request.json.get("bandwidth"),
        band_64x_32x=request.json.get("band_64x_32x"),
        max_mem_bandwidth=request.json.get("max_mem_bandwidth"),
        micro_arc=request.json.get("micro_arc"),
        graph_cpu=request.json.get("graph_cpu"),
        techprocess=request.json.get("techprocess"),
        chip_freq=request.json.get("chip_freq"),
        ALU=request.json.get("ALU"),
        texture_blocks=request.json.get("texture_blocks"),
        raster_blocks=request.json.get("raster_blocks"),
        max_temp=request.json.get("max_temp"),
        RTX=request.json.get("RTX"),
        appart_accelerate_RT=request.json.get("appart_accelerate_RT"),
        tenz_cores=request.json.get("tenz_cores"),
        max_efficiency_FP32=request.json.get("max_efficiency_FP32"),
        connectors=request.json.get("connectors"),
        HDMI_version=request.json.get("HDMI_version"),
        max_resolution=request.json.get("max_resolution"),
        max_monitors=request.json.get("max_monitors"),
        connection_interface=request.json.get("connection_interface"),
        PCI_version=request.json.get("PCI_version"),
        support_mult_cpu_config=request.json.get("support_mult_cpu_config"),
        need_extra_power=request.json.get("need_extra_power"),
        extra_power_connections=request.json.get("extra_power_connections"),
        max_consuming_power=request.json.get("max_consuming_power"),
        recommended_power=request.json.get("recommended_power"),
        cooling=request.json.get("cooling"),
        type_and_amount_fans=request.json.get("type_and_amount_fans"),
        fan_speed_control=request.json.get("fan_speed_control"),
        low_profile=request.json.get("low_profile"),
        needed_slots=request.json.get("needed_slots"),
        length=request.json.get("length"),
        width=request.json.get("width"),
        weight=request.json.get("weight"),
        illumination=request.json.get("illumination"),
        synch_RGB=request.json.get("synch_RGB"),
        LCD=request.json.get("LCD"),
        BIOS_switch=request.json.get("BIOS_switch"),
        description=request.json.get("description"),
        price=request.json.get("price"),
        rating=request.json.get("rating"),
        rates=request.json.get("rates")
    )
    if gpu.warranty:
        db_sess.query(GPU).filter(GPU.id == gpu.id).update(values={GPU.warranty: gpu.warranty})
    if gpu.country:
        db_sess.query(GPU).filter(GPU.id == gpu.id).update(values={GPU.country: gpu.country})
    if gpu.title:
        db_sess.query(GPU).filter(GPU.id == gpu.id).update(values={GPU.title: gpu.title})
    if gpu.year:
        db_sess.query(GPU).filter(GPU.id == gpu.id).update(values={GPU.year: gpu.year})
    if gpu.manufacturer_code:
        db_sess.query(GPU).filter(GPU.id == gpu.id).update(values={GPU.manufacturer_code: gpu.manufacturer_code})
    if gpu.is_for_mining:
        db_sess.query(GPU).filter(GPU.id == gpu.id).update(values={GPU.is_for_mining: gpu.is_for_mining})
    if gpu.LHR:
        db_sess.query(GPU).filter(GPU.id == gpu.id).update(values={GPU.LHR: gpu.LHR})
    if gpu.memory:
        db_sess.query(GPU).filter(GPU.id == gpu.id).update(values={GPU.memory: gpu.memory})
    if gpu.memory_type:
        db_sess.query(GPU).filter(GPU.id == gpu.id).update(values={GPU.memory_type: gpu.memory_type})
    if gpu.bandwidth:
        db_sess.query(GPU).filter(GPU.id == gpu.id).update(values={GPU.bandwidth: gpu.bandwidth})
    if gpu.band_64x_32x:
        db_sess.query(GPU).filter(GPU.id == gpu.id).update(values={GPU.band_64x_32x: gpu.band_64x_32x})
    if gpu.max_mem_bandwidth:
        db_sess.query(GPU).filter(GPU.id == gpu.id).update(values={GPU.max_mem_bandwidth: gpu.max_mem_bandwidth})
    if gpu.micro_arc:
        db_sess.query(GPU).filter(GPU.id == gpu.id).update(values={GPU.micro_arc: gpu.micro_arc})
    if gpu.graph_cpu:
        db_sess.query(GPU).filter(GPU.id == gpu.id).update(values={GPU.graph_cpu: gpu.graph_cpu})
    if gpu.techprocess:
        db_sess.query(GPU).filter(GPU.id == gpu.id).update(values={GPU.techprocess: gpu.techprocess})
    if gpu.chip_freq:
        db_sess.query(GPU).filter(GPU.id == gpu.id).update(values={GPU.chip_freq: gpu.chip_freq})
    if gpu.ALU:
        db_sess.query(GPU).filter(GPU.id == gpu.id).update(values={GPU.ALU: gpu.ALU})
    if gpu.texture_blocks:
        db_sess.query(GPU).filter(GPU.id == gpu.id).update(values={GPU.texture_blocks: gpu.texture_blocks})
    if gpu.raster_blocks:
        db_sess.query(GPU).filter(GPU.id == gpu.id).update(values={GPU.raster_blocks: gpu.raster_blocks})
    if gpu.max_temp:
        db_sess.query(GPU).filter(GPU.id == gpu.id).update(values={GPU.max_temp: gpu.max_temp})
    if gpu.RTX:
        db_sess.query(GPU).filter(GPU.id == gpu.id).update(values={GPU.RTX: gpu.RTX})
    if gpu.appart_accelerate_RT:
        db_sess.query(GPU).filter(GPU.id == gpu.id).update(values={GPU.appart_accelerate_RT: gpu.appart_accelerate_RT})
    if gpu.tenz_cores:
        db_sess.query(GPU).filter(GPU.id == gpu.id).update(values={GPU.tenz_cores: gpu.tenz_cores})
    if gpu.max_efficiency_FP32:
        db_sess.query(GPU).filter(GPU.id == gpu.id).update(values={GPU.max_efficiency_FP32: gpu.max_efficiency_FP32})
    if gpu.connectors:
        db_sess.query(GPU).filter(GPU.id == gpu.id).update(values={GPU.connectors: gpu.connectors})
    if gpu.HDMI_version:
        db_sess.query(GPU).filter(GPU.id == gpu.id).update(values={GPU.HDMI_version: gpu.HDMI_version})
    if gpu.max_resolution:
        db_sess.query(GPU).filter(GPU.id == gpu.id).update(values={GPU.max_resolution: gpu.max_resolution})
    if gpu.max_monitors:
        db_sess.query(GPU).filter(GPU.id == gpu.id).update(values={GPU.max_monitors: gpu.max_monitors})
    if gpu.connection_interface:
        db_sess.query(GPU).filter(GPU.id == gpu.id).update(values={GPU.connection_interface: gpu.connection_interface})
    if gpu.PCI_version:
        db_sess.query(GPU).filter(GPU.id == gpu.id).update(values={GPU.PCI_version: gpu.PCI_version})
    if gpu.support_mult_cpu_config:
        db_sess.query(GPU).filter(GPU.id == gpu.id).update(
            values={GPU.support_mult_cpu_config: gpu.support_mult_cpu_config})
    if gpu.need_extra_power:
        db_sess.query(GPU).filter(GPU.id == gpu.id).update(values={GPU.need_extra_power: gpu.need_extra_power})
    if gpu.extra_power_connections:
        db_sess.query(GPU).filter(GPU.id == gpu.id).update(
            values={GPU.extra_power_connections: gpu.extra_power_connections})
    if gpu.max_consuming_power:
        db_sess.query(GPU).filter(GPU.id == gpu.id).update(values={GPU.max_consuming_power: gpu.max_consuming_power})
    if gpu.recommended_power:
        db_sess.query(GPU).filter(GPU.id == gpu.id).update(values={GPU.recommended_power: gpu.recommended_power})
    if gpu.cooling:
        db_sess.query(GPU).filter(GPU.id == gpu.id).update(values={GPU.cooling: gpu.cooling})
    if gpu.type_and_amount_fans:
        db_sess.query(GPU).filter(GPU.id == gpu.id).update(values={GPU.type_and_amount_fans: gpu.type_and_amount_fans})
    if gpu.fan_speed_control:
        db_sess.query(GPU).filter(GPU.id == gpu.id).update(values={GPU.fan_speed_control: gpu.fan_speed_control})
    if gpu.low_profile:
        db_sess.query(GPU).filter(GPU.id == gpu.id).update(values={GPU.low_profile: gpu.low_profile})
    if gpu.needed_slots:
        db_sess.query(GPU).filter(GPU.id == gpu.id).update(values={GPU.needed_slots: gpu.needed_slots})
    if gpu.length:
        db_sess.query(GPU).filter(GPU.id == gpu.id).update(values={GPU.length: gpu.length})
    if gpu.width:
        db_sess.query(GPU).filter(GPU.id == gpu.id).update(values={GPU.width: gpu.width})
    if gpu.weight:
        db_sess.query(GPU).filter(GPU.id == gpu.id).update(values={GPU.weight: gpu.weight})
    if gpu.illumination:
        db_sess.query(GPU).filter(GPU.id == gpu.id).update(values={GPU.illumination: gpu.illumination})
    if gpu.synch_RGB:
        db_sess.query(GPU).filter(GPU.id == gpu.id).update(values={GPU.synch_RGB: gpu.synch_RGB})
    if gpu.LCD:
        db_sess.query(GPU).filter(GPU.id == gpu.id).update(values={GPU.LCD: gpu.LCD})
    if gpu.BIOS_switch:
        db_sess.query(GPU).filter(GPU.id == gpu.id).update(values={GPU.BIOS_switch: gpu.BIOS_switch})
    if gpu.description:
        db_sess.query(GPU).filter(GPU.id == gpu.id).update(values={GPU.description: gpu.description})
    if gpu.price:
        db_sess.query(GPU).filter(GPU.id == gpu.id).update(values={GPU.price: gpu.price})
    if gpu.rating:
        db_sess.query(GPU).filter(GPU.id == gpu.id).update(values={GPU.rating: gpu.rating})
    if gpu.rates:
        db_sess.query(GPU).filter(GPU.id == gpu.id).update(values={GPU.rates: gpu.rates})
    db_sess.commit()
    return flask.jsonify({'success': 'OK'})