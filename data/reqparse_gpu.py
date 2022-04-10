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
parser.add_argument("manufacturer_code", required=True)
parser.add_argument("is_for_mining", required=True, type=bool)
parser.add_argument("LHR", required=True, type=bool)
parser.add_argument("memory", required=True, type=int)
parser.add_argument("memory_type", required=True)
parser.add_argument("bandwidth", required=True, type=float)
parser.add_argument("band_64x_32x", required=True)
parser.add_argument("max_mem_bandwidth", required=True, type=float)
parser.add_argument("micro_arc", required=True)
parser.add_argument("graph_cpu", required=True)
parser.add_argument("techprocess", required=True, type=int)
parser.add_argument("chip_freq", required=True, type=int)
parser.add_argument("ALU", required=True, type=int)
parser.add_argument("texture_blocks", required=True, type=int)
parser.add_argument("raster_blocks", required=True, type=int)
parser.add_argument("max_temp", required=True, type=int)
parser.add_argument("RTX", required=True, type=bool)
parser.add_argument("appart_accelerate_RT", required=True, type=bool)
parser.add_argument("tenz_cores", required=True, type=int)
parser.add_argument("max_efficiency_FP32", required=True, type=float)
parser.add_argument("connectors", required=True)
parser.add_argument("HDMI_version", required=True)
parser.add_argument("max_resolution", required=True)
parser.add_argument("max_monitors", required=True, type=int)
parser.add_argument("connection_interface", required=True)
parser.add_argument("PCI_version", required=True)
parser.add_argument("support_mult_cpu_config", required=True)
parser.add_argument("need_extra_power", required=True, type=bool)
parser.add_argument("extra_power_connections", required=True, type=bool)
parser.add_argument("max_consuming_power", required=True, type=float)
parser.add_argument("recommended_power", required=True, type=int)
parser.add_argument("cooling", required=True)
parser.add_argument("type_and_amount_fans", required=True)
parser.add_argument("fan_speed_control", required=True, type=bool)
parser.add_argument("low_profile", required=True, type=bool)
parser.add_argument("needed_slots", required=True, type=int)
parser.add_argument("length", required=True, type=int)
parser.add_argument("width", required=True, type=int)
parser.add_argument("weight", required=True, type=int)
parser.add_argument("illumination", required=True, type=bool)
parser.add_argument("synch_RGB", required=True, type=bool)
parser.add_argument("LCD", required=True, type=bool)
parser.add_argument("BIOS_switch", required=True, type=bool)
parser.add_argument("description", required=True)
parser.add_argument("price", required=True, type=int)
parser.add_argument("rating", required=True, type=int)
parser.add_argument("rates", required=True, type=int)


def abort_if_gpu_not_found(gpu_id):
    session = db_session.create_session()
    gpus = session.query(GPU).get(gpu_id)
    if not gpus:
        abort(404, message=f"GPU {gpu_id} not found")


class GPUResource(Resource):
    def get(self, gpu_id):
        abort_if_gpu_not_found(gpu_id)
        session = db_session.create_session()
        gpu = session.query(GPU).get(gpu_id)
        return jsonify({'gpu': gpu.to_dict(
            only=("warranty", "country", "title", "year",
                  "manufacturer_code", "is_for_mining",
                  "LHR", "memory", "memory_type", "bandwidth",
                  "band_64x_32x", "max_mem_bandwidth",
                  "micro_arc", "graph_cpu", "techprocess",
                  "chip_freq", "ALU", "texture_blocks",
                  "raster_blocks", "max_temp", "RTX",
                  "appart_accelerate_RT", "tenz_cores",
                  "max_efficiency_FP32", "connectors",
                  "HDMI_version", "max_resolution",
                  "max_monitors", "connection_interface",
                  "PCI_version", "support_mult_cpu_config",
                  "need_extra_power", "extra_power_connections",
                  "max_consuming_power", "recommended_power",
                  "cooling", "type_and_amount_fans",
                  "fan_speed_control", "low_profile",
                  "needed_slots", "length", "width",
                  "weight", "illumination", "synch_RGB",
                  "LCD", "BIOS_switch", "description",
                  "price", "rating", "rates"))})

    def delete(self, gpu_id):
        abort_if_gpu_not_found(gpu_id)
        session = db_session.create_session()
        gpu = session.query(GPU).get(gpu_id)
        session.delete(gpu)
        session.commit()
        return jsonify({'success': 'OK'})


class GPUListResource(Resource):
    def get(self):
        session = db_session.create_session()
        gpu = session.query(GPU).all()
        return jsonify({'gpu': [item.to_dict(
            only=("warranty", "country", "title", "year",
                  "manufacturer_code", "is_for_mining",
                  "LHR", "memory", "memory_type", "bandwidth",
                  "band_64x_32x", "max_mem_bandwidth",
                  "micro_arc", "graph_cpu", "techprocess",
                  "chip_freq", "ALU", "texture_blocks",
                  "raster_blocks", "max_temp", "RTX",
                  "appart_accelerate_RT", "tenz_cores",
                  "max_efficiency_FP32", "connectors",
                  "HDMI_version", "max_resolution",
                  "max_monitors", "connection_interface",
                  "PCI_version", "support_mult_cpu_config",
                  "need_extra_power", "extra_power_connections",
                  "max_consuming_power", "recommended_power",
                  "cooling", "type_and_amount_fans",
                  "fan_speed_control", "low_profile",
                  "needed_slots", "length", "width",
                  "weight", "illumination", "synch_RGB",
                  "LCD", "BIOS_switch", "description",
                  "price", "rating", "rates")) for item in gpu]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        gpu = GPU(
            warranty=args["warranty"],
            country=args["country"],
            title=args["title"],
            year=args["year"],
            manufacturer_code=args["manufacturer_code"],
            is_for_mining=args["is_for_mining"],
            LHR=args["LHR"],
            memory=args["memory"],
            memory_type=args["memory_type"],
            bandwidth=args["bandwidth"],
            band_64x_32x=args["band_64x_32x"],
            max_mem_bandwidth=args["max_mem_bandwidth"],
            micro_arc=args["micro_arc"],
            graph_cpu=args["graph_cpu"],
            techprocess=args["techprocess"],
            chip_freq=args["chip_freq"],
            ALU=args["ALU"],
            texture_blocks=args["texture_blocks"],
            raster_blocks=args["raster_blocks"],
            max_temp=args["max_temp"],
            RTX=args["RTX"],
            appart_accelerate_RT=args["appart_accelerate_RT"],
            tenz_cores=args["tenz_cores"],
            max_efficiency_FP32=args["max_efficiency_FP32"],
            connectors=args["connectors"],
            HDMI_version=args["HDMI_version"],
            max_resolution=args["max_resolution"],
            max_monitors=args["max_monitors"],
            connection_interface=args["connection_interface"],
            PCI_version=args["PCI_version"],
            support_mult_cpu_config=args["support_mult_cpu_config"],
            need_extra_power=args["need_extra_power"],
            extra_power_connections=args["extra_power_connections"],
            max_consuming_power=args["max_consuming_power"],
            recommended_power=args["recommended_power"],
            cooling=args["cooling"],
            type_and_amount_fans=args["type_and_amount_fans"],
            fan_speed_control=args["fan_speed_control"],
            low_profile=args["low_profile"],
            needed_slots=args["needed_slots"],
            length=args["length"],
            width=args["width"],
            weight=args["weight"],
            illumination=args["illumination"],
            synch_RGB=args["synch_RGB"],
            LCD=args["LCD"],
            BIOS_switch=args["BIOS_switch"],
            description=args["description"],
            price=args["price"],
            rating=args["rating"],
            rates=args["rates"]
        )
        session.add(gpu)
        session.commit()
        return jsonify({'success': 'OK'})
