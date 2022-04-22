from data import db_session
from data.__all_models import *
from flask import jsonify
from flask_restful import Resource, abort, reqparse
from werkzeug.security import generate_password_hash
parser = reqparse.RequestParser()
parser.add_argument("id", required=True, type=int)
parser.add_argument("warranty", required=True, type=int)
parser.add_argument("country", required=True)
parser.add_argument("title", required=True)
parser.add_argument("year", required=True, type=int)
parser.add_argument("memory_bits", required=True, type=int)
parser.add_argument("rotation_speed", required=True, type=int)
parser.add_argument("cash_memory_bits", required=True, type=int)
parser.add_argument("raid_massives_optimization", required=True, type=bool)
parser.add_argument("helium_fill", required=True, type=bool)
parser.add_argument("noise_dba", required=True, type=int)
parser.add_argument("writing_tech_CMR_SMR", required=True, type=bool)
parser.add_argument("position_park_cycles_amount", required=True, type=int)
parser.add_argument("width", required=True, type=int)
parser.add_argument("length", required=True, type=int)
parser.add_argument("height", required=True, type=int)
parser.add_argument("description", required=True)
parser.add_argument("price", required=True, type=int)
parser.add_argument("rating", required=True, type=int)
parser.add_argument("rates", required=True, type=int)


def abort_if_hdd35_not_found(_id):
    session = db_session.create_session()
    hdd35 = session.query(HDD35).get(_id)
    if not hdd35:
        abort(404, message=f"SSD {_id} not found")


class HDD35Resource(Resource):
    def get(self, _id):
        abort_if_hdd35_not_found(_id)
        session = db_session.create_session()
        hdd35 = session.query(HDD35).get(_id)
        return jsonify({'hdd35': hdd35.to_dict(
            only=("warranty", "country",
                  "title", "year",
                  "memory_bits", "rotation_speed",
                  "cash_memory_bits",
                  "raid_massives_optimization",
                  "helium_fill", "noise_dba",
                  "writing_tech_CMR_SMR",
                  "position_park_cycles_amount",
                  "width", "length", "height",
                  "description", "price", "rating",
                  "rates"))})

    def delete(self, _id):
        abort_if_hdd35_not_found(_id)
        session = db_session.create_session()
        hdd35 = session.query(HDD35).get(_id)
        session.delete(hdd35)
        session.commit()
        return jsonify({'success': 'OK'})


class HDD35ListResource(Resource):
    def get(self):
        session = db_session.create_session()
        hdd35 = session.query(HDD35).all()
        return jsonify({'hdd35': [item.to_dict(
            only=("warranty", "country",
                  "title", "year",
                  "memory_bits", "rotation_speed",
                  "cash_memory_bits",
                  "raid_massives_optimization",
                  "helium_fill", "noise_dba",
                  "writing_tech_CMR_SMR",
                  "position_park_cycles_amount",
                  "width", "length", "height",
                  "description", "price", "rating",
                  "rates")) for item in hdd35]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        hdd35 = HDD35(
            warranty=args.get("warranty"),
            country=args.get("country"),
            title=args.get("title"),
            year=args.get("year"),
            memory_bits=args.get("memory_bits"),
            rotation_speed=args.get("rotation_speed"),
            cash_memory_bits=args.get("cash_memory_bits"),
            raid_massives_optimization=args.get("raid_massives_optimization"),
            helium_fill=args.get("helium_fill"),
            noise_dba=args.get("noise_dba"),
            writing_tech_CMR_SMR=args.get("writing_tech_CMR_SMR"),
            position_park_cycles_amount=args.get("position_park_cycles_amount"),
            width=args.get("width"),
            length=args.get("length"),
            height=args.get("height"),
            description=args.get("description"),
            price=args["price"],
            rating=args["rating"],
            rates=args["rates"]
        )
        session.add(hdd35)
        session.commit()
        return jsonify({'success': 'OK'})
