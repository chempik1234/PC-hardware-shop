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
parser.add_argument("year", required=True, type=int)
parser.add_argument("common_type", required=True)
parser.add_argument("type_ddr", required=True)
parser.add_argument("one_module_memory", required=True, type=int)
parser.add_argument("all_memory", required=True, type=int)
parser.add_argument("modules_amount", required=True, type=int)
parser.add_argument("ecc_memory", required=True, type=bool)
parser.add_argument("rang", required=True, type=int)
parser.add_argument("register_memory", required=True, type=bool)
parser.add_argument("freq", required=True, type=int)
parser.add_argument("intel_xpm_profiles", required=True)
parser.add_argument("modes", required=True, type=int)
parser.add_argument("cas_latency_cl", required=True, type=float)
parser.add_argument("ras_to_cas_delay_trcd", required=True, type=int)
parser.add_argument("row_precharge_delay_trp", required=True, type=int)
parser.add_argument("has_radiator", required=True, type=bool)
parser.add_argument("illumination", required=True, type=bool)
parser.add_argument("height", required=True, type=int)
parser.add_argument("radiator_color", required=True)
parser.add_argument("low_profile", required=True, type=bool)
parser.add_argument("power_voltage", required=True, type=float)
parser.add_argument("description", required=True)
parser.add_argument("price", required=True, type=int)
parser.add_argument("rating", required=True, type=int)
parser.add_argument("rates", required=True, type=int)


def abort_if_ram_dimm_not_found(_id):
    session = db_session.create_session()
    ram_dimm = session.query(RAM_DIMM).get(_id)
    if not ram_dimm:
        abort(404, message=f"RAM DIMM {_id} not found")


class RAMDIMMResource(Resource):
    def get(self, _id):
        abort_if_ram_dimm_not_found(_id)
        session = db_session.create_session()
        rd = session.query(RAM_DIMM).get(_id)
        return jsonify({'ram_dimm': rd.to_dict(
            only=("warranty", "country", "title",
                  "year", "common_type", "type_ddr",
                  "one_module_memory", "all_memory",
                  "modules_amount", "ecc_memory",
                  "rang", "register_memory", "freq",
                  "intel_xpm_profiles", "modes",
                  "cas_latency_cl", "ras_to_cas_delay_trcd",
                  "row_precharge_delay_trp", "has_radiator",
                  "illumination", "height", "radiator_color",
                  "low_profile", "power_voltage",
                  "description", "price", "rating",
                  "rates"))})

    def delete(self, _id):
        abort_if_ram_dimm_not_found(_id)
        session = db_session.create_session()
        rd = session.query(RAM_DIMM).get(_id)
        session.delete(rd)
        session.commit()
        return jsonify({'success': 'OK'})


class RAMDIMMListResource(Resource):
    def get(self):
        session = db_session.create_session()
        rd = session.query(RAM_DIMM).all()
        return jsonify({'ram_dimm': [item.to_dict(
            only=("warranty", "country", "title",
                  "year", "common_type", "type_ddr",
                  "one_module_memory", "all_memory",
                  "modules_amount", "ecc_memory",
                  "rang", "register_memory", "freq",
                  "intel_xpm_profiles", "modes",
                  "cas_latency_cl", "ras_to_cas_delay_trcd",
                  "row_precharge_delay_trp", "has_radiator",
                  "illumination", "height", "radiator_color",
                  "low_profile", "power_voltage",
                  "description", "price", "rating",
                  "rates")) for item in rd]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        rd = RAM_DIMM(
            warranty=args["warranty"],
            country=args["country"],
            title=args["title"],
            year=args["year"],
            common_type=args["common_type"],
            type_ddr=args["type_ddr"],
            one_module_memory=args["one_module_memory"],
            all_memory=args["all_memory"],
            modules_amount=args["modules_amount"],
            ecc_memory=args["ecc_memory"],
            rang=args["rang"],
            register_memory=args["register_memory"],
            freq=args["freq"],
            intel_xpm_profiles=args["intel_xpm_profiles"],
            modes=args["modes"],
            cas_latency_cl=args["cas_latency_cl"],
            ras_to_cas_delay_trcd=args["ras_to_cas_delay_trcd"],
            row_precharge_delay_trp=args["row_precharge_delay_trp"],
            has_radiator=args["has_radiator"],
            illumination=args["illumination"],
            height=args["height"],
            radiator_color=args["radiator_color"],
            low_profile=args["low_profile"],
            power_voltage=args["power_voltage"],
            description=args["description"],
            price=args["price"],
            rating=args["rating"],
            rates=args["rates"]
        )
        session.add(rd)
        session.commit()
        return jsonify({'success': 'OK'})
