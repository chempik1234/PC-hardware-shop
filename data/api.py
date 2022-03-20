import flask
from data.__all_models import *
from flask import request
from data import db_session


blueprint = flask.Blueprint('cpu_api', __name__, template_folder='templates')


# cpu


@blueprint.route('/api/cpu', methods=['GET'])
def get_jobs():
    db_sess = db_session.create_session()
    cpu = db_sess.query(CPU).all()
    return flask.jsonify({'cpu': [item.to_dict(
        only=('id', 'warranty', 'country', 'title',
              'generation', 'year', 'socket',
              'has_cooling', 'term_interface',
              'cores', 'threads', 'tech_process',
              'core', 'cash_l1_instructions_bits',
              'cash_l1_data_bits',
              'cash_l2_bits', 'cash_l3_bits',
              'base_freq', 'max_freq', 'free_mult',
              'memory', 'max_mem_bits', 'channels',
              'min_RAM_freq', 'max_RAM_freq', 'ECC',
              'TDP', 'custom_TDP', 'max_temp',
              'has_graphics', 'PCI', 'PCI_amount',
              'bandwidth', 'support_x64', 'multi_thread',
              'add_freq_tech', 'energy_save_tech',
              'description', 'price', 'rating', 'rates'))
        for item in cpu]})


@blueprint.route('/api/cpu_add', methods=['POST'])
def add_cpu():
    db_sess = db_session.create_session()
    if not request.json:
        return flask.jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['id', 'warranty', 'country', 'title',
                  'generation', 'year', 'socket',
                  'has_cooling', 'term_interface',
                  'cores', 'threads', 'tech_process',
                  'core', 'cash_l1_instructions_bits',
                  'cash_l1_data_bits',
                  'cash_l2_bits', 'cash_l3_bits',
                  'base_freq', 'max_freq', 'free_mult',
                  'memory', 'max_mem_bits', 'channels',
                  'min_RAM_freq', 'max_RAM_freq', 'ECC',
                  'TDP', 'custom_TDP', 'max_temp',
                  'has_graphics', 'PCI', 'PCI_amount',
                  'bandwidth', 'support_x64', 'multi_thread',
                  'add_freq_tech', 'energy_save_tech',
                  'description', 'price', 'rating', 'rates']):
        return flask.jsonify({'error': 'Bad request'})
    elif db_sess.query(CPU).filter(CPU.id == request.json['id']).first():
        return flask.jsonify({'error': 'Id already exists'})
    cpu = CPU(
        id=request.json['id'],
        warranty=request.json.get("warranty"),
        country=request.json.get("country"),
        title=request.json.get("title"),
        generation=request.json.get("generation"),
        year=request.json.get("year"),
        socket=request.json.get("socket"),
        has_cooling=request.json.get("has_cooling"),
        term_interface=request.json.get("term_interface"),
        cores=request.json.get("cores"),
        threads=request.json.get("threads"),
        tech_process=request.json.get("tech_process"),
        core=request.json.get("core"),
        cash_l1_instructions_bits=request.json.get("cash_l1_instructions_bits"),
        cash_l1_data_bits=request.json.get("cash_l1_data_bits"),
        cash_l2_bits=request.json.get("cash_l2_bits"),
        cash_l3_bits=request.json.get("cash_l3_bits"),
        base_freq=request.json.get("base_freq"),
        max_freq=request.json.get("max_freq"),
        free_mult=request.json.get("free_mult"),
        memory=request.json.get("memory"),
        max_mem_bits=request.json.get("max_mem_bits"),
        channels=request.json.get("channels"),
        min_RAM_freq=request.json.get("min_RAM_freq"),
        max_RAM_freq=request.json.get("max_RAM_freq"),
        ECC=request.json.get("ECC"),
        TDP=request.json.get("TDP"),
        custom_TDP=request.json.get("custom_TDP"),
        max_temp=request.json.get("max_temp"),
        has_graphics=request.json.get("has_graphics"),
        PCI=request.json.get("PCI"),
        PCI_amount=request.json.get("PCI_amount"),
        bandwidth=request.json.get("bandwidth"),
        support_x64=request.json.get("support_x64"),
        multi_thread=request.json.get("multi_thread"),
        add_freq_tech=request.json.get("add_freq_tech"),
        energy_save_tech=request.json.get("energy_save_tech"),
        description=request.json.get("description"),
        price=request.json.get("price"),
        rating=request.json.get("rating"),
        rates=request.json.get('rates'),
    )
    db_sess.add(cpu)
    db_sess.commit()
    return flask.jsonify({'success': 'OK'})


@blueprint.route('/api/cpu_get/<int:cpu_id>', methods=['GET'])
def get_job(cpu_id):
    db_sess = db_session.create_session()
    cpu = db_sess.query(CPU).filter(CPU.id == cpu_id).first()
    if not cpu:
        return flask.jsonify({'error': 'Not found'})
    return flask.jsonify(
        {
            'cpu': cpu.to_dict(only=(
                'id', 'warranty', 'country', 'title',
                'generation', 'year', 'socket',
                'has_cooling', 'term_interface',
                'cores', 'threads', 'tech_process',
                'core', 'cash_l1_instructions_bits',
                'cash_l1_data_bits',
                'cash_l2_bits', 'cash_l3_bits',
                'base_freq', 'max_freq', 'free_mult',
                'memory', 'max_mem_bits', 'channels',
                'min_RAM_freq', 'max_RAM_freq', 'ECC',
                'TDP', 'custom_TDP', 'max_temp',
                'has_graphics', 'PCI', 'PCI_amount',
                'bandwidth', 'support_x64', 'multi_thread',
                'add_freq_tech', 'energy_save_tech',
                'description', 'price', 'rating', 'rates')
            )
        }
    )


@blueprint.route('/api/cpu_delete/<int:cpu_id>', methods=['DELETE'])
def delete_cpu(cpu_id):
    db_sess = db_session.create_session()
    cpu = db_sess.query(CPU).get(cpu_id)
    if not cpu:
        return flask.jsonify({'error': 'Not found'})
    db_sess.delete(cpu)
    db_sess.commit()
    return flask.jsonify({'success': 'OK'})


@blueprint.route('/api/cpu_edit/', methods=['PUT'])
def edit_cpu():
    db_sess = db_session.create_session()
    keyss = ['id', 'warranty', 'country', 'title',
             'generation', 'year', 'socket',
             'has_cooling', 'term_interface',
             'cores', 'threads', 'tech_process',
             'core', 'cash_l1_instructions_bits',
             'cash_l1_data_bits',
             'cash_l2_bits', 'cash_l3_bits',
             'base_freq', 'max_freq', 'free_mult',
             'memory', 'max_mem_bits', 'channels',
             'min_RAM_freq', 'max_RAM_freq', 'ECC',
             'TDP', 'custom_TDP', 'max_temp',
             'has_graphics', 'PCI', 'PCI_amount',
             'bandwidth', 'support_x64', 'multi_thread',
             'add_freq_tech', 'energy_save_tech',
             'description', 'price', 'rating', 'rates']
    if not request.json:
        return flask.jsonify({'error': 'Empty request'})
    elif 'id' not in request.json or not all(key in keyss for key in request.json):
        return flask.jsonify({'error': 'Bad request'})
    elif not db_sess.query(CPU).filter(CPU.id == request.json['id']).first():
        return flask.jsonify({'error': 'Id does not exist'})
    cpu = CPU(
        id=request.json['id'],
        warranty=request.json.get("warranty"),
        country=request.json.get("country"),
        title=request.json.get("title"),
        generation=request.json.get("generation"),
        year=request.json.get("year"),
        socket=request.json.get("socket"),
        has_cooling=request.json.get("has_cooling"),
        term_interface=request.json.get("term_interface"),
        cores=request.json.get("cores"),
        threads=request.json.get("threads"),
        tech_process=request.json.get("tech_process"),
        core=request.json.get("core"),
        cash_l1_instructions_bits=request.json.get("cash_l1_instructions_bits"),
        cash_l1_data_bits=request.json.get("cash_l1_data_bits"),
        cash_l2_bits=request.json.get("cash_l2_bits"),
        cash_l3_bits=request.json.get("cash_l3_bits"),
        base_freq=request.json.get("base_freq"),
        max_freq=request.json.get("max_freq"),
        free_mult=request.json.get("free_mult"),
        memory=request.json.get("memory"),
        max_mem_bits=request.json.get("max_mem_bits"),
        channels=request.json.get("channels"),
        min_RAM_freq=request.json.get("min_RAM_freq"),
        max_RAM_freq=request.json.get("max_RAM_freq"),
        ECC=request.json.get("ECC"),
        TDP=request.json.get("TDP"),
        custom_TDP=request.json.get("custom_TDP"),
        max_temp=request.json.get("max_temp"),
        has_graphics=request.json.get("has_graphics"),
        PCI=request.json.get("PCI"),
        PCI_amount=request.json.get("PCI_amount"),
        bandwidth=request.json.get("bandwidth"),
        support_x64=request.json.get("support_x64"),
        multi_thread=request.json.get("multi_thread"),
        add_freq_tech=request.json.get("add_freq_tech"),
        energy_save_tech=request.json.get("energy_save_tech"),
        description=request.json.get("description"),
        price=request.json.get("price"),
        rating=request.json.get("rating"),
        rates=request.json.get('rates'),
    )
    if cpu.warranty:
        db_sess.query(CPU).filter(CPU.id == cpu.id).update(values={CPU.warranty: cpu.warranty})
    if cpu.country:
        db_sess.query(CPU).filter(CPU.id == cpu.id).update(values={CPU.country: cpu.country})
    if cpu.title:
        db_sess.query(CPU).filter(CPU.id == cpu.id).update(values={CPU.title: cpu.title})
    if cpu.generation:
        db_sess.query(CPU).filter(CPU.id == cpu.id).update(values={CPU.generation: cpu.generation})
    if cpu.year:
        db_sess.query(CPU).filter(CPU.id == cpu.id).update(values={CPU.year: cpu.year})
    if cpu.socket:
        db_sess.query(CPU).filter(CPU.id == cpu.id).update(values={CPU.socket: cpu.socket})
    if cpu.has_cooling:
        db_sess.query(CPU).filter(CPU.id == cpu.id).update(values={CPU.has_cooling: cpu.has_cooling})
    if cpu.term_interface:
        db_sess.query(CPU).filter(CPU.id == cpu.id).update(values={CPU.term_interface: cpu.term_interface})
    if cpu.cores:
        db_sess.query(CPU).filter(CPU.id == cpu.id).update(values={CPU.cores: cpu.cores})
    if cpu.threads:
        db_sess.query(CPU).filter(CPU.id == cpu.id).update(values={CPU.threads: cpu.threads})
    if cpu.tech_process:
        db_sess.query(CPU).filter(CPU.id == cpu.id).update(values={CPU.tech_process: cpu.tech_process})
    if cpu.core:
        db_sess.query(CPU).filter(CPU.id == cpu.id).update(values={CPU.core: cpu.core})
    if cpu.cash_l1_instructions_bits:
        db_sess.query(CPU).filter(CPU.id == cpu.id).update(
            values={CPU.cash_l1_instructions_bits: cpu.cash_l1_instructions_bits})
    if cpu.cash_l1_data_bits:
        db_sess.query(CPU).filter(CPU.id == cpu.id).update(values={CPU.cash_l1_data_bits: cpu.cash_l1_data_bits})
    if cpu.cash_l2_bits:
        db_sess.query(CPU).filter(CPU.id == cpu.id).update(values={CPU.cash_l2_bits: cpu.cash_l2_bits})
    if cpu.cash_l3_bits:
        db_sess.query(CPU).filter(CPU.id == cpu.id).update(values={CPU.cash_l3_bits: cpu.cash_l3_bits})
    if cpu.base_freq:
        db_sess.query(CPU).filter(CPU.id == cpu.id).update(values={CPU.base_freq: cpu.base_freq})
    if cpu.max_freq:
        db_sess.query(CPU).filter(CPU.id == cpu.id).update(values={CPU.max_freq: cpu.max_freq})
    if cpu.free_mult:
        db_sess.query(CPU).filter(CPU.id == cpu.id).update(values={CPU.free_mult: cpu.free_mult})
    if cpu.memory:
        db_sess.query(CPU).filter(CPU.id == cpu.id).update(values={CPU.memory: cpu.memory})
    if cpu.max_mem_bits:
        db_sess.query(CPU).filter(CPU.id == cpu.id).update(values={CPU.max_mem_bits: cpu.max_mem_bits})
    if cpu.channels:
        db_sess.query(CPU).filter(CPU.id == cpu.id).update(values={CPU.channels: cpu.channels})
    if cpu.min_RAM_freq:
        db_sess.query(CPU).filter(CPU.id == cpu.id).update(values={CPU.min_RAM_freq: cpu.min_RAM_freq})
    if cpu.max_RAM_freq:
        db_sess.query(CPU).filter(CPU.id == cpu.id).update(values={CPU.max_RAM_freq: cpu.max_RAM_freq})
    if cpu.ECC:
        db_sess.query(CPU).filter(CPU.id == cpu.id).update(values={CPU.ECC: cpu.ECC})
    if cpu.TDP:
        db_sess.query(CPU).filter(CPU.id == cpu.id).update(values={CPU.TDP: cpu.TDP})
    if cpu.custom_TDP:
        db_sess.query(CPU).filter(CPU.id == cpu.id).update(values={CPU.custom_TDP: cpu.custom_TDP})
    if cpu.max_temp:
        db_sess.query(CPU).filter(CPU.id == cpu.id).update(values={CPU.max_temp: cpu.max_temp})
    if cpu.has_graphics:
        db_sess.query(CPU).filter(CPU.id == cpu.id).update(values={CPU.has_graphics: cpu.has_graphics})
    if cpu.PCI:
        db_sess.query(CPU).filter(CPU.id == cpu.id).update(values={CPU.PCI: cpu.PCI})
    if cpu.PCI_amount:
        db_sess.query(CPU).filter(CPU.id == cpu.id).update(values={CPU.PCI_amount: cpu.PCI_amount})
    if cpu.bandwidth:
        db_sess.query(CPU).filter(CPU.id == cpu.id).update(values={CPU.bandwidth: cpu.bandwidth})
    if cpu.support_x64:
        db_sess.query(CPU).filter(CPU.id == cpu.id).update(values={CPU.support_x64: cpu.support_x64})
    if cpu.multi_thread:
        db_sess.query(CPU).filter(CPU.id == cpu.id).update(values={CPU.multi_thread: cpu.multi_thread})
    if cpu.add_freq_tech:
        db_sess.query(CPU).filter(CPU.id == cpu.id).update(values={CPU.add_freq_tech: cpu.add_freq_tech})
    if cpu.energy_save_tech:
        db_sess.query(CPU).filter(CPU.id == cpu.id).update(values={CPU.energy_save_tech: cpu.energy_save_tech})
    if cpu.description:
        db_sess.query(CPU).filter(CPU.id == cpu.id).update(values={CPU.description: cpu.description})
    if cpu.price:
        db_sess.query(CPU).filter(CPU.id == cpu.id).update(values={CPU.price: cpu.price})
    if cpu.rating:
        db_sess.query(CPU).filter(CPU.id == cpu.id).update(values={CPU.rating: cpu.rating})
    if cpu.rates:
        db_sess.query(CPU).filter(CPU.id == cpu.id).update(values={CPU.rates: cpu.rates})
    db_sess.commit()
    return flask.jsonify({'success': 'OK'})


# user


@blueprint.route('/api/users', methods=['GET'])
def get_users():
    db_sess = db_session.create_session()
    user = db_sess.query(User).all()
    return flask.jsonify({'users': [item.to_dict(
        only=('id', 'surname', 'name', 'email', 'hashed_password', 'modified_date')
    )
        for item in user]})


@blueprint.route('/api/users_add', methods=['POST'])
def add_users():
    db_sess = db_session.create_session()
    if not request.json:
        return flask.jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['id', 'surname', 'name', 'email', 'hashed_password', 'modified_date']):
        return flask.jsonify({'error': 'Bad request'})
    elif db_sess.query(User).filter(User.id == request.json['id']).first():
        return flask.jsonify({'error': 'Id already exists'})
    user = User(
        id=request.json['id'],
        surname=request.json['surname'],
        name=request.json['name'],
        email=request.json['email'],
        hashed_password=request.json['hashed_password'],
        modified_date=request.json['modified_date']
    )
    db_sess.add(user)
    db_sess.commit()
    return flask.jsonify({'success': 'OK'})


@blueprint.route('/api/users_get/<int:users_id>', methods=['GET'])
def get_user(users_id):
    db_sess = db_session.create_session()
    user = db_sess.query(User).filter(User.id == users_id).first()
    if not user:
        return flask.jsonify({'error': 'Not found'})
    return flask.jsonify(
        {
            'users': user.to_dict(only=(
                'id', 'surname', 'name', 'email', 'hashed_password', 'modified_date')
            )
        }
    )


@blueprint.route('/api/jobs_delete/<int:users_id>', methods=['DELETE'])
def delete_users(users_id):
    db_sess = db_session.create_session()
    user = db_sess.query(User).get(users_id)
    if not user:
        return flask.jsonify({'error': 'Not found'})
    db_sess.delete(user)
    db_sess.commit()
    return flask.jsonify({'success': 'OK'})


@blueprint.route('/api/users_edit/', methods=['PUT'])
def edit_users():
    db_sess = db_session.create_session()
    keyss = ['id', 'surname', 'name', 'email', 'hashed_password', 'modified_date']
    if not request.json:
        return flask.jsonify({'error': 'Empty request'})
    elif 'id' not in request.json or not all(key in keyss for key in request.json):
        return flask.jsonify({'error': 'Bad request'})
    elif not db_sess.query(User).filter(User.id == request.json['id']).first():
        return flask.jsonify({'error': 'Id does not exist'})
    user = User(
        id=request.json['id'],
        surname=request.json.get('surname'),
        name=request.json.get('name'),
        email=request.json.get('email'),
        hashed_password=request.json.get('hashed_password'),
        modified_date=request.json.get('modified_date')
    )
    if user.surname:
        db_sess.query(User).filter(User.id == user.id).update(values={User.surname: user.surname})
    if user.name:
        db_sess.query(User).filter(User.id == user.id).update(values={User.name: user.name})
    if user.email:
        db_sess.query(User).filter(User.id == user.id).update(values={User.email: user.email})
    if user.hashed_password:
        db_sess.query(User).filter(User.id == user.id).update(values={User.hashed_password: user.hashed_password})
    if user.modified_date:
        db_sess.query(User).filter(User.id == user.id).update(values={User.modified_date: user.modified_date})
    db_sess.commit()
    return flask.jsonify({'success': 'OK'})