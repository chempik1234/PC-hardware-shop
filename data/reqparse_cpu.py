from data import db_session
from data.__all_models import *
from flask import jsonify
from flask_restful import Resource, abort, reqparse
from werkzeug.security import generate_password_hash
parser = reqparse.RequestParser()
parser.add_argument("warranty", required=True, type=int)
parser.add_argument("country", required=True)
parser.add_argument("title", required=True)
parser.add_argument("generation", required=True)
parser.add_argument("year", required=True, type=int)
parser.add_argument("socket", required=True)
parser.add_argument("has_cooling", required=True, type=bool)
parser.add_argument("term_interface", required=True, type=bool)
parser.add_argument("cores", required=True, type=int)
parser.add_argument("threads", required=True, type=int)
parser.add_argument("tech_process", required=True, type=int)
parser.add_argument("core", required=True)
parser.add_argument("cash_l1_instructions_bits", required=True, type=int)
parser.add_argument("cash_l1_data_bits", required=True, type=int)
parser.add_argument("cash_l2_bits", required=True, type=int)
parser.add_argument("cash_l3_bits", required=True, type=int)
parser.add_argument("base_freq", required=True, type=int)
parser.add_argument("max_freq", required=True, type=int)
parser.add_argument("free_mult", required=True, type=bool)
parser.add_argument("memory", required=True)
parser.add_argument("max_mem_bits", required=True, type=int)
parser.add_argument("channels", required=True, type=int)
parser.add_argument("min_RAM_freq", required=True, type=int)
parser.add_argument("max_RAM_freq", required=True, type=int)
parser.add_argument("ECC", required=True, type=bool)
parser.add_argument("TDP", required=True, type=int)
parser.add_argument("custom_TDP", required=True, type=bool)
parser.add_argument("max_temp", required=True, type=int)
parser.add_argument("has_graphics", required=True, type=bool)
parser.add_argument("PCI", required=True)
parser.add_argument("PCI_amount", required=True, type=int)
parser.add_argument("bandwidth", required=True, type=float)
parser.add_argument("support_x64", required=True)
parser.add_argument("multi_thread", required=True, type=bool)
parser.add_argument("add_freq_tech", required=True)
parser.add_argument("energy_save_tech", required=True)
parser.add_argument("description", required=True)
parser.add_argument("price", required=True, type=int)
parser.add_argument("rating", required=True, type=int)
parser.add_argument("rates", required=True, type=int)


def abort_if_cpu_not_found(cpu_id):
    session = db_session.create_session()
    cpus = session.query(CPU).get(cpu_id)
    if not cpus:
        abort(404, message=f"CPU {cpu_id} not found")


def set_password(password):
    return generate_password_hash(password)


class CPUResource(Resource):
    def get(self, cpu_id):
        abort_if_cpu_not_found(cpu_id)
        session = db_session.create_session()
        cpu = session.query(CPU).get(cpu_id)
        return jsonify({'cpu': cpu.to_dict(
            only=('warranty', 'country', 'title',
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
                  'description', 'price', 'rating'))})

    def delete(self, cpu_id):
        abort_if_cpu_not_found(cpu_id)
        session = db_session.create_session()
        cpu = session.query(CPU).get(cpu_id)
        session.delete(cpu)
        session.commit()
        return jsonify({'success': 'OK'})


class CPUListResource(Resource):
    def get(self):
        session = db_session.create_session()
        cpu = session.query(CPU).all()
        return jsonify({'cpu': [item.to_dict(
            only=('warranty', 'country', 'title',
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
                  'description', 'price', 'rating')) for item in cpu]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        cpu = CPU(
            warranty=args['warranty'],
            country=args['country'],
            title=args['title'],
            generation=args['generation'],
            year=args['year'],
            socket=args['socket'],
            has_cooling=args['has_cooling'],
            term_interface=args['term_interface'],
            cores=args['cores'],
            threads=args['threads'],
            tech_process=args['tech_process'],
            core=args['core'],
            cash_l1_instructions_bits=args['cash_l1_instructions_bits'],
            cash_l1_data_bits=args['cash_l1_data_bits'],
            cash_l2_bits=args['cash_l2_bits'],
            cash_l3_bits=args['cash_l3_bits'],
            base_freq=args['base_freq'],
            max_freq=args['max_freq'],
            free_mult=args['free_mult'],
            memory=args['memory'],
            max_mem_bits=args['max_mem_bits'],
            channels=args['channels'],
            min_RAM_freq=args['min_RAM_freq'],
            max_RAM_freq=args['max_RAM_freq'],
            ECC=args['ECC'],
            TDP=args['TDP'],
            custom_TDP=args['custom_TDP'],
            max_temp=args['max_temp'],
            has_graphics=args['has_graphics'],
            PCI=args['PCI'],
            PCI_amount=args['PCI_amount'],
            bandwidth=args['bandwidth'],
            support_x64=args['support_x64'],
            multi_thread=args['multi_thread'],
            add_freq_tech=args['add_freq_tech'],
            energy_save_tech=args['energy_save_tech'],
            description=args['description'],
            price=args['price'],
            rating=args['rating']
        )
        session.add(cpu)
        session.commit()
        return jsonify({'success': 'OK'})
