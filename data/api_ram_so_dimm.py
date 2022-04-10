import flask
from data.__all_models import *
from flask import request
from data import db_session


blueprint = flask.Blueprint('ram_so_dimm_api', __name__, template_folder='templates')


@blueprint.route('/api/ram_so_dimm', methods=['GET'])
def get_ram_so_dimms():
    db_sess = db_session.create_session()
    rsd = db_sess.query(RAM_SO_DIMM).all()
    return flask.jsonify({'ram_dimm': [item.to_dict(
        only=("id", "warranty", "country",
              "title", "common_type",
              "type_ddr", "one_module_memory",
              "all_memory", "modules_amount",
              "freq", "ras_to_cas_delay_trcd",
              "row_precharge_delay_trp",
              "cas_latency_cl", "chips_amount",
              "double_sided_chips_setup",
              "power_voltage", "description",
              "price", "rating", "rates"))
        for item in rsd]})


@blueprint.route('/api/ram_so_dimm_add', methods=['POST'])
def add_so_ram_dimm():
    db_sess = db_session.create_session()
    if not request.json:
        return flask.jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ["id", "warranty", "country",
                  "title", "common_type",
                  "type_ddr", "one_module_memory",
                  "all_memory", "modules_amount",
                  "freq", "ras_to_cas_delay_trcd",
                  "row_precharge_delay_trp",
                  "cas_latency_cl", "chips_amount",
                  "double_sided_chips_setup",
                  "power_voltage", "description",
                  "price", "rating", "rates"]):
        return flask.jsonify({'error': 'Bad request'})
    elif db_sess.query(RAM_SO_DIMM).filter(RAM_SO_DIMM.id == request.json['id']).first():
        return flask.jsonify({'error': 'Id already exists'})
    rsd = RAM_SO_DIMM(
        id=request.json['id'],
        warranty=request.json.get("warranty"),
        country=request.json.get("country"),
        title=request.json.get("title"),
        common_type=request.json.get("common_type"),
        type_ddr=request.json.get("type_ddr"),
        one_module_memory=request.json.get("one_module_memory"),
        all_memory=request.json.get("all_memory"),
        modules_amount=request.json.get("modules_amount"),
        freq=request.json.get("freq"),
        ras_to_cas_delay_trcd=request.json.get("ras_to_cas_delay_trcd"),
        row_precharge_delay_trp=request.json.get("row_precharge_delay_trp"),
        cas_latency_cl=request.json.get("cas_latency_cl"),
        chips_amount=request.json.get("chips_amount"),
        double_sided_chips_setup=request.json.get("double_sided_chips_setup"),
        power_voltage=request.json.get("power_voltage"),
        description=request.json.get("description"),
        price=request.json.get("price"),
        rating=request.json.get("rating"),
        rates=request.json.get("rates")
    )
    db_sess.add(rsd)
    db_sess.commit()
    return flask.jsonify({'success': 'OK'})


@blueprint.route('/api/ram_so_dimm_get/<int:_id>', methods=['GET'])
def get_ram_so_dimm(_id):
    db_sess = db_session.create_session()
    rsd = db_sess.query(RAM_SO_DIMM).filter(RAM_SO_DIMM.id == _id).first()
    if not rsd:
        return flask.jsonify({'error': 'Not found'})
    return flask.jsonify(
        {
            'ram_so_dimm': rsd.to_dict(only=(
                "id", "warranty", "country",
                "title", "common_type",
                "type_ddr", "one_module_memory",
                "all_memory", "modules_amount",
                "freq", "ras_to_cas_delay_trcd",
                "row_precharge_delay_trp",
                "cas_latency_cl", "chips_amount",
                "double_sided_chips_setup",
                "power_voltage", "description",
                "price", "rating", "rates")
            )
        }
    )


@blueprint.route('/api/ram_so_dimm_delete/<int:_id>', methods=['DELETE'])
def delete_ram_so_dimm(_id):
    db_sess = db_session.create_session()
    rsd = db_sess.query(RAM_SO_DIMM).get(_id)
    if not rsd:
        return flask.jsonify({'error': 'Not found'})
    db_sess.delete(rsd)
    db_sess.commit()
    return flask.jsonify({'success': 'OK'})


@blueprint.route('/api/ram_so_dimm_edit/', methods=['PUT'])
def edit_ram_so_dimm():
    db_sess = db_session.create_session()
    keyss = ["id", "warranty", "country",
             "title", "common_type",
             "type_ddr", "one_module_memory",
             "all_memory", "modules_amount",
             "freq", "ras_to_cas_delay_trcd",
             "row_precharge_delay_trp",
             "cas_latency_cl", "chips_amount",
             "double_sided_chips_setup",
             "power_voltage", "description",
             "price", "rating", "rates"]
    if not request.json:
        return flask.jsonify({'error': 'Empty request'})
    elif 'id' not in request.json or not all(key in keyss for key in request.json):
        return flask.jsonify({'error': 'Bad request'})
    elif not db_sess.query(RAM_SO_DIMM).filter(RAM_SO_DIMM.id == request.json['id']).first():
        return flask.jsonify({'error': 'Id does not exist'})
    rsd = RAM_SO_DIMM(
        id=request.json['id'],
        warranty=request.json.get("warranty"),
        country=request.json.get("country"),
        title=request.json.get("title"),
        common_type=request.json.get("common_type"),
        type_ddr=request.json.get("type_ddr"),
        one_module_memory=request.json.get("one_module_memory"),
        all_memory=request.json.get("all_memory"),
        modules_amount=request.json.get("modules_amount"),
        freq=request.json.get("freq"),
        ras_to_cas_delay_trcd=request.json.get("ras_to_cas_delay_trcd"),
        row_precharge_delay_trp=request.json.get("row_precharge_delay_trp"),
        cas_latency_cl=request.json.get("cas_latency_cl"),
        chips_amount=request.json.get("chips_amount"),
        double_sided_chips_setup=request.json.get("double_sided_chips_setup"),
        power_voltage=request.json.get("power_voltage"),
        description=request.json.get("description"),
        price=request.json.get("price"),
        rating=request.json.get("rating"),
        rates=request.json.get("rates")
    )
    if rsd.warranty:
        db_sess.query(RAM_SO_DIMM).filter(RAM_SO_DIMM.id == rsd.id).update(values={RAM_SO_DIMM.warranty: rsd.warranty})
    if rsd.country:
        db_sess.query(RAM_SO_DIMM).filter(RAM_SO_DIMM.id == rsd.id).update(values={RAM_SO_DIMM.country: rsd.country})
    if rsd.title:
        db_sess.query(RAM_SO_DIMM).filter(RAM_SO_DIMM.id == rsd.id).update(values={RAM_SO_DIMM.title: rsd.title})
    if rsd.common_type:
        db_sess.query(RAM_SO_DIMM).filter(RAM_SO_DIMM.id == rsd.id).update(
            values={RAM_SO_DIMM.common_type: rsd.common_type})
    if rsd.type_ddr:
        db_sess.query(RAM_SO_DIMM).filter(RAM_SO_DIMM.id == rsd.id).update(values={RAM_SO_DIMM.type_ddr: rsd.type_ddr})
    if rsd.one_module_memory:
        db_sess.query(RAM_SO_DIMM).filter(RAM_SO_DIMM.id == rsd.id).update(
            values={RAM_SO_DIMM.one_module_memory: rsd.one_module_memory})
    if rsd.all_memory:
        db_sess.query(RAM_SO_DIMM).filter(RAM_SO_DIMM.id == rsd.id).update(
            values={RAM_SO_DIMM.all_memory: rsd.all_memory})
    if rsd.modules_amount:
        db_sess.query(RAM_SO_DIMM).filter(RAM_SO_DIMM.id == rsd.id).update(
            values={RAM_SO_DIMM.modules_amount: rsd.modules_amount})
    if rsd.freq:
        db_sess.query(RAM_SO_DIMM).filter(RAM_SO_DIMM.id == rsd.id).update(values={RAM_SO_DIMM.freq: rsd.freq})
    if rsd.ras_to_cas_delay_trcd:
        db_sess.query(RAM_SO_DIMM).filter(RAM_SO_DIMM.id == rsd.id).update(
            values={RAM_SO_DIMM.ras_to_cas_delay_trcd: rsd.ras_to_cas_delay_trcd})
    if rsd.row_precharge_delay_trp:
        db_sess.query(RAM_SO_DIMM).filter(RAM_SO_DIMM.id == rsd.id).update(
            values={RAM_SO_DIMM.row_precharge_delay_trp: rsd.row_precharge_delay_trp})
    if rsd.cas_latency_cl:
        db_sess.query(RAM_SO_DIMM).filter(RAM_SO_DIMM.id == rsd.id).update(
            values={RAM_SO_DIMM.cas_latency_cl: rsd.cas_latency_cl})
    if rsd.chips_amount:
        db_sess.query(RAM_SO_DIMM).filter(RAM_SO_DIMM.id == rsd.id).update(
            values={RAM_SO_DIMM.chips_amount: rsd.chips_amount})
    if rsd.double_sided_chips_setup:
        db_sess.query(RAM_SO_DIMM).filter(RAM_SO_DIMM.id == rsd.id).update(
            values={RAM_SO_DIMM.double_sided_chips_setup: rsd.double_sided_chips_setup})
    if rsd.power_voltage:
        db_sess.query(RAM_SO_DIMM).filter(RAM_SO_DIMM.id == rsd.id).update(
            values={RAM_SO_DIMM.power_voltage: rsd.power_voltage})
    if rsd.description:
        db_sess.query(RAM_SO_DIMM).filter(RAM_SO_DIMM.id == rsd.id).update(
            values={RAM_SO_DIMM.description: rsd.description})
    if rsd.price:
        db_sess.query(RAM_SO_DIMM).filter(RAM_SO_DIMM.id == rsd.id).update(values={RAM_SO_DIMM.price: rsd.price})
    if rsd.rating:
        db_sess.query(RAM_SO_DIMM).filter(RAM_SO_DIMM.id == rsd.id).update(values={RAM_SO_DIMM.rating: rsd.rating})
    if rsd.rates:
        db_sess.query(RAM_SO_DIMM).filter(RAM_SO_DIMM.id == rsd.id).update(values={RAM_SO_DIMM.rates: rsd.rates})
    db_sess.commit()
    return flask.jsonify({'success': 'OK'})
