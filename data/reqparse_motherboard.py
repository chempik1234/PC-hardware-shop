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
parser.add_argument("form_factor", required=True)
parser.add_argument("width", required=True, type=int)
parser.add_argument("height", required=True)
parser.add_argument("socket", required=True)
parser.add_argument("chipset", required=True)
parser.add_argument("built_in_cpu", required=True, type=bool)
parser.add_argument("title_built_in_cpu", required=True)
parser.add_argument("memory_slots_amount", required=True, type=int)
parser.add_argument("memory_type", required=True)
parser.add_argument("ram_freq", required=True)
parser.add_argument("max_memory", required=True, type=int)
parser.add_argument("memory_channels_amount", required=True, type=int)
parser.add_argument("memory_form_factor", required=True)
parser.add_argument("m2_slots_amount", required=True, type=int)
parser.add_argument("sata_slots_amount", required=True, type=int)
parser.add_argument("nvme_support", required=True, type=bool)
parser.add_argument("sata_raid_mode", required=True)
parser.add_argument("m2_slots", required=True)
parser.add_argument("m2_form_factor", required=True)
parser.add_argument("other_drive_slots", required=True)
parser.add_argument("pci_express_version", required=True)
parser.add_argument("pci_e_x1_slots_amount", required=True, type=int)
parser.add_argument("pci_e_x16_slots_amount", required=True, type=int)
parser.add_argument("sli_crossfire_support", required=True, type=bool)
parser.add_argument("other_expansion_slots", required=True)
parser.add_argument("video_outputs", required=True)
parser.add_argument("usb_amount_and_type", required=True)
parser.add_argument("digital_and_audio_ports_s_pdif", required=True)
parser.add_argument("other_slots_on_back_panel", required=True)
parser.add_argument("network_ports_amount_rj45", required=True, type=int)
parser.add_argument("fan_4pin_connectors", required=True, type=int)
parser.add_argument("internal_connectors_on_usb_plate_amount_and_type", required=True)
parser.add_argument("cpu_cooler_power_slot", required=True)
parser.add_argument("m2_e_key", required=True, type=bool)
parser.add_argument("lpt_interface", required=True, type=bool)
parser.add_argument("sound_adapter_chipset", required=True)
parser.add_argument("sound_scheme", required=True)
parser.add_argument("built_in_wifi_adapter", required=True)
parser.add_argument("bluetooth", required=True)
parser.add_argument("network_adapter_speed", required=True)
parser.add_argument("network_adapter_chipset", required=True)
parser.add_argument("power_phases_amount", required=True, type=int)
parser.add_argument("cpu_power_slot", required=True)
parser.add_argument("passive_cooling", required=True)
parser.add_argument("main_power_slot", required=True)
parser.add_argument("illumination", required=True, type=bool)
parser.add_argument("description", required=True)
parser.add_argument("price", required=True, type=int)
parser.add_argument("rating", required=True, type=int)
parser.add_argument("rates", required=True, type=int)


def abort_if_motherboard_not_found(motherboard_id):
    session = db_session.create_session()
    mbs = session.query(CPU).get(motherboard_id)
    if not mbs:
        abort(404, message=f"Motherboard {motherboard_id} not found")


class MotherboardResource(Resource):
    def get(self, _id):
        abort_if_motherboard_not_found(_id)
        session = db_session.create_session()
        mb = session.query(CPU).get(_id)
        return jsonify({'motherboard': mb.to_dict(
            only=("warranty", "country", "title",
                  "year", "form_factor", "width",
                  "height", "socket", "chipset",
                  "built_in_cpu", "title_built_in_cpu",
                  "memory_slots_amount", "memory_type",
                  "ram_freq", "max_memory",
                  "memory_channels_amount",
                  "memory_form_factor", "m2_slots_amount",
                  "sata_slots_amount", "nvme_support",
                  "sata_raid_mode", "m2_slots",
                  "m2_form_factor", "other_drive_slots",
                  "pci_express_version",
                  "pci_e_x1_slots_amount",
                  "pci_e_x16_slots_amount",
                  "sli_crossfire_support",
                  "other_expansion_slots",
                  "video_outputs", "usb_amount_and_type",
                  "digital_and_audio_ports_s_pdif",
                  "other_slots_on_back_panel",
                  "network_ports_amount_rj45",
                  "fan_4pin_connectors",
                  "internal_connectors_on_usb_plate_amount_and_type",
                  "cpu_cooler_power_slot",
                  "m2_e_key", "lpt_interface",
                  "sound_adapter_chipset",
                  "sound_scheme", "built_in_wifi_adapter",
                  "bluetooth", "network_adapter_speed",
                  "network_adapter_chipset", "power_phases_amount",
                  "cpu_power_slot", "passive_cooling",
                  "main_power_slot", "illumination",
                  "description", "price", "rating",
                  "rates"))})

    def delete(self, _id):
        abort_if_motherboard_not_found(_id)
        session = db_session.create_session()
        mb = session.query(Motherboard).get(_id)
        session.delete(mb)
        session.commit()
        return jsonify({'success': 'OK'})


class MotherboardListResource(Resource):
    def get(self):
        session = db_session.create_session()
        mb = session.query(Motherboard).all()
        return jsonify({'mb': [item.to_dict(
            only=("warranty", "country", "title",
                  "year", "form_factor", "width",
                  "height", "socket", "chipset",
                  "built_in_cpu", "title_built_in_cpu",
                  "memory_slots_amount", "memory_type",
                  "ram_freq", "max_memory",
                  "memory_channels_amount",
                  "memory_form_factor", "m2_slots_amount",
                  "sata_slots_amount", "nvme_support",
                  "sata_raid_mode", "m2_slots",
                  "m2_form_factor", "other_drive_slots",
                  "pci_express_version",
                  "pci_e_x1_slots_amount",
                  "pci_e_x16_slots_amount",
                  "sli_crossfire_support",
                  "other_expansion_slots",
                  "video_outputs", "usb_amount_and_type",
                  "digital_and_audio_ports_s_pdif",
                  "other_slots_on_back_panel",
                  "network_ports_amount_rj45",
                  "fan_4pin_connectors",
                  "internal_connectors_on_usb_plate_amount_and_type",
                  "cpu_cooler_power_slot",
                  "m2_e_key", "lpt_interface",
                  "sound_adapter_chipset",
                  "sound_scheme", "built_in_wifi_adapter",
                  "bluetooth", "network_adapter_speed",
                  "network_adapter_chipset", "power_phases_amount",
                  "cpu_power_slot", "passive_cooling",
                  "main_power_slot", "illumination",
                  "description", "price", "rating",
                  "rates")) for item in mb]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        mb = Motherboard(
            warranty=args["warranty"],
            country=args["country"],
            title=args["title"],
            year=args["year"],
            form_factor=args["form_factor"],
            width=args["width"],
            height=args["height"],
            socket=args["socket"],
            chipset=args["chipset"],
            built_in_cpu=args["built_in_cpu"],
            title_built_in_cpu=args["title_built_in_cpu"],
            memory_slots_amount=args["memory_slots_amount"],
            memory_type=args["memory_type"],
            ram_freq=args["ram_freq"],
            max_memory=args["max_memory"],
            memory_channels_amount=args["memory_channels_amount"],
            memory_form_factor=args["memory_form_factor"],
            m2_slots_amount=args["m2_slots_amount"],
            sata_slots_amount=args["sata_slots_amount"],
            nvme_support=args["nvme_support"],
            sata_raid_mode=args["sata_raid_mode"],
            m2_slots=args["m2_slots"],
            m2_form_factor=args["m2_form_factor"],
            other_drive_slots=args["other_drive_slots"],
            pci_express_version=args["pci_express_version"],
            pci_e_x1_slots_amount=args["pci_e_x1_slots_amount"],
            pci_e_x16_slots_amount=args["pci_e_x16_slots_amount"],
            sli_crossfire_support=args["sli_crossfire_support"],
            other_expansion_slots=args["other_expansion_slots"],
            video_outputs=args["video_outputs"],
            usb_amount_and_type=args["usb_amount_and_type"],
            digital_and_audio_ports_s_pdif=args["digital_and_audio_ports_s_pdif"],
            other_slots_on_back_panel=args["other_slots_on_back_panel"],
            network_ports_amount_rj45=args["network_ports_amount_rj45"],
            fan_4pin_connectors=args["fan_4pin_connectors"],
            internal_connectors_on_usb_plate_amount_and_type=args["internal_connectors_on_usb_plate_amount_and_type"],
            cpu_cooler_power_slot=args["cpu_cooler_power_slot"],
            m2_e_key=args["m2_e_key"],
            lpt_interface=args["lpt_interface"],
            sound_adapter_chipset=args["sound_adapter_chipset"],
            sound_scheme=args["sound_scheme"],
            built_in_wifi_adapter=args["built_in_wifi_adapter"],
            bluetooth=args["bluetooth"],
            network_adapter_speed=args["network_adapter_speed"],
            network_adapter_chipset=args["network_adapter_chipset"],
            power_phases_amount=args["power_phases_amount"],
            cpu_power_slot=args["cpu_power_slot"],
            passive_cooling=args["passive_cooling"],
            main_power_slot=args["main_power_slot"],
            illumination=args["illumination"],
            description=args["description"],
            price=args["price"],
            rating=args["rating"],
            rates=args["rates"]
        )
        session.add(mb)
        session.commit()
        return jsonify({'success': 'OK'})
