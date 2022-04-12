import flask
from data.__all_models import *
from flask import request
from data import db_session


blueprint = flask.Blueprint('ssd_api', __name__, template_folder='templates')


@blueprint.route('/api/ssd', methods=['GET'])
def get_ssds():
    db_sess = db_session.create_session()
    ssd = db_sess.query(SSD).all()
    return flask.jsonify({'ssd': [item.to_dict(
        only=('id', "warranty", "title", "year",
              "ssd_type", "memory",
              "phys_interface",
              "bit_per_cell_amount",
              "memory_structure", "DRAM_buffer",
              "max_cons_reading_speed",
              "max_cons_writing_speed",
              "max_writing_resource_TBW", "DWPD",
              "hardware_data_encryption", "width",
              "form_factor", "description", "price",
              "rating", "rates"))
        for item in ssd]})


@blueprint.route('/api/ssd_add', methods=['POST'])
def add_ssd():
    db_sess = db_session.create_session()
    if not request.json:
        return flask.jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['id', "warranty", "title", "year",
                  "ssd_type", "memory",
                  "phys_interface",
                  "bit_per_cell_amount",
                  "memory_structure", "DRAM_buffer",
                  "max_cons_reading_speed",
                  "max_cons_writing_speed",
                  "max_writing_resource_TBW", "DWPD",
                  "hardware_data_encryption", "width",
                  "form_factor", "description", "price",
                  "rating", "rates"]):
        return flask.jsonify({'error': 'Bad request'})
    elif db_sess.query(SSD).filter(SSD.id == request.json['id']).first():
        return flask.jsonify({'error': 'Id already exists'})
    ssd = SSD(
        id=request.json['id'],
        warranty=request.json.get("warranty"),
        title=request.json.get("title"),
        year=request.json.get("year"),
        ssd_type=request.json.get("ssd_type"),
        memory=request.json.get("memory"),
        phys_interface=request.json.get("phys_interface"),
        bit_per_cell_amount=request.json.get("bit_per_cell_amount"),
        memory_structure=request.json.get("memory_structure"),
        DRAM_buffer=request.json.get("DRAM_buffer"),
        max_cons_reading_speed=request.json.get("max_cons_reading_speed"),
        max_cons_writing_speed=request.json.get("max_cons_writing_speed"),
        max_writing_resource_TBW=request.json.get("max_writing_resource_TBW"),
        DWPD=request.json.get("DWPD"),
        hardware_data_encryption=request.json.get("hardware_data_encryption"),
        width=request.json.get("width"),
        form_factor=request.json.get("form_factor"),
        description=request.json.get("description"),
        price=request.json.get("price"),
        rating=request.json.get("rating"),
        rates=request.json.get("rates")
    )
    db_sess.add(ssd)
    db_sess.commit()
    return flask.jsonify({'success': 'OK'})


@blueprint.route('/api/ssd_get/<int:_id>', methods=['GET'])
def get_ssd(_id):
    db_sess = db_session.create_session()
    ssd = db_sess.query(SSD).filter(SSD.id == _id).first()
    if not ssd:
        return flask.jsonify({'error': 'Not found'})
    return flask.jsonify(
        {
            'ssd': ssd.to_dict(only=(
                'id', "warranty", "title", "year",
                "ssd_type", "memory",
                "phys_interface",
                "bit_per_cell_amount",
                "memory_structure", "DRAM_buffer",
                "max_cons_reading_speed",
                "max_cons_writing_speed",
                "max_writing_resource_TBW", "DWPD",
                "hardware_data_encryption", "width",
                "form_factor", "description", "price",
                "rating", "rates")
            )
        }
    )


@blueprint.route('/api/ssd_delete/<int:_id>', methods=['DELETE'])
def delete_ssd(_id):
    db_sess = db_session.create_session()
    ssd = db_sess.query(SSD).get(_id)
    if not ssd:
        return flask.jsonify({'error': 'Not found'})
    db_sess.delete(ssd)
    db_sess.commit()
    return flask.jsonify({'success': 'OK'})


@blueprint.route('/api/ssd_edit/', methods=['PUT'])
def edit_ssd():
    db_sess = db_session.create_session()
    keyss = ['id', "warranty", "title", "year",
             "ssd_type", "memory",
             "phys_interface",
             "bit_per_cell_amount",
             "memory_structure", "DRAM_buffer",
             "max_cons_reading_speed",
             "max_cons_writing_speed",
             "max_writing_resource_TBW", "DWPD",
             "hardware_data_encryption", "width",
             "form_factor", "description", "price",
             "rating", "rates"]
    if not request.json:
        return flask.jsonify({'error': 'Empty request'})
    elif 'id' not in request.json or not all(key in keyss for key in request.json):
        return flask.jsonify({'error': 'Bad request'})
    elif not db_sess.query(SSD).filter(SSD.id == request.json['id']).first():
        return flask.jsonify({'error': 'Id does not exist'})
    ssd = SSD(
        id=request.json['id'],
        warranty=request.json.get("warranty"),
        title=request.json.get("title"),
        year=request.json.get("year"),
        ssd_type=request.json.get("ssd_type"),
        memory=request.json.get("memory"),
        phys_interface=request.json.get("phys_interface"),
        bit_per_cell_amount=request.json.get("bit_per_cell_amount"),
        memory_structure=request.json.get("memory_structure"),
        DRAM_buffer=request.json.get("DRAM_buffer"),
        max_cons_reading_speed=request.json.get("max_cons_reading_speed"),
        max_cons_writing_speed=request.json.get("max_cons_writing_speed"),
        max_writing_resource_TBW=request.json.get("max_writing_resource_TBW"),
        DWPD=request.json.get("DWPD"),
        hardware_data_encryption=request.json.get("hardware_data_encryption"),
        width=request.json.get("width"),
        form_factor=request.json.get("form_factor"),
        description=request.json.get("description"),
        price=request.json.get("price"),
        rating=request.json.get("rating"),
        rates=request.json.get("rates")
    )
    if ssd.warranty:
        db_sess.query(SSD).filter(SSD.id == ssd.id).update(values={SSD.warranty: ssd.warranty})
    if ssd.title:
        db_sess.query(SSD).filter(SSD.id == ssd.id).update(values={SSD.title: ssd.title})
    if ssd.year:
        db_sess.query(SSD).filter(SSD.id == ssd.id).update(values={SSD.year: ssd.year})
    if ssd.ssd_type:
        db_sess.query(SSD).filter(SSD.id == ssd.id).update(values={SSD.ssd_type: ssd.ssd_type})
    if ssd.memory:
        db_sess.query(SSD).filter(SSD.id == ssd.id).update(values={SSD.memory: ssd.memory})
    if ssd.phys_interface:
        db_sess.query(SSD).filter(SSD.id == ssd.id).update(values={SSD.phys_interface: ssd.phys_interface})
    if ssd.bit_per_cell_amount:
        db_sess.query(SSD).filter(SSD.id == ssd.id).update(values={SSD.bit_per_cell_amount: ssd.bit_per_cell_amount})
    if ssd.memory_structure:
        db_sess.query(SSD).filter(SSD.id == ssd.id).update(values={SSD.memory_structure: ssd.memory_structure})
    if ssd.DRAM_buffer:
        db_sess.query(SSD).filter(SSD.id == ssd.id).update(values={SSD.DRAM_buffer: ssd.DRAM_buffer})
    if ssd.max_cons_reading_speed:
        db_sess.query(SSD).filter(SSD.id == ssd.id).update(
            values={SSD.max_cons_reading_speed: ssd.max_cons_reading_speed})
    if ssd.max_cons_writing_speed:
        db_sess.query(SSD).filter(SSD.id == ssd.id).update(
            values={SSD.max_cons_writing_speed: ssd.max_cons_writing_speed})
    if ssd.max_writing_resource_TBW:
        db_sess.query(SSD).filter(SSD.id == ssd.id).update(
            values={SSD.max_writing_resource_TBW: ssd.max_writing_resource_TBW})
    if ssd.DWPD:
        db_sess.query(SSD).filter(SSD.id == ssd.id).update(values={SSD.DWPD: ssd.DWPD})
    if ssd.hardware_data_encryption:
        db_sess.query(SSD).filter(SSD.id == ssd.id).update(
            values={SSD.hardware_data_encryption: ssd.hardware_data_encryption})
    if ssd.width:
        db_sess.query(SSD).filter(SSD.id == ssd.id).update(values={SSD.width: ssd.width})
    if ssd.form_factor:
        db_sess.query(SSD).filter(SSD.id == ssd.id).update(values={SSD.form_factor: ssd.form_factor})
    if ssd.description:
        db_sess.query(SSD).filter(SSD.id == ssd.id).update(values={SSD.description: ssd.description})
    if ssd.price:
        db_sess.query(SSD).filter(SSD.id == ssd.id).update(values={SSD.price: ssd.price})
    if ssd.rating:
        db_sess.query(SSD).filter(SSD.id == ssd.id).update(values={SSD.rating: ssd.rating})
    if ssd.rates:
        db_sess.query(SSD).filter(SSD.id == ssd.id).update(values={SSD.rates: ssd.rates})
    db_sess.commit()
    return flask.jsonify({'success': 'OK'})