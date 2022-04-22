import flask
from data.__all_models import *
from flask import request
from data import db_session


blueprint = flask.Blueprint('hdd35_api', __name__, template_folder='templates')


@blueprint.route('/api/hdd35', methods=['GET'])
def get_gpus():
    db_sess = db_session.create_session()
    hdd35 = db_sess.query(HDD35).all()
    return flask.jsonify({'hdd35': [item.to_dict(
        only=("id", "warranty", "country", "title",
              "year", "memory_bits", "rotation_speed",
              "cash_memory_bits", "raid_massives_optimization",
              "helium_fill", "noise_dba", "writing_tech_CMR_SMR",
              "position_park_cycles_amount", "width",
              "length", "height", "description", "price",
              "rating", "rates"))
        for item in hdd35]})


@blueprint.route('/api/hdd35_add', methods=['POST'])
def add_hdd35():
    db_sess = db_session.create_session()
    if not request.json:
        return flask.jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ["id", "warranty", "country", "title",
                  "year", "memory_bits", "rotation_speed",
                  "cash_memory_bits", "raid_massives_optimization",
                  "helium_fill", "noise_dba", "writing_tech_CMR_SMR",
                  "position_park_cycles_amount", "width",
                  "length", "height", "description", "price",
                  "rating", "rates"]):
        return flask.jsonify({'error': 'Bad request'})
    elif db_sess.query(HDD35).filter(HDD35.id == request.json['id']).first():
        return flask.jsonify({'error': 'Id already exists'})
    hdd35 = HDD35(
        id=request.json['id'],
        warranty=request.json.get("warranty"),
        country=request.json.get("country"),
        title=request.json.get("title"),
        year=request.json.get("year"),
        memory_bits=request.json.get("memory_bits"),
        rotation_speed=request.json.get("rotation_speed"),
        cash_memory_bits=request.json.get("cash_memory_bits"),
        raid_massives_optimization=request.json.get("raid_massives_optimization"),
        helium_fill=request.json.get("helium_fill"),
        noise_dba=request.json.get("noise_dba"),
        writing_tech_CMR_SMR=request.json.get("writing_tech_CMR_SMR"),
        position_park_cycles_amount=request.json.get("position_park_cycles_amount"),
        width=request.json.get("width"),
        length=request.json.get("length"),
        height=request.json.get("height"),
        description=request.json.get("description"),
        price=request.json.get("price"),
        rating=request.json.get("rating"),
        rates=request.json.get("rates")
    )
    db_sess.add(hdd35)
    db_sess.commit()
    return flask.jsonify({'success': 'OK'})


@blueprint.route('/api/hdd35_get/<int:_id>', methods=['GET'])
def get_hdd35(_id):
    db_sess = db_session.create_session()
    hdd35 = db_sess.query(HDD35).filter(HDD35.id == _id).first()
    if not hdd35:
        return flask.jsonify({'error': 'Not found'})
    return flask.jsonify(
        {
            'hdd35': hdd35.to_dict(only=(
                "id", "warranty", "country", "title",
                "year", "memory_bits", "rotation_speed",
                "cash_memory_bits", "raid_massives_optimization",
                "helium_fill", "noise_dba", "writing_tech_CMR_SMR",
                "position_park_cycles_amount", "width",
                "length", "height", "description", "price",
                "rating", "rates")
            )
        }
    )


@blueprint.route('/api/hdd35_delete/<int:_id>', methods=['DELETE'])
def delete_hdd35(_id):
    db_sess = db_session.create_session()
    hdd35 = db_sess.query(HDD35).get(_id)
    if not hdd35:
        return flask.jsonify({'error': 'Not found'})
    db_sess.delete(hdd35)
    db_sess.commit()
    return flask.jsonify({'success': 'OK'})


@blueprint.route('/api/hdd35_edit/', methods=['PUT'])
def edit_hdd35():
    db_sess = db_session.create_session()
    keyss = ["id", "warranty", "country", "title",
             "year", "memory_bits", "rotation_speed",
             "cash_memory_bits", "raid_massives_optimization",
             "helium_fill", "noise_dba", "writing_tech_CMR_SMR",
             "position_park_cycles_amount", "width",
             "length", "height", "description", "price",
             "rating", "rates"]
    if not request.json:
        return flask.jsonify({'error': 'Empty request'})
    elif 'id' not in request.json or not all(key in keyss for key in request.json):
        return flask.jsonify({'error': 'Bad request'})
    elif not db_sess.query(HDD35).filter(HDD35.id == request.json['id']).first():
        return flask.jsonify({'error': 'Id does not exist'})
    hdd35 = HDD35(
        id=request.json['id'],
        warranty=request.json.get("warranty"),
        country=request.json.get("country"),
        title=request.json.get("title"),
        year=request.json.get("year"),
        memory_bits=request.json.get("memory_bits"),
        rotation_speed=request.json.get("rotation_speed"),
        cash_memory_bits=request.json.get("cash_memory_bits"),
        raid_massives_optimization=request.json.get("raid_massives_optimization"),
        helium_fill=request.json.get("helium_fill"),
        noise_dba=request.json.get("noise_dba"),
        writing_tech_CMR_SMR=request.json.get("writing_tech_CMR_SMR"),
        position_park_cycles_amount=request.json.get("position_park_cycles_amount"),
        width=request.json.get("width"),
        length=request.json.get("length"),
        height=request.json.get("height"),
        description=request.json.get("description"),
        price=request.json.get("price"),
        rating=request.json.get("rating"),
        rates=request.json.get("rates")
    )
    if hdd35.warranty:
        db_sess.query(HDD35).filter(HDD35.id == hdd35.id).update(values={HDD35.warranty: hdd35.warranty})
    if hdd35.country:
        db_sess.query(HDD35).filter(HDD35.id == hdd35.id).update(values={HDD35.country: hdd35.country})
    if hdd35.title:
        db_sess.query(HDD35).filter(HDD35.id == hdd35.id).update(values={HDD35.title: hdd35.title})
    if hdd35.year:
        db_sess.query(HDD35).filter(HDD35.id == hdd35.id).update(values={HDD35.year: hdd35.year})
    if hdd35.memory_bits:
        db_sess.query(HDD35).filter(HDD35.id == hdd35.id).update(values={HDD35.memory_bits: hdd35.memory_bits})
    if hdd35.rotation_speed:
        db_sess.query(HDD35).filter(HDD35.id == hdd35.id).update(values={HDD35.rotation_speed: hdd35.rotation_speed})
    if hdd35.cash_memory_bits:
        db_sess.query(HDD35).filter(HDD35.id == hdd35.id).update(
            values={HDD35.cash_memory_bits: hdd35.cash_memory_bits})
    if hdd35.raid_massives_optimization:
        db_sess.query(HDD35).filter(HDD35.id == hdd35.id).update(
            values={HDD35.raid_massives_optimization: hdd35.raid_massives_optimization})
    if hdd35.helium_fill:
        db_sess.query(HDD35).filter(HDD35.id == hdd35.id).update(values={HDD35.helium_fill: hdd35.helium_fill})
    if hdd35.noise_dba:
        db_sess.query(HDD35).filter(HDD35.id == hdd35.id).update(values={HDD35.noise_dba: hdd35.noise_dba})
    if hdd35.writing_tech_CMR_SMR:
        db_sess.query(HDD35).filter(HDD35.id == hdd35.id).update(
            values={HDD35.writing_tech_CMR_SMR: hdd35.writing_tech_CMR_SMR})
    if hdd35.position_park_cycles_amount:
        db_sess.query(HDD35).filter(HDD35.id == hdd35.id).update(
            values={HDD35.position_park_cycles_amount: hdd35.position_park_cycles_amount})
    if hdd35.width:
        db_sess.query(HDD35).filter(HDD35.id == hdd35.id).update(values={HDD35.width: hdd35.width})
    if hdd35.length:
        db_sess.query(HDD35).filter(HDD35.id == hdd35.id).update(values={HDD35.length: hdd35.length})
    if hdd35.height:
        db_sess.query(HDD35).filter(HDD35.id == hdd35.id).update(values={HDD35.height: hdd35.height})
    if hdd35.description:
        db_sess.query(HDD35).filter(HDD35.id == hdd35.id).update(values={HDD35.description: hdd35.description})
    if hdd35.price:
        db_sess.query(HDD35).filter(HDD35.id == hdd35.id).update(values={HDD35.price: hdd35.price})
    if hdd35.rating:
        db_sess.query(HDD35).filter(HDD35.id == hdd35.id).update(values={HDD35.rating: hdd35.rating})
    if hdd35.rates:
        db_sess.query(HDD35).filter(HDD35.id == hdd35.id).update(values={HDD35.rates: hdd35.rates})
    db_sess.commit()
    return flask.jsonify({'success': 'OK'})
