import flask
from data.__all_models import *
from flask import request
from data import db_session


blueprint = flask.Blueprint('motherboard_api', __name__, template_folder='templates')


@blueprint.route('/api/motherboard', methods=['GET'])
def get_motherboards():
    db_sess = db_session.create_session()
    mb = db_sess.query(Motherboard).all()
    return flask.jsonify({'motherboard': [item.to_dict(
        only=("id", "warranty", "country", "title", "year",
              "form_factor", "width", "height", "socket",
              "chipset", "built_in_cpu", "title_built_in_cpu",
              "memory_slots_amount", "memory_type", "ram_freq",
              "max_memory", "memory_channels_amount",
              "memory_form_factor", "m2_slots_amount",
              "sata_slots_amount", "nvme_support",
              "sata_raid_mode", "m2_slots", "m2_form_factor",
              "other_drive_slots", "pci_express_version",
              "pci_e_x1_slots_amount", "pci_e_x16_slots_amount",
              "sli_crossfire_support", "other_expansion_slots",
              "video_outputs", "usb_amount_and_type",
              "digital_and_audio_ports_s_pdif",
              "other_slots_on_back_panel",
              "network_ports_amount_rj45",
              "fan_4pin_connectors",
              "internal_connectors_on_usb_plate_amount_and_type",
              "cpu_cooler_power_slot", "m2_e_key",
              "lpt_interface", "sound_adapter_chipset",
              "sound_scheme", "built_in_wifi_adapter", "bluetooth",
              "network_adapter_speed", "network_adapter_chipset",
              "power_phases_amount", "cpu_power_slot", "passive_cooling",
              "main_power_slot", "illumination", "description",
              "price", "rating", "rates"))
        for item in mb]})


@blueprint.route('/api/motherboard_add', methods=['POST'])
def add_motherboard():
    db_sess = db_session.create_session()
    if not request.json:
        return flask.jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ["id", "warranty", "country", "title", "year",
                  "form_factor", "width", "height", "socket",
                  "chipset", "built_in_cpu", "title_built_in_cpu",
                  "memory_slots_amount", "memory_type", "ram_freq",
                  "max_memory", "memory_channels_amount",
                  "memory_form_factor", "m2_slots_amount",
                  "sata_slots_amount", "nvme_support",
                  "sata_raid_mode", "m2_slots", "m2_form_factor",
                  "other_drive_slots", "pci_express_version",
                  "pci_e_x1_slots_amount", "pci_e_x16_slots_amount",
                  "sli_crossfire_support", "other_expansion_slots",
                  "video_outputs", "usb_amount_and_type",
                  "digital_and_audio_ports_s_pdif",
                  "other_slots_on_back_panel",
                  "network_ports_amount_rj45",
                  "fan_4pin_connectors",
                  "internal_connectors_on_usb_plate_amount_and_type",
                  "cpu_cooler_power_slot", "m2_e_key",
                  "lpt_interface", "sound_adapter_chipset",
                  "sound_scheme", "built_in_wifi_adapter", "bluetooth",
                  "network_adapter_speed", "network_adapter_chipset",
                  "power_phases_amount", "cpu_power_slot", "passive_cooling",
                  "main_power_slot", "illumination", "description",
                  "price", "rating", "rates"]):
        return flask.jsonify({'error': 'Bad request'})
    elif db_sess.query(Motherboard).filter(Motherboard.id == request.json['id']).first():
        return flask.jsonify({'error': 'Id already exists'})
    mb = Motherboard(
        id=request.json['id'],
        warranty=request.json.get("warranty"),
        country=request.json.get("country"),
        title=request.json.get("title"),
        year=request.json.get("year"),
        form_factor=request.json.get("form_factor"),
        width=request.json.get("width"),
        height=request.json.get("height"),
        socket=request.json.get("socket"),
        chipset=request.json.get("chipset"),
        built_in_cpu=request.json.get("built_in_cpu"),
        title_built_in_cpu=request.json.get("title_built_in_cpu"),
        memory_slots_amount=request.json.get("memory_slots_amount"),
        memory_type=request.json.get("memory_type"),
        ram_freq=request.json.get("ram_freq"),
        max_memory=request.json.get("max_memory"),
        memory_channels_amount=request.json.get("memory_channels_amount"),
        memory_form_factor=request.json.get("memory_form_factor"),
        m2_slots_amount=request.json.get("m2_slots_amount"),
        sata_slots_amount=request.json.get("sata_slots_amount"),
        nvme_support=request.json.get("nvme_support"),
        sata_raid_mode=request.json.get("sata_raid_mode"),
        m2_slots=request.json.get("m2_slots"),
        m2_form_factor=request.json.get("m2_form_factor"),
        other_drive_slots=request.json.get("other_drive_slots"),
        pci_express_version=request.json.get("pci_express_version"),
        pci_e_x1_slots_amount=request.json.get("pci_e_x1_slots_amount"),
        pci_e_x16_slots_amount=request.json.get("pci_e_x16_slots_amount"),
        sli_crossfire_support=request.json.get("sli_crossfire_support"),
        other_expansion_slots=request.json.get("other_expansion_slots"),
        video_outputs=request.json.get("video_outputs"),
        usb_amount_and_type=request.json.get("usb_amount_and_type"),
        digital_and_audio_ports_s_pdif=request.json.get("digital_and_audio_ports_s_pdif"),
        other_slots_on_back_panel=request.json.get("other_slots_on_back_panel"),
        network_ports_amount_rj45=request.json.get("network_ports_amount_rj45"),
        fan_4pin_connectors=request.json.get("fan_4pin_connectors"),
        internal_connectors_on_usb_plate_amount_and_type=request.json.get(
            "internal_connectors_on_usb_plate_amount_and_type"),
        cpu_cooler_power_slot=request.json.get("cpu_cooler_power_slot"),
        m2_e_key=request.json.get("m2_e_key"),
        lpt_interface=request.json.get("lpt_interface"),
        sound_adapter_chipset=request.json.get("sound_adapter_chipset"),
        sound_scheme=request.json.get("sound_scheme"),
        built_in_wifi_adapter=request.json.get("built_in_wifi_adapter"),
        bluetooth=request.json.get("bluetooth"),
        network_adapter_speed=request.json.get("network_adapter_speed"),
        network_adapter_chipset=request.json.get("network_adapter_chipset"),
        power_phases_amount=request.json.get("power_phases_amount"),
        cpu_power_slot=request.json.get("cpu_power_slot"),
        passive_cooling=request.json.get("passive_cooling"),
        main_power_slot=request.json.get("main_power_slot"),
        illumination=request.json.get("illumination"),
        description=request.json.get("description"),
        price=request.json.get("price"),
        rating=request.json.get("rating"),
        rates=request.json.get("rates"),
    )
    db_sess.add(mb)
    db_sess.commit()
    return flask.jsonify({'success': 'OK'})


@blueprint.route('/api/motherboard_get/<int:_id>', methods=['GET'])
def get_motherboard(_id):
    db_sess = db_session.create_session()
    mb = db_sess.query(Motherboard).filter(Motherboard.id == _id).first()
    if not mb:
        return flask.jsonify({'error': 'Not found'})
    return flask.jsonify(
        {
            'motherboard': mb.to_dict(
                "id", "warranty", "country", "title", "year",
                "form_factor", "width", "height", "socket",
                "chipset", "built_in_cpu", "title_built_in_cpu",
                "memory_slots_amount", "memory_type", "ram_freq",
                "max_memory", "memory_channels_amount",
                "memory_form_factor", "m2_slots_amount",
                "sata_slots_amount", "nvme_support",
                "sata_raid_mode", "m2_slots", "m2_form_factor",
                "other_drive_slots", "pci_express_version",
                "pci_e_x1_slots_amount", "pci_e_x16_slots_amount",
                "sli_crossfire_support", "other_expansion_slots",
                "video_outputs", "usb_amount_and_type",
                "digital_and_audio_ports_s_pdif",
                "other_slots_on_back_panel",
                "network_ports_amount_rj45",
                "fan_4pin_connectors",
                "internal_connectors_on_usb_plate_amount_and_type",
                "cpu_cooler_power_slot", "m2_e_key",
                "lpt_interface", "sound_adapter_chipset",
                "sound_scheme", "built_in_wifi_adapter", "bluetooth",
                "network_adapter_speed", "network_adapter_chipset",
                "power_phases_amount", "cpu_power_slot", "passive_cooling",
                "main_power_slot", "illumination", "description",
                "price", "rating", "rates"
            )
        }
    )


@blueprint.route('/api/motherboard_delete/<int:_id>', methods=['DELETE'])
def delete_motherboard(_id):
    db_sess = db_session.create_session()
    mb = db_sess.query(Motherboard).get(_id)
    if not mb:
        return flask.jsonify({'error': 'Not found'})
    db_sess.delete(mb)
    db_sess.commit()
    return flask.jsonify({'success': 'OK'})


@blueprint.route('/api/motherboard_edit/', methods=['PUT'])
def edit_motherboard():
    db_sess = db_session.create_session()
    keyss = ["id", "warranty", "country", "title", "year",
             "form_factor", "width", "height", "socket",
             "chipset", "built_in_cpu", "title_built_in_cpu",
             "memory_slots_amount", "memory_type", "ram_freq",
             "max_memory", "memory_channels_amount",
             "memory_form_factor", "m2_slots_amount",
             "sata_slots_amount", "nvme_support",
             "sata_raid_mode", "m2_slots", "m2_form_factor",
             "other_drive_slots", "pci_express_version",
             "pci_e_x1_slots_amount", "pci_e_x16_slots_amount",
             "sli_crossfire_support", "other_expansion_slots",
             "video_outputs", "usb_amount_and_type",
             "digital_and_audio_ports_s_pdif",
             "other_slots_on_back_panel",
             "network_ports_amount_rj45",
             "fan_4pin_connectors",
             "internal_connectors_on_usb_plate_amount_and_type",
             "cpu_cooler_power_slot", "m2_e_key",
             "lpt_interface", "sound_adapter_chipset",
             "sound_scheme", "built_in_wifi_adapter", "bluetooth",
             "network_adapter_speed", "network_adapter_chipset",
             "power_phases_amount", "cpu_power_slot", "passive_cooling",
             "main_power_slot", "illumination", "description",
             "price", "rating", "rates"]
    if not request.json:
        return flask.jsonify({'error': 'Empty request'})
    elif 'id' not in request.json or not all(key in keyss for key in request.json):
        return flask.jsonify({'error': 'Bad request'})
    elif not db_sess.query(Motherboard).filter(Motherboard.id == request.json['id']).first():
        return flask.jsonify({'error': 'Id does not exist'})
    mb = Motherboard(
        id=request.json['id'],
        warranty=request.json.get("warranty"),
        country=request.json.get("country"),
        title=request.json.get("title"),
        year=request.json.get("year"),
        form_factor=request.json.get("form_factor"),
        width=request.json.get("width"),
        height=request.json.get("height"),
        socket=request.json.get("socket"),
        chipset=request.json.get("chipset"),
        built_in_cpu=request.json.get("built_in_cpu"),
        title_built_in_cpu=request.json.get("title_built_in_cpu"),
        memory_slots_amount=request.json.get("memory_slots_amount"),
        memory_type=request.json.get("memory_type"),
        ram_freq=request.json.get("ram_freq"),
        max_memory=request.json.get("max_memory"),
        memory_channels_amount=request.json.get("memory_channels_amount"),
        memory_form_factor=request.json.get("memory_form_factor"),
        m2_slots_amount=request.json.get("m2_slots_amount"),
        sata_slots_amount=request.json.get("sata_slots_amount"),
        nvme_support=request.json.get("nvme_support"),
        sata_raid_mode=request.json.get("sata_raid_mode"),
        m2_slots=request.json.get("m2_slots"),
        m2_form_factor=request.json.get("m2_form_factor"),
        other_drive_slots=request.json.get("other_drive_slots"),
        pci_express_version=request.json.get("pci_express_version"),
        pci_e_x1_slots_amount=request.json.get("pci_e_x1_slots_amount"),
        pci_e_x16_slots_amount=request.json.get("pci_e_x16_slots_amount"),
        sli_crossfire_support=request.json.get("sli_crossfire_support"),
        other_expansion_slots=request.json.get("other_expansion_slots"),
        video_outputs=request.json.get("video_outputs"),
        usb_amount_and_type=request.json.get("usb_amount_and_type"),
        digital_and_audio_ports_s_pdif=request.json.get("digital_and_audio_ports_s_pdif"),
        other_slots_on_back_panel=request.json.get("other_slots_on_back_panel"),
        network_ports_amount_rj45=request.json.get("network_ports_amount_rj45"),
        fan_4pin_connectors=request.json.get("fan_4pin_connectors"),
        internal_connectors_on_usb_plate_amount_and_type=request.json.get(
            "internal_connectors_on_usb_plate_amount_and_type"),
        cpu_cooler_power_slot=request.json.get("cpu_cooler_power_slot"),
        m2_e_key=request.json.get("m2_e_key"),
        lpt_interface=request.json.get("lpt_interface"),
        sound_adapter_chipset=request.json.get("sound_adapter_chipset"),
        sound_scheme=request.json.get("sound_scheme"),
        built_in_wifi_adapter=request.json.get("built_in_wifi_adapter"),
        bluetooth=request.json.get("bluetooth"),
        network_adapter_speed=request.json.get("network_adapter_speed"),
        network_adapter_chipset=request.json.get("network_adapter_chipset"),
        power_phases_amount=request.json.get("power_phases_amount"),
        cpu_power_slot=request.json.get("cpu_power_slot"),
        passive_cooling=request.json.get("passive_cooling"),
        main_power_slot=request.json.get("main_power_slot"),
        illumination=request.json.get("illumination"),
        description=request.json.get("description"),
        price=request.json.get("price"),
        rating=request.json.get("rating"),
        rates=request.json.get("rates"),
    )
    if mb.warranty:
        db_sess.query(Motherboard).filter(Motherboard.id == mb.id).update(values={Motherboard.warranty: mb.warranty})
    if mb.country:
        db_sess.query(Motherboard).filter(Motherboard.id == mb.id).update(values={Motherboard.country: mb.country})
    if mb.title:
        db_sess.query(Motherboard).filter(Motherboard.id == mb.id).update(values={Motherboard.title: mb.title})
    if mb.year:
        db_sess.query(Motherboard).filter(Motherboard.id == mb.id).update(values={Motherboard.year: mb.year})
    if mb.form_factor:
        db_sess.query(Motherboard).filter(Motherboard.id == mb.id).update(
            values={Motherboard.form_factor: mb.form_factor})
    if mb.width:
        db_sess.query(Motherboard).filter(Motherboard.id == mb.id).update(values={Motherboard.width: mb.width})
    if mb.height:
        db_sess.query(Motherboard).filter(Motherboard.id == mb.id).update(values={Motherboard.height: mb.height})
    if mb.socket:
        db_sess.query(Motherboard).filter(Motherboard.id == mb.id).update(values={Motherboard.socket: mb.socket})
    if mb.chipset:
        db_sess.query(Motherboard).filter(Motherboard.id == mb.id).update(values={Motherboard.chipset: mb.chipset})
    if mb.built_in_cpu:
        db_sess.query(Motherboard).filter(Motherboard.id == mb.id).update(
            values={Motherboard.built_in_cpu: mb.built_in_cpu})
    if mb.title_built_in_cpu:
        db_sess.query(Motherboard).filter(Motherboard.id == mb.id).update(
            values={Motherboard.title_built_in_cpu: mb.title_built_in_cpu})
    if mb.memory_slots_amount:
        db_sess.query(Motherboard).filter(Motherboard.id == mb.id).update(
            values={Motherboard.memory_slots_amount: mb.memory_slots_amount})
    if mb.memory_type:
        db_sess.query(Motherboard).filter(Motherboard.id == mb.id).update(
            values={Motherboard.memory_type: mb.memory_type})
    if mb.ram_freq:
        db_sess.query(Motherboard).filter(Motherboard.id == mb.id).update(values={Motherboard.ram_freq: mb.ram_freq})
    if mb.max_memory:
        db_sess.query(Motherboard).filter(Motherboard.id == mb.id).update(
            values={Motherboard.max_memory: mb.max_memory})
    if mb.memory_channels_amount:
        db_sess.query(Motherboard).filter(Motherboard.id == mb.id).update(
            values={Motherboard.memory_channels_amount: mb.memory_channels_amount})
    if mb.memory_form_factor:
        db_sess.query(Motherboard).filter(Motherboard.id == mb.id).update(
            values={Motherboard.memory_form_factor: mb.memory_form_factor})
    if mb.m2_slots_amount:
        db_sess.query(Motherboard).filter(Motherboard.id == mb.id).update(
            values={Motherboard.m2_slots_amount: mb.m2_slots_amount})
    if mb.sata_slots_amount:
        db_sess.query(Motherboard).filter(Motherboard.id == mb.id).update(
            values={Motherboard.sata_slots_amount: mb.sata_slots_amount})
    if mb.nvme_support:
        db_sess.query(Motherboard).filter(Motherboard.id == mb.id).update(
            values={Motherboard.nvme_support: mb.nvme_support})
    if mb.sata_raid_mode:
        db_sess.query(Motherboard).filter(Motherboard.id == mb.id).update(
            values={Motherboard.sata_raid_mode: mb.sata_raid_mode})
    if mb.m2_slots:
        db_sess.query(Motherboard).filter(Motherboard.id == mb.id).update(values={Motherboard.m2_slots: mb.m2_slots})
    if mb.m2_form_factor:
        db_sess.query(Motherboard).filter(Motherboard.id == mb.id).update(
            values={Motherboard.m2_form_factor: mb.m2_form_factor})
    if mb.other_drive_slots:
        db_sess.query(Motherboard).filter(Motherboard.id == mb.id).update(
            values={Motherboard.other_drive_slots: mb.other_drive_slots})
    if mb.pci_express_version:
        db_sess.query(Motherboard).filter(Motherboard.id == mb.id).update(
            values={Motherboard.pci_express_version: mb.pci_express_version})
    if mb.pci_e_x1_slots_amount:
        db_sess.query(Motherboard).filter(Motherboard.id == mb.id).update(
            values={Motherboard.pci_e_x1_slots_amount: mb.pci_e_x1_slots_amount})
    if mb.pci_e_x16_slots_amount:
        db_sess.query(Motherboard).filter(Motherboard.id == mb.id).update(
            values={Motherboard.pci_e_x16_slots_amount: mb.pci_e_x16_slots_amount})
    if mb.sli_crossfire_support:
        db_sess.query(Motherboard).filter(Motherboard.id == mb.id).update(
            values={Motherboard.sli_crossfire_support: mb.sli_crossfire_support})
    if mb.other_expansion_slots:
        db_sess.query(Motherboard).filter(Motherboard.id == mb.id).update(
            values={Motherboard.other_expansion_slots: mb.other_expansion_slots})
    if mb.video_outputs:
        db_sess.query(Motherboard).filter(Motherboard.id == mb.id).update(
            values={Motherboard.video_outputs: mb.video_outputs})
    if mb.usb_amount_and_type:
        db_sess.query(Motherboard).filter(Motherboard.id == mb.id).update(
            values={Motherboard.usb_amount_and_type: mb.usb_amount_and_type})
    if mb.digital_and_audio_ports_s_pdif:
        db_sess.query(Motherboard).filter(Motherboard.id == mb.id).update(
            values={Motherboard.digital_and_audio_ports_s_pdif: mb.digital_and_audio_ports_s_pdif})
    if mb.other_slots_on_back_panel:
        db_sess.query(Motherboard).filter(Motherboard.id == mb.id).update(
            values={Motherboard.other_slots_on_back_panel: mb.other_slots_on_back_panel})
    if mb.network_ports_amount_rj45:
        db_sess.query(Motherboard).filter(Motherboard.id == mb.id).update(
            values={Motherboard.network_ports_amount_rj45: mb.network_ports_amount_rj45})
    if mb.fan_4pin_connectors:
        db_sess.query(Motherboard).filter(Motherboard.id == mb.id).update(
            values={Motherboard.fan_4pin_connectors: mb.fan_4pin_connectors})
    if mb.internal_connectors_on_usb_plate_amount_and_type:
        db_sess.query(Motherboard).filter(Motherboard.id == mb.id).update(values={
            Motherboard.internal_connectors_on_usb_plate_amount_and_type: mb.internal_connectors_on_usb_plate_amount_and_type})
    if mb.cpu_cooler_power_slot:
        db_sess.query(Motherboard).filter(Motherboard.id == mb.id).update(
            values={Motherboard.cpu_cooler_power_slot: mb.cpu_cooler_power_slot})
    if mb.m2_e_key:
        db_sess.query(Motherboard).filter(Motherboard.id == mb.id).update(values={Motherboard.m2_e_key: mb.m2_e_key})
    if mb.lpt_interface:
        db_sess.query(Motherboard).filter(Motherboard.id == mb.id).update(
            values={Motherboard.lpt_interface: mb.lpt_interface})
    if mb.sound_adapter_chipset:
        db_sess.query(Motherboard).filter(Motherboard.id == mb.id).update(
            values={Motherboard.sound_adapter_chipset: mb.sound_adapter_chipset})
    if mb.sound_scheme:
        db_sess.query(Motherboard).filter(Motherboard.id == mb.id).update(
            values={Motherboard.sound_scheme: mb.sound_scheme})
    if mb.built_in_wifi_adapter:
        db_sess.query(Motherboard).filter(Motherboard.id == mb.id).update(
            values={Motherboard.built_in_wifi_adapter: mb.built_in_wifi_adapter})
    if mb.bluetooth:
        db_sess.query(Motherboard).filter(Motherboard.id == mb.id).update(values={Motherboard.bluetooth: mb.bluetooth})
    if mb.network_adapter_speed:
        db_sess.query(Motherboard).filter(Motherboard.id == mb.id).update(
            values={Motherboard.network_adapter_speed: mb.network_adapter_speed})
    if mb.network_adapter_chipset:
        db_sess.query(Motherboard).filter(Motherboard.id == mb.id).update(
            values={Motherboard.network_adapter_chipset: mb.network_adapter_chipset})
    if mb.power_phases_amount:
        db_sess.query(Motherboard).filter(Motherboard.id == mb.id).update(
            values={Motherboard.power_phases_amount: mb.power_phases_amount})
    if mb.cpu_power_slot:
        db_sess.query(Motherboard).filter(Motherboard.id == mb.id).update(
            values={Motherboard.cpu_power_slot: mb.cpu_power_slot})
    if mb.passive_cooling:
        db_sess.query(Motherboard).filter(Motherboard.id == mb.id).update(
            values={Motherboard.passive_cooling: mb.passive_cooling})
    if mb.main_power_slot:
        db_sess.query(Motherboard).filter(Motherboard.id == mb.id).update(
            values={Motherboard.main_power_slot: mb.main_power_slot})
    if mb.illumination:
        db_sess.query(Motherboard).filter(Motherboard.id == mb.id).update(
            values={Motherboard.illumination: mb.illumination})
    if mb.description:
        db_sess.query(Motherboard).filter(Motherboard.id == mb.id).update(
            values={Motherboard.description: mb.description})
    if mb.price:
        db_sess.query(Motherboard).filter(Motherboard.id == mb.id).update(values={Motherboard.price: mb.price})
    if mb.rating:
        db_sess.query(Motherboard).filter(Motherboard.id == mb.id).update(values={Motherboard.rating: mb.rating})
    if mb.rates:
        db_sess.query(Motherboard).filter(Motherboard.id == mb.id).update(values={Motherboard.rates: mb.rates})
    db_sess.commit()
    return flask.jsonify({'success': 'OK'})