from data.__all_models import *
class_ = RAM_DIMM
d = class_.__dict__
print('''
from data import db_session
from data.__all_models import *
from flask import jsonify
from flask_restful import Resource, abort, reqparse
from werkzeug.security import generate_password_hash
parser = reqparse.RequestParser()''')
types = {'INTEGER': 'int',
         'BOOLEAN': 'bool',
         'FLOAT': 'float'}
for i in d.keys():
    if i[0] != '_':
        print(f'parser.add_argument("{i}", required=True', end='')
        if str(d[i].type) != 'VARCHAR':
            print(f', type={types[str(d[i].type)]}', end='')
        print(')')
print('", "'.join(d.keys()))
for i in d.keys():
    if i[0] != '_':
        print(i + '=request.json.get("' + i + '"),')
for i in d.keys():
    if i != 'id' and i[0] != '_':
        print(f'if rd.{i}:')
        print('\tdb_sess.query(RAM_DIMM).filter(RAM_DIMM.id == rd.id).update(values={RAM_DIMM.' + i + ': rd.' + i + '})')