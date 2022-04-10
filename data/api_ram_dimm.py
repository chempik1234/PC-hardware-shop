import flask
from data.__all_models import *
from flask import request
from data import db_session


blueprint = flask.Blueprint('ram_dimm_api', __name__, template_folder='templates')


@blueprint.route('/api/ram_dimm', methods=['GET'])
def get_ram_dimms():
    db_sess = db_session.create_session()
    rd = db_sess.query(RAM_DIMM).all()
    return flask.jsonify({'ram_dimm': [item.to_dict(
        only=("id", "warranty", "country", "title",
              "year", "common_type", "type_ddr",
              "one_module_memory", "all_memory",
              "modules_amount", "ecc_memory", "rang",
              "register_memory", "freq",
              "intel_xpm_profiles", "modes",
              "cas_latency_cl", "ras_to_cas_delay_trcd",
              "row_precharge_delay_trp", "has_radiator",
              "illumination", "height", "radiator_color",
              "low_profile", "power_voltage", "description",
              "price", "rating", "rates"))
        for item in rd]})


@blueprint.route('/api/ram_dimm_add', methods=['POST'])
def add_ram_dimm():
    db_sess = db_session.create_session()
    if not request.json:
        return flask.jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ["id", "warranty", "country", "title",
                  "year", "common_type", "type_ddr",
                  "one_module_memory", "all_memory",
                  "modules_amount", "ecc_memory", "rang",
                  "register_memory", "freq",
                  "intel_xpm_profiles", "modes",
                  "cas_latency_cl", "ras_to_cas_delay_trcd",
                  "row_precharge_delay_trp", "has_radiator",
                  "illumination", "height", "radiator_color",
                  "low_profile", "power_voltage", "description",
                  "price", "rating", "rates"]):
        return flask.jsonify({'error': 'Bad request'})
    elif db_sess.query(RAM_DIMM).filter(RAM_DIMM.id == request.json['id']).first():
        return flask.jsonify({'error': 'Id already exists'})
    rd = RAM_DIMM(
        id=request.json['id'],
        warranty=request.json.get("warranty"),
        country=request.json.get("country"),
        title=request.json.get("title"),
        year=request.json.get("year"),
        common_type=request.json.get("common_type"),
        type_ddr=request.json.get("type_ddr"),
        one_module_memory=request.json.get("one_module_memory"),
        all_memory=request.json.get("all_memory"),
        modules_amount=request.json.get("modules_amount"),
        ecc_memory=request.json.get("ecc_memory"),
        rang=request.json.get("rang"),
        register_memory=request.json.get("register_memory"),
        freq=request.json.get("freq"),
        intel_xpm_profiles=request.json.get("intel_xpm_profiles"),
        modes=request.json.get("modes"),
        cas_latency_cl=request.json.get("cas_latency_cl"),
        ras_to_cas_delay_trcd=request.json.get("ras_to_cas_delay_trcd"),
        row_precharge_delay_trp=request.json.get("row_precharge_delay_trp"),
        has_radiator=request.json.get("has_radiator"),
        illumination=request.json.get("illumination"),
        height=request.json.get("height"),
        radiator_color=request.json.get("radiator_color"),
        low_profile=request.json.get("low_profile"),
        power_voltage=request.json.get("power_voltage"),
        description=request.json.get("description"),
        price=request.json.get("price"),
        rating=request.json.get("rating"),
        rates=request.json.get("rates")
    )
    db_sess.add(rd)
    db_sess.commit()
    return flask.jsonify({'success': 'OK'})


@blueprint.route('/api/ram_dimm_get/<int:_id>', methods=['GET'])
def get_ram_dimm(_id):
    db_sess = db_session.create_session()
    rd = db_sess.query(RAM_DIMM).filter(RAM_DIMM.id == _id).first()
    if not rd:
        return flask.jsonify({'error': 'Not found'})
    return flask.jsonify(
        {
            'ram_dimm': rd.to_dict(only=(
                "id", "warranty", "country", "title",
                "year", "common_type", "type_ddr",
                "one_module_memory", "all_memory",
                "modules_amount", "ecc_memory", "rang",
                "register_memory", "freq",
                "intel_xpm_profiles", "modes",
                "cas_latency_cl", "ras_to_cas_delay_trcd",
                "row_precharge_delay_trp", "has_radiator",
                "illumination", "height", "radiator_color",
                "low_profile", "power_voltage", "description",
                "price", "rating", "rates")
            )
        }
    )


@blueprint.route('/api/ram_dimm_delete/<int:_id>', methods=['DELETE'])
def delete_ram_dimm(_id):
    db_sess = db_session.create_session()
    rd = db_sess.query(RAM_DIMM).get(_id)
    if not rd:
        return flask.jsonify({'error': 'Not found'})
    db_sess.delete(rd)
    db_sess.commit()
    return flask.jsonify({'success': 'OK'})


@blueprint.route('/api/ram_dimm_edit/', methods=['PUT'])
def edit_ram_dimm():
    db_sess = db_session.create_session()
    keyss = ["id", "warranty", "country", "title",
             "year", "common_type", "type_ddr",
             "one_module_memory", "all_memory",
             "modules_amount", "ecc_memory", "rang",
             "register_memory", "freq",
             "intel_xpm_profiles", "modes",
             "cas_latency_cl", "ras_to_cas_delay_trcd",
             "row_precharge_delay_trp", "has_radiator",
             "illumination", "height", "radiator_color",
             "low_profile", "power_voltage", "description",
             "price", "rating", "rates"]
    if not request.json:
        return flask.jsonify({'error': 'Empty request'})
    elif 'id' not in request.json or not all(key in keyss for key in request.json):
        return flask.jsonify({'error': 'Bad request'})
    elif not db_sess.query(RAM_DIMM).filter(RAM_DIMM.id == request.json['id']).first():
        return flask.jsonify({'error': 'Id does not exist'})
    rd = RAM_DIMM(
        id=request.json['id'],
        warranty=request.json.get("warranty"),
        country=request.json.get("country"),
        title=request.json.get("title"),
        year=request.json.get("year"),
        common_type=request.json.get("common_type"),
        type_ddr=request.json.get("type_ddr"),
        one_module_memory=request.json.get("one_module_memory"),
        all_memory=request.json.get("all_memory"),
        modules_amount=request.json.get("modules_amount"),
        ecc_memory=request.json.get("ecc_memory"),
        rang=request.json.get("rang"),
        register_memory=request.json.get("register_memory"),
        freq=request.json.get("freq"),
        intel_xpm_profiles=request.json.get("intel_xpm_profiles"),
        modes=request.json.get("modes"),
        cas_latency_cl=request.json.get("cas_latency_cl"),
        ras_to_cas_delay_trcd=request.json.get("ras_to_cas_delay_trcd"),
        row_precharge_delay_trp=request.json.get("row_precharge_delay_trp"),
        has_radiator=request.json.get("has_radiator"),
        illumination=request.json.get("illumination"),
        height=request.json.get("height"),
        radiator_color=request.json.get("radiator_color"),
        low_profile=request.json.get("low_profile"),
        power_voltage=request.json.get("power_voltage"),
        description=request.json.get("description"),
        price=request.json.get("price"),
        rating=request.json.get("rating"),
        rates=request.json.get("rates")
    )
    if rd.warranty:
        db_sess.query(RAM_DIMM).filter(RAM_DIMM.id == rd.id).update(values={RAM_DIMM.warranty: rd.warranty})
    if rd.country:
        db_sess.query(RAM_DIMM).filter(RAM_DIMM.id == rd.id).update(values={RAM_DIMM.country: rd.country})
    if rd.title:
        db_sess.query(RAM_DIMM).filter(RAM_DIMM.id == rd.id).update(values={RAM_DIMM.title: rd.title})
    if rd.year:
        db_sess.query(RAM_DIMM).filter(RAM_DIMM.id == rd.id).update(values={RAM_DIMM.year: rd.year})
    if rd.common_type:
        db_sess.query(RAM_DIMM).filter(RAM_DIMM.id == rd.id).update(values={RAM_DIMM.common_type: rd.common_type})
    if rd.type_ddr:
        db_sess.query(RAM_DIMM).filter(RAM_DIMM.id == rd.id).update(values={RAM_DIMM.type_ddr: rd.type_ddr})
    if rd.one_module_memory:
        db_sess.query(RAM_DIMM).filter(RAM_DIMM.id == rd.id).update(
            values={RAM_DIMM.one_module_memory: rd.one_module_memory})
    if rd.all_memory:
        db_sess.query(RAM_DIMM).filter(RAM_DIMM.id == rd.id).update(values={RAM_DIMM.all_memory: rd.all_memory})
    if rd.modules_amount:
        db_sess.query(RAM_DIMM).filter(RAM_DIMM.id == rd.id).update(values={RAM_DIMM.modules_amount: rd.modules_amount})
    if rd.ecc_memory:
        db_sess.query(RAM_DIMM).filter(RAM_DIMM.id == rd.id).update(values={RAM_DIMM.ecc_memory: rd.ecc_memory})
    if rd.rang:
        db_sess.query(RAM_DIMM).filter(RAM_DIMM.id == rd.id).update(values={RAM_DIMM.rang: rd.rang})
    if rd.register_memory:
        db_sess.query(RAM_DIMM).filter(RAM_DIMM.id == rd.id).update(
            values={RAM_DIMM.register_memory: rd.register_memory})
    if rd.freq:
        db_sess.query(RAM_DIMM).filter(RAM_DIMM.id == rd.id).update(values={RAM_DIMM.freq: rd.freq})
    if rd.intel_xpm_profiles:
        db_sess.query(RAM_DIMM).filter(RAM_DIMM.id == rd.id).update(
            values={RAM_DIMM.intel_xpm_profiles: rd.intel_xpm_profiles})
    if rd.modes:
        db_sess.query(RAM_DIMM).filter(RAM_DIMM.id == rd.id).update(values={RAM_DIMM.modes: rd.modes})
    if rd.cas_latency_cl:
        db_sess.query(RAM_DIMM).filter(RAM_DIMM.id == rd.id).update(values={RAM_DIMM.cas_latency_cl: rd.cas_latency_cl})
    if rd.ras_to_cas_delay_trcd:
        db_sess.query(RAM_DIMM).filter(RAM_DIMM.id == rd.id).update(
            values={RAM_DIMM.ras_to_cas_delay_trcd: rd.ras_to_cas_delay_trcd})
    if rd.row_precharge_delay_trp:
        db_sess.query(RAM_DIMM).filter(RAM_DIMM.id == rd.id).update(
            values={RAM_DIMM.row_precharge_delay_trp: rd.row_precharge_delay_trp})
    if rd.has_radiator:
        db_sess.query(RAM_DIMM).filter(RAM_DIMM.id == rd.id).update(values={RAM_DIMM.has_radiator: rd.has_radiator})
    if rd.illumination:
        db_sess.query(RAM_DIMM).filter(RAM_DIMM.id == rd.id).update(values={RAM_DIMM.illumination: rd.illumination})
    if rd.height:
        db_sess.query(RAM_DIMM).filter(RAM_DIMM.id == rd.id).update(values={RAM_DIMM.height: rd.height})
    if rd.radiator_color:
        db_sess.query(RAM_DIMM).filter(RAM_DIMM.id == rd.id).update(values={RAM_DIMM.radiator_color: rd.radiator_color})
    if rd.low_profile:
        db_sess.query(RAM_DIMM).filter(RAM_DIMM.id == rd.id).update(values={RAM_DIMM.low_profile: rd.low_profile})
    if rd.power_voltage:
        db_sess.query(RAM_DIMM).filter(RAM_DIMM.id == rd.id).update(values={RAM_DIMM.power_voltage: rd.power_voltage})
    if rd.description:
        db_sess.query(RAM_DIMM).filter(RAM_DIMM.id == rd.id).update(values={RAM_DIMM.description: rd.description})
    if rd.price:
        db_sess.query(RAM_DIMM).filter(RAM_DIMM.id == rd.id).update(values={RAM_DIMM.price: rd.price})
    if rd.rating:
        db_sess.query(RAM_DIMM).filter(RAM_DIMM.id == rd.id).update(values={RAM_DIMM.rating: rd.rating})
    if rd.rates:
        db_sess.query(RAM_DIMM).filter(RAM_DIMM.id == rd.id).update(values={RAM_DIMM.rates: rd.rates})
    db_sess.commit()
    return flask.jsonify({'success': 'OK'})