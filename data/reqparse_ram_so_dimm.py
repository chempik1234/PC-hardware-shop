from data import db_session
from data.__all_models import *
from flask import jsonify
from flask_restful import Resource, abort, reqparse
from werkzeug.security import generate_password_hash
parser = reqparse.RequestParser()
parser.add_argument("id", required=True, type=int)
parser.add_argument("warranty", required=True)
parser.add_argument("country", required=True)
parser.add_argument("title", required=True)
parser.add_argument("common_type", required=True)
parser.add_argument("type_ddr", required=True)
parser.add_argument("one_module_memory", required=True, type=int)
parser.add_argument("all_memory", required=True, type=int)
parser.add_argument("modules_amount", required=True, type=int)
parser.add_argument("freq", required=True, type=int)
parser.add_argument("ras_to_cas_delay_trcd", required=True, type=int)
parser.add_argument("row_precharge_delay_trp", required=True, type=int)
parser.add_argument("cas_latency_cl", required=True, type=float)
parser.add_argument("chips_amount", required=True, type=int)
parser.add_argument("double_sided_chips_setup", required=True, type=bool)
parser.add_argument("power_voltage", required=True, type=float)
parser.add_argument("description", required=True)
parser.add_argument("price", required=True, type=int)
parser.add_argument("rating", required=True, type=int)
parser.add_argument("rates", required=True, type=int)


def abort_if_ram_so_dimm_not_found(_id):
    session = db_session.create_session()
    rsd = session.query(RAM_SO_DIMM).get(_id)
    if not rsd:
        abort(404, message=f"RAM SO-DIMM {_id} not found")


class RAMSODIMMResource(Resource):
    def get(self, _id):
        abort_if_ram_so_dimm_not_found(_id)
        session = db_session.create_session()
        rsd = session.query(RAM_SO_DIMM).get(_id)
        return jsonify({'ram_so_dimm': rsd.to_dict(
            only=("warranty", "country", "title",
                  "common_type", "type_ddr",
                  "one_module_memory", "all_memory",
                  "modules_amount", "freq",
                  "ras_to_cas_delay_trcd",
                  "row_precharge_delay_trp",
                  "cas_latency_cl", "chips_amount",
                  "double_sided_chips_setup",
                  "power_voltage", "description",
                  "price", "rating", "rates"))})

    def delete(self, _id):
        abort_if_ram_so_dimm_not_found(_id)
        session = db_session.create_session()
        rsd = session.query(RAM_SO_DIMM).get(_id)
        session.delete(rsd)
        session.commit()
        return jsonify({'success': 'OK'})


class RAMSODIMMListResource(Resource):
    def get(self):
        session = db_session.create_session()
        rsd = session.query(RAM_SO_DIMM).all()
        return jsonify({'ram_so_dimm': [item.to_dict(
            only=("warranty", "country", "title",
                  "common_type", "type_ddr",
                  "one_module_memory", "all_memory",
                  "modules_amount", "freq",
                  "ras_to_cas_delay_trcd",
                  "row_precharge_delay_trp",
                  "cas_latency_cl", "chips_amount",
                  "double_sided_chips_setup",
                  "power_voltage", "description",
                  "price", "rating", "rates")) for item in rsd]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        rsd = RAM_SO_DIMM(
            warranty=args["warranty"],
            country=args["country"],
            title=args["title"],
            common_type=args["common_type"],
            type_ddr=args["type_ddr"],
            one_module_memory=args["one_module_memory"],
            all_memory=args["all_memory"],
            modules_amount=args["modules_amount"],
            freq=args["freq"],
            ras_to_cas_delay_trcd=args["ras_to_cas_delay_trcd"],
            row_precharge_delay_trp=args["row_precharge_delay_trp"],
            cas_latency_cl=args["cas_latency_cl"],
            chips_amount=args["chips_amount"],
            double_sided_chips_setup=args["double_sided_chips_setup"],
            power_voltage=args["power_voltage"],
            description=args["description"],
            price=args["price"],
            rating=args["rating"],
            rates=args["rates"]
        )
        session.add(rsd)
        session.commit()
        return jsonify({'success': 'OK'})
