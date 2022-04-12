from data import db_session
from data.__all_models import *
from flask import jsonify
from flask_restful import Resource, abort, reqparse
from werkzeug.security import generate_password_hash
parser = reqparse.RequestParser()
parser.add_argument("id", required=True, type=int)
parser.add_argument("warranty", required=True, type=int)
parser.add_argument("title", required=True)
parser.add_argument("year", required=True, type=int)
parser.add_argument("ssd_type", required=True)
parser.add_argument("memory", required=True, type=int)
parser.add_argument("phys_interface", required=True)
parser.add_argument("bit_per_cell_amount", required=True)
parser.add_argument("memory_structure", required=True)
parser.add_argument("DRAM_buffer", required=True, type=bool)
parser.add_argument("max_cons_reading_speed", required=True, type=int)
parser.add_argument("max_cons_writing_speed", required=True, type=int)
parser.add_argument("max_writing_resource_TBW", required=True, type=int)
parser.add_argument("DWPD", required=True, type=float)
parser.add_argument("hardware_data_encryption", required=True, type=bool)
parser.add_argument("width", required=True, type=int)
parser.add_argument("form_factor", required=True, type=bool)
parser.add_argument("description", required=True)
parser.add_argument("price", required=True, type=int)
parser.add_argument("rating", required=True, type=int)
parser.add_argument("rates", required=True, type=int)


def abort_if_ssd_not_found(_id):
    session = db_session.create_session()
    ssds = session.query(SSD).get(_id)
    if not ssds:
        abort(404, message=f"SSD {_id} not found")


class SSDResource(Resource):
    def get(self, _id):
        abort_if_ssd_not_found(_id)
        session = db_session.create_session()
        ssd = session.query(SSD).get(_id)
        return jsonify({'ssd': ssd.to_dict(
            only=("warranty", "title", "year",
                  "ssd_type", "memory",
                  "phys_interface",
                  "bit_per_cell_amount",
                  "memory_structure", "DRAM_buffer",
                  "max_cons_reading_speed",
                  "max_cons_writing_speed",
                  "max_writing_resource_TBW", "DWPD",
                  "hardware_data_encryption", "width",
                  "form_factor", "description", "price",
                  "rating", "rates"))})

    def delete(self, _id):
        abort_if_ssd_not_found(_id)
        session = db_session.create_session()
        ssd = session.query(SSD).get(_id)
        session.delete(ssd)
        session.commit()
        return jsonify({'success': 'OK'})


class SSDListResource(Resource):
    def get(self):
        session = db_session.create_session()
        ssd = session.query(SSD).all()
        return jsonify({'ssd': [item.to_dict(
            only=("warranty", "title", "year",
                  "ssd_type", "memory",
                  "phys_interface",
                  "bit_per_cell_amount",
                  "memory_structure", "DRAM_buffer",
                  "max_cons_reading_speed",
                  "max_cons_writing_speed",
                  "max_writing_resource_TBW", "DWPD",
                  "hardware_data_encryption", "width",
                  "form_factor", "description", "price",
                  "rating", "rates")) for item in ssd]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        ssd = SSD(
            warranty=args.get("warranty"),
            title=args.get("title"),
            year=args.get("year"),
            ssd_type=args.get("ssd_type"),
            memory=args.get("memory"),
            phys_interface=args.get("phys_interface"),
            bit_per_cell_amount=args.get("bit_per_cell_amount"),
            memory_structure=args.get("memory_structure"),
            DRAM_buffer=args.get("DRAM_buffer"),
            max_cons_reading_speed=args.get("max_cons_reading_speed"),
            max_cons_writing_speed=args.get("max_cons_writing_speed"),
            max_writing_resource_TBW=args.get("max_writing_resource_TBW"),
            DWPD=args.get("DWPD"),
            hardware_data_encryption=args.get("hardware_data_encryption"),
            width=args.get("width"),
            form_factor=args.get("form_factor"),
            description=args.get("description"),
            price=args["price"],
            rating=args["rating"],
            rates=args["rates"]
        )
        session.add(ssd)
        session.commit()
        return jsonify({'success': 'OK'})
