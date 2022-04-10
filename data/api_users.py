import flask
from data.__all_models import *
from flask import request
from data import db_session


blueprint = flask.Blueprint('user_api', __name__, template_folder='templates')


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