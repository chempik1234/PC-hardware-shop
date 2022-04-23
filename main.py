import flask
from flask import Flask, flash, render_template, url_for, redirect, request, abort, make_response, send_from_directory
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, EmailField, FileField
from wtforms.validators import DataRequired, EqualTo
from random import randint
import os
import json
from data.reqparse_user import *
from data.reqparse_cpu import *
from data.reqparse_gpu import *
from data.reqparse_motherboard import *
from data.reqparse_ram_dimm import *
from data.reqparse_ram_so_dimm import *
from data.reqparse_ssd import *
from data import api_users
from data import api_cpu
from data import api_gpu
from data import api_motherboard
from data import api_ram_dimm
from data import api_ram_so_dimm
from data import api_ssd
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from sqlalchemy_serializer import *
import requests
from flask_restful import reqparse, abort, Api, Resource
from werkzeug.utils import secure_filename
app = Flask(__name__)
api = Api(app)
db = SQLAlchemy(app)
api.add_resource(UserListResource, '/api/v2/users')
api.add_resource(UserResource, '/api/v2/users/<int:user_id>')
api.add_resource(CPUListResource, '/api/v2/cpu')
api.add_resource(CPUResource, '/api/v2/cpu/<int:cpu_id>')
api.add_resource(GPUListResource, '/api/v2/gpu')
api.add_resource(GPUResource, '/api/v2/gpu/<int:gpu_id>')
api.add_resource(MotherboardListResource, '/api/v2/motherboard')
api.add_resource(MotherboardResource, '/api/v2/motherboard/<int:_id>')
api.add_resource(RAMDIMMListResource, '/api/v2/ram_dimm')
api.add_resource(RAMDIMMResource, '/api/v2/ram_dimm/<int:_id>')
api.add_resource(RAMSODIMMListResource, '/api/v2/ram_so_dimm')
api.add_resource(RAMSODIMMResource, '/api/v2/ram_so_dimm/<int:_id>')
api.add_resource(SSDListResource, '/api/v2/ssd')
api.add_resource(SSDResource, '/api/v2/ssd/<int:_id>')
UPLOAD_FOLDER = '/static/img/opinion'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'bmp'}
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
login_manager = LoginManager()
login_manager.init_app(app)


def x_or_y_if_a(a, x, y):
    if a is None:
        return None
    elif not a:
        return x
    else:
        return y


def byte(a):
    return a * 8


def KB(a):
    return byte(a * 1024)


def MB(a):
    return KB(a * 1024)


def GB(a):
    return MB(a * 1024)


def TB(a):
    return GB(a * 1024)


def net_string(a):
    return a if a else 'нет'


def net_yest(a):
    return 'есть' if a else 'нет'


def net_da(a):
    return 'да' if a else "нет"


def human_read_format(size):
    l, k = ['бит', 'Б', 'КБ', 'МБ', 'ГБ', 'ТБ'], 0
    if size > 8:
        size /= 8
        k += 1
        print(size, k)
    while size >= 1024:
        k += 1
        size /= 1024
        print(size, k)
    return str(round(size)) + l[k]


@app.errorhandler(404)
def not_found(error):
    return make_response(flask.jsonify({'error': '404'}), 404)


@app.route('/')
def index():
    url_style = url_for('static', filename='styles/style3.css')
    return render_template('index.html', title="Главная", style=url_style)


@app.route('/product/<product_type>')
def product_list(product_type):
    d = []
    types = {'cpu': ('Процессоры', CPU),
             'gpu': ('Видеокарты', GPU),
             'motherboard': ('Материнские платы', Motherboard),
             'ram_dimm': ('Оперативная память DIMM', RAM_DIMM),
             'ram_so_dimm': ('Оперативная память SO-DIMM', RAM_SO_DIMM),
             'ssd': ('SSD', SSD),
             'hdd35': ('HDD 3.5', HDD35)}
    if product_type not in types.keys():
        return abort(404)
    for item in db_sess.query(types[product_type][1]).all():
        d.append({'title': item.title,
                  'price': item.price,
                  'rating': round(item.rating / max(1, item.rates), 1)})
        d[-1]["id"] = item.id
    style = url_for('static', filename='/styles/style3.css')
    return render_template('list.html', style=style, title=types[product_type][0],
                           dictionary=d, type=product_type)


@app.route('/product/<pr_type>/<title>')
def product(pr_type, title):
    style = url_for('static', filename='/styles/style3.css')
    tables = {'cpu': CPU, 'gpu': GPU, 'motherboard': Motherboard,
              'ram_dimm': RAM_DIMM, 'ram_so_dimm': RAM_SO_DIMM,
              'ssd': SSD, 'hdd35': HDD35}
    item = db_sess.query(tables[pr_type]).filter(tables[pr_type].title == title).first()
    d = None
    if pr_type == 'cpu':
        d = {
            'Гарантия': str(item.warranty) + ' мес.',
            'Страна выпуска': item.country,
            'Модель': item.title,
            'Поколение': item.generation,
            'Год выпуска': item.year,
            'Сокет': item.socket,
            'Система охлаждения': net_yest(item.has_cooling),
            'Термоинтерфейс': net_yest(item.term_interface),
            'Количество ядер': item.cores,
            'Максимальное количество потоков': item.threads,
            'Техпроцесс': str(item.tech_process) + ' нм',
            'Ядро': item.core,
            'Кэш L1 (инструкции)': human_read_format(item.cash_l1_instructions_bits),
            'Кэш L1 (данные)': human_read_format(item.cash_l1_data_bits),
            'Кэш L2': human_read_format(item.cash_l2_bits),
            'Кэш L3': human_read_format(item.cash_l3_bits),
            'Частота': str(item.base_freq) + ' ГГц',
            'Макс. частота': str(item.max_freq) + ' ГГц',
            'Свободный множитель': item.free_mult,
            'Тип памяти': item.memory,
            'Макс. объём памяти': human_read_format(item.max_mem_bits),
            'Каналы': item.channels,
            'минимальная частота ОЗУ': str(item.min_RAM_freq) + ' МГц',
            'максимальная частота ОЗУ': str(item.max_RAM_freq) + ' МГц',
            'ECC': net_yest(item.ECC),
            'TDP': str(item.TDP) + ' Вт',
            'Настраиваемая величина TDP': net_yest(item.custom_TDP),
            'Максимальная температура': str(item.max_temp) + '°',
            'Встроенное графическое ядро': net_yest(item.has_graphics),
            'PCI': item.PCI,
            'Число линий PCI Express': item.PCI_amount,
            'Пропускная способность шины': item.bandwidth,
            'Поддержка 64-битного набора команд': item.support_x64,
            'Многопоточность': net_yest(item.multi_thread),
            'Технология повышения частоты процессора': item.add_freq_tech,
            'Технология энергосбережения': item.energy_save_tech,
            'Описание': item.description,
            'Цена': item.price,
            'Оценка': round(item.rating / max(1, item.rates), 1),
            'rates': item.rates
        }
    elif pr_type == 'gpu':
        d = {'Гарантия': str(item.warranty) + ' мес.',
             'Страна выпуска': item.country,
             'Название': item.title,
             'Год выпуска': item.year,
             'Код производителя': item.manufacturer_code,
             'Для майнинга': net_da(item.is_for_mining),
             'LHR': net_da(item.LHR),
             'Объём видеопамяти': human_read_format(item.memory),
             'Тип памяти': item.memory_type,
             'Пропускная способность памяти на один контакт': str(item.bandwidth) + ' Гбит/c',
             'Разрядность шины памяти': str(item.band_64x_32x) + ' бит',
             'Максимальная пропускная способность памяти': str(item.max_mem_bandwidth) + ' Гбайт/c',
             'Микроархитектура': item.micro_arc,
             'Кодовое название графического процессора ': item.graph_cpu,
             'Техпроцесс': str(item.techprocess) + 'нм',
             'Штатная частота работы видеочипа': str(item.chip_freq) + " МГц",
             'Количество универсальных процессоров (ALU)': item.ALU,
             'Число текстурных блоков': item.texture_blocks,
             'Число блоков растеризации ': item.raster_blocks,
             'Максимальная температура процессора': item.max_temp,
             'Поддержка трассировки лучей': net_yest(item.RTX),
             'Аппаратное ускорение трассировки лучей (RT-ядра)': net_yest(item.appart_accelerate_RT),
             'Тензорные ядра': item.tenz_cores,
             'Пиковая производительность чипов в FP32': str(item.max_efficiency_FP32) + ' GFLOPS',
             'Видеоразъемы': item.connectors,
             'Версия HDMI': item.HDMI_version,
             'Максимальное разрешение': item.max_resolution,
             'Количество подключаемых одновременно мониторов': item.max_monitors,
             'Интерфейс подключения': item.connection_interface,
             'Версия PCI Express': item.PCI_version,
             'Поддержка мультипроцессорной конфигурации': net_yest(item.support_mult_cpu_config),
             'Необходимость дополнительного питания': net_yest(item.need_extra_power),
             'Разъемы дополнительного питания': net_yest(item.extra_power_connections),
             'Максимальное энергопотребление': item.max_consuming_power,
             'Рекомендуемый блок питания': item.recommended_power,
             'Тип охлаждения': item.cooling,
             'Тип и количество установленных вентиляторов': item.type_and_amount_fans,
             'Управление скоростью вращения': net_yest(item.fan_speed_control),
             'Низкопрофильная карта (Low Profile)': net_da(item.low_profile),
             'Количество занимаемых слотов расширения': item.needed_slots,
             'Длина видеокарты': item.length,
             'Толщина видеокарты': item.width,
             'Вес': item.weight,
             'Подсветка элементов видеокарты': net_yest(item.illumination),
             'Синхронизация RGB подсветки': net_yest(item.synch_RGB),
             'LCD дисплей': net_yest(item.LCD),
             'Переключатель BIOS': net_yest(item.BIOS_switch),
             'Описание': item.description,
             'Цена': item.price,
             'Оценка': round(item.rating / max(1, item.rates), 1),
             'rates': item.rates,
        }
    elif pr_type == 'motherboard':
        d = {'Гарантия': str(item.warranty) + ' мес.',
             'Страна выпуска': item.country,
             'Название': item.title,
             'Год выпуска': item.year,
             'Форм-фактор': item.form_factor,
             'Ширина': item.width,
             'Высота': item.height,
             'Сокет': item.socket,
             'Чипсет': item.chipset,
             'Встроенный центральный процессор': net_yest(item.built_in_cpu),
             'Модель встроенного центрального процессора': item.title_built_in_cpu,
             'Количество слотов памяти': item.memory_slots_amount,
             'Тип памяти': item.memory_type,
             'Частота оперативной памяти': item.ram_freq,
             'Максимальный объём памяти': human_read_format(item.max_memory),
             'Количество каналов памяти': item.memory_channels_amount,
             'Форм фактор поддерживаемой памяти': item.memory_form_factor,
             'Количество слотов M2': item.m2_slots_amount,
             'Количество слотов SATA': item.sata_slots_amount,
             'Поддержка NVMe': net_yest(item.nvme_support),
             'Режим работы SATA RAID': item.sata_raid_mode,
             'Разъёмы M2': net_string(item.m2_slots),
             'Форм-фактор M2': item.m2_form_factor,
             'Другие разъёмы накопителей': net_string(item.other_drive_slots),
             'Версия PCI Express': item.pci_express_version,
             'Количество слотов PCI-E x1': item.pci_e_x1_slots_amount,
             'Количество слотов PCI-E x16': item.pci_e_x16_slots_amount,
             'Поддержка SLI/CrossFire': net_yest(item.sli_crossfire_support),
             'Другие слоты расширения': item.other_expansion_slots,
             'Видеовыходы': item.video_outputs,
             'Количество и тип USB на задней панели': item.usb_amount_and_type,
             'Цифровые аудио порты (S/PDIF)': item.digital_and_audio_ports_s_pdif,
             'Другие разъемы на задней панели': item.other_slots_on_back_panel,
             'Количество сетевых портов (RJ-45)': item.network_ports_amount_rj45,
             '4-Pin PWM коннекторы для вентиляторов': item.fan_4pin_connectors,
             'Внутренние коннекторы USB на плате': item.internal_connectors_on_usb_plate_amount_and_type,
             'Разъем питания процессорного кулера': item.cpu_cooler_power_slot,
             'M.2 ключ E': net_yest(item.m2_e_key),
             'Интерфейс LPT': net_yest(item.lpt_interface),
             'Чипсет звукового адаптера': 'sound_adapter_chipset',
             'Звуковая схема': item.sound_scheme,
             'Встроенный адаптер Wi-Fi': item.built_in_wifi_adapter,
             'Bluetooth': net_string(item.bluetooth),
             'Скорость сетевого адаптера': item.network_adapter_speed,
             'Чипсет сетевого адаптера': item.network_adapter_chipset,
             'Количество фаз питания': item.power_phases_amount,
             'Разъем питания процессора': item.cpu_power_slot,
             'Пассивное охлаждение': item.passive_cooling,
             'Основной разъем питания': item.main_power_slot,
             'Подсветка элементов платы': net_yest(item.illumination),
             'Описание': item.description,
             'Цена': item.price,
             'Оценка': round(item.rating / max(1, item.rates), 1),
             'rates': item.rates,
        }
    elif pr_type == 'ram_dimm':
        d = {'Гарантия': str(item.warranty) + ' мес.',
             'Страна выпуска': item.country,
             'Название': item.title,
             'Год выпуска': item.year,
             'Тип': item.common_type,
             'Тип памяти': item.type_ddr,
             'Ранговость': item.rang,
             'Регистровая память': net_da(item.register_memory),
             'ECC-память': net_yest(item.ecc_memory),
             'Память одного модуля': human_read_format(item.one_module_memory),
             'Суммарный объем памяти всего комплекта': human_read_format(GB(item.all_memory)),
             'Количество модулей в комплекте': item.modules_amount,
             'Тактовая частота': str(item.freq) + ' МГц',
             'CAS Latency (CL)': item.cas_latency_cl,
             'RAS to CAS Delay (tRCD)': item.ras_to_cas_delay_trcd,
             'Row Precharge Delay (tRP)': item.row_precharge_delay_trp,
             'Наличие радиатора': net_yest(item.has_radiator),
             'Высота': str(item.height) + ' мм',
             'Низкопрофильная (Low Profile)': net_da(item.low_profile),
             'Напряжение питания': str(item.power_voltage) + ' В',
             'Подсветка элементов платы': net_yest(item.illumination),
             'Цвет радиатора': item.radiator_color,
             'Описание': item.description,
             'Цена': item.price,
             'Оценка': round(item.rating / max(1, item.rates), 1),
             'rates': item.rates,
             }
    elif pr_type == 'ram_so_dimm':
        d = {'Гарантия': str(item.warranty) + ' мес.',
             'Страна выпуска': item.country,
             'Название': item.title,
             'Тип': item.common_type,
             'Тип памяти': item.type_ddr,
             'Память одного модуля': human_read_format(item.one_module_memory),
             'Суммарный объем памяти всего комплекта': human_read_format(item.all_memory),
             'Количество модулей в комплекте': item.modules_amount,
             'Частота': str(item.freq) + ' МГц',
             'CAS Latency (CL)': item.cas_latency_cl,
             'RAS to CAS Delay (tRCD)': item.ras_to_cas_delay_trcd,
             'Row Precharge Delay (tRP)': item.row_precharge_delay_trp,
             'Количество чипов модуля': item.chips_amount,
             'Двухсторонняя установка чипов': net_yest(item.double_sided_chips_setup),
             'Напряжение питания': str(item.power_voltage) + ' В',
             'Описание': item.description,
             'Цена': item.price,
             'Оценка': round(item.rating / max(1, item.rates), 1),
             'rates': item.rates,
             }
    elif pr_type == 'ssd':
        d = {
            'Гарантия': str(item.warranty) + ' мес.',
            'Название': item.title,
            'Тип': item.ssd_type,
            'Объём памяти (ГБ)': item.memory,
            'Физический интерфейс': item.phys_interface,
            'Количество бит на ячейку': item.bit_per_cell_amount,
            'Структура памяти': item.memory_structure,
            'DRAM буфер': net_yest(item.DRAM_buffer),
            'Максимальная скорость последовательного чтения': str(item.max_cons_reading_speed) + 'Мбайт/сек',
            'Максимальная скорость последовательной записи': str(item.max_cons_writing_speed) + 'Мбайт/сек',
            'Максимальный ресурс записи (TBW)': str(item.max_writing_resource_TBW) + 'ТБ',
            'DWPD': item.DWPD,
            'Аппаратное шифрование данных': net_yest(item.hardware_data_encryption),
            'Толщина (мм)': item.width,
            'Форм-фактор': x_or_y_if_a(item.form_factor, 'mSATA', '2.5"'),
            'Описание': item.description,
            'Цена': item.price,
            'Оценка': round(item.rating / max(1, item.rates), 1),
            'rates': item.rates,
        }
    elif pr_type == 'hdd35':
        d = {
            'Гарантия': str(item.warranty) + ' мес.',
            'Название': item.title,
            'Объём памяти': human_read_format(item.memory_bits),
            'Скорость вращения': str(item.rotation_speed) + ' об/мин',
            'Объём кэш-памяти': human_read_format(item.cash_memory_bits),
            'Оптимизация под RAID-массивы': net_yest(item.raid_massives_optimization),
            'С гелиевым наполнением': net_yest(item.helium_fill),
            'Уровень шума во время работы': str(item.noise_dba) + ' дБа',
            'Технология записи': x_or_y_if_a(item.writing_tech_CMR_SMR, 'CMR', 'SMR'),
            'Число циклов позиционирования-парковки': item.position_park_cycles_amount,
            'Ширина': str(item.width) + ' мм',
            'Длина': str(item.length) + ' мм',
            'Высота': str(item.height) + ' мм',
            'Описание': item.description,
            'Цена': item.price,
            'Оценка': round(item.rating / max(1, item.rates), 1),
            'rates': item.rates,
        }
    opinions_db = db_sess.query(Opinion).filter(Opinion.pr_type == pr_type, Opinion.pr_title == title)
    opinions = []
    for i in opinions_db:
        user = db_sess.query(User).get(i.user_id)
        opinions.append([user.surname + ' ' + user.name, i.text, i.image])
    if not opinions:
        opinions = None
    if not d:
        return abort(404)
    return render_template('product.html', style=style, title=title,
                           item=d, product_type=pr_type, keys=d.keys(),
                           opinions=opinions)


@app.route('/product/<pr_type>/<title>/<rate>')
def leave_rate(pr_type, title, rate):
    types = {'cpu': CPU, 'gpu': GPU, 'motherboard': Motherboard,
             'ram_dimm': RAM_DIMM, 'ram_so_dimm': RAM_SO_DIMM,
             'ssd': SSD, 'hdd35': HDD35}
    table = types[pr_type]
    item = db_sess.query(table).filter(table.title == title).first()
    if item:
        item.rates += 1
        item.rating += int(rate)
    db_sess.commit()
    return redirect(f'/product/{pr_type}/{title}')


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/uploads/<name>')
def download_file(name):
    return send_from_directory(app.config["UPLOAD_FOLDER"], name)


@app.route('/product/add_opinion/<pr_type>/<title>', methods=['GET', 'POST'])
def add_opinion(pr_type, title):
    if not current_user.is_authenticated:
        return redirect('/login')
    if db_sess.query(Opinion).filter(Opinion.pr_type == pr_type, Opinion.pr_title == title,
                                     Opinion.user_id == current_user.id).first():
        flash('Вы уже оставили отзыв')
        return redirect('/product/' + pr_type + '/' + title)
    url_style = url_for('static', filename='styles/style3.css')
    if request.method == 'POST':
        print(request.form, request.files)
        op = Opinion()
        op.user_id = current_user.id
        op.text = request.form['text']
        op.pr_type = pr_type
        op.pr_title = title
        file = request.files['file']
        if file and allowed_file(file.filename):
            # filename = secure_filename(file.filename)
            filename = '1.png'
            quer = db_sess.query(Opinion).all()
            if quer:
                filename = str(max([i.id for i in quer])) + '.png'
            file.filename = filename
            file.save(os.path.abspath(os.getcwd()) + os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print(file.filename)
            op.image = file.filename
        db_sess.add(op)
        db_sess.commit()
        return redirect('/product/' + pr_type + '/' + title)
    return render_template('opinion.html', style=url_style,
                           title=title, product_type=pr_type)


@app.route('/profile')
def profile():
    style = url_for('static', filename='/styles/style3.css')
    if current_user.is_authenticated:
        return render_template('profile.html', style=style, title="Профиль")
    else:
        return redirect('/login')


class OpinionForm(FlaskForm):
    text = StringField("Текст", validators=[DataRequired()])
    images = FileField("Фото",)
    submit = SubmitField('Отправить')


class DBLoginForm(FlaskForm):
    surname = StringField("Фамилия", validators=[DataRequired()])
    name = StringField("Имя", validators=[DataRequired()])
    email = EmailField("Логин / Почта", validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    repeat_password = PasswordField('Повторите пароль',
                                    validators=[DataRequired(),
                                                EqualTo('password', message='Passwords must match')])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class SignInForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


@app.route('/product/buy/<pr_type>/<title>')
def product_buy(pr_type, title):
    tables = {'cpu': CPU, 'gpu': GPU, 'motherboard': Motherboard}
    item = db_sess.query(tables[pr_type]).filter(tables[pr_type].title == title).first()
    price = item.price
    json_ = {
        "caption": "Покупка товара",
        "description": "Название: " + title,
        "meta": title + pr_type + str(randint(100000, 999999)),
        "autoclear": True,
        "items": [
            {
                "name": title,
                "price": str(price),
                "nds": "nds_10",
                "currency": "RUB",
                "amount": 1,
                "image": {
                    "url": url_for('static', filename='/img/' + pr_type + '/' + title + '.jpg')
              }
            }
          ],
        "mode": "test",
        "return_url": "/product/" + pr_type
        }
    requests.post('https://pay-sdk.yandex.net/v1', json=json_)
    return index()


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = DBLoginForm()
    url_style = url_for('static', filename='styles/style3.css')
    if form.validate_on_submit():
        user = User()
        user.surname = form.surname.data
        user.name = form.name.data
        user.email = form.email.data
        user.hashed_password = form.password.data
        db_sess.add(user)
        db_sess.commit()
        return redirect('/success')
    return render_template('login.html', style=url_style,
                           header='<h2 style="color: white;">Регистрация</h2>',
                           title='Авторизация', form=form)


@app.route('/login', methods=['GET', 'POST'])
def sign_in():
    form = SignInForm()
    url_style = url_for('static', filename='styles/style3.css')
    if form.validate_on_submit():
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/success")
        return render_template('sign_in.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('sign_in.html', title='Авторизация', form=form, style=url_style)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/success')
def success():
    return redirect('/')


def db_main():
    cpu_amount = 1
    warranty = {'AMD FX-4300': 12}
    country = {'AMD FX-4300': 'Малайзия'}
    title = ['AMD FX-4300']
    generation = {'AMD FX-4300': 'AMD FX'}
    year = {'AMD FX-4300': 2012}
    socket = {'AMD FX-4300': 'AM3+'}
    has_cooling = {'AMD FX-4300': False}
    term_interface = {'AMD FX-4300': False}
    cores = {'AMD FX-4300': 4}
    threads = {'AMD FX-4300': 4}
    tech_process = {'AMD FX-4300': 32}
    core = {'AMD FX-4300': 'Vishera'}
    cash_l1_instructions_bits = {'AMD FX-4300': KB(128)}
    cash_l1_data_bits = {'AMD FX-4300': KB(64)}
    cash_l2_bits = {'AMD FX-4300': MB(4)}
    cash_l3_bits = {'AMD FX-4300': MB(4)}
    base_freq = {'AMD FX-4300': 3.8}
    max_freq = {'AMD FX-4300': 4}
    free_mult = {'AMD FX-4300': True}
    memory = {'AMD FX-4300': 'DDR3'}
    max_mem_bits = {'AMD FX-4300': GB(128)}
    channels = {'AMD FX-4300': 2}
    min_RAM_freq = {'AMD FX-4300': 800}
    max_RAM_freq = {'AMD FX-4300': 1866}
    ECC = {'AMD FX-4300': False}
    TDP = {'AMD FX-4300': 95}
    custom_TDP = {'AMD FX-4300': False}
    max_temp = {'AMD FX-4300': 0}
    has_graphics = {'AMD FX-4300': False}
    PCI = {'AMD FX-4300': 'No'}
    PCI_amount = {'AMD FX-4300': 0}
    bandwidth = {'AMD FX-4300': 5.2}
    support_x64 = {'AMD FX-4300': 'AMD64'}
    multi_thread = {'AMD FX-4300': False}
    add_freq_tech = {'AMD FX-4300': 'No'}
    energy_save_tech = {'AMD FX-4300': 'PowerNow!'}
    description = {'AMD FX-4300': '''Четырехъядерный «народный процессор» AMD FX-4300 OEM, способный работать в четыре потока, позволяет насладиться преимуществами параллельных вычислений в полном объеме. Представитель линейки Vishera AMD FX-4300 OEM гармонично впишется в вашу игровую систему.
3.8 ГГц — номинальная тактовая частота модели, однако чип из серии Black Edition AMD FX-4300 OEM, благодаря открытому множителю и технологии AMD Turbo Core 3.0, способен работать и на частоте 4 ГГц.
Общий объем кэша 8 МБ гарантирует работу процессора AMD FX-4300 OEM на полную мощность, Socket AM3+ делает его совместимым с большинством системных плат, а двухканальный контроллер ОЗУ добавляет поддержку памяти до 1866 МГц частотой и до 128 ГБ объемом.
Вы также останетесь удовлетворены широкой поддержкой наборов команд и технологий — в процессор AMD FX-4300 OEM внедрена поддержка виртуализации, технология экономии энергии, широкий спектр наборов инструкций, в частности, SSE вплоть до 4.2, FMA3, EVP, MMX, XOP и другие.'''}
    price = {'AMD FX-4300': 3299}
    rating = {'AMD FX-4300': 0}
    rates = {'AMD FX-4300': 0}
    for i in range(cpu_amount):
        cpu = CPU()
        ii = title[i]
        cpu.warranty = warranty[ii]
        cpu.country = country[ii]
        cpu.title = ii
        cpu.generation = generation[ii]
        cpu.year = year[ii]
        cpu.socket = socket[ii]
        cpu.has_cooling = has_cooling[ii]
        cpu.term_interface = term_interface[ii]
        cpu.cores = cores[ii]
        cpu.threads = threads[ii]
        cpu.tech_process = tech_process[ii]
        cpu.core = core[ii]
        cpu.cash_l1_instructions_bits = cash_l1_instructions_bits[ii]
        cpu.cash_l1_data_bits = cash_l1_data_bits[ii]
        cpu.cash_l2_bits = cash_l2_bits[ii]
        cpu.cash_l3_bits = cash_l3_bits[ii]
        cpu.base_freq = base_freq[ii]
        cpu.max_freq = max_freq[ii]
        cpu.free_mult = free_mult[ii]
        cpu.memory = memory[ii]
        cpu.max_mem_bits = max_mem_bits[ii]
        cpu.channels = channels[ii]
        cpu.min_RAM_freq = min_RAM_freq[ii]
        cpu.max_RAM_freq = max_RAM_freq[ii]
        cpu.ECC = ECC[ii]
        cpu.TDP = TDP[ii]
        cpu.custom_TDP = custom_TDP[ii]
        cpu.max_temp = max_temp[ii]
        cpu.has_graphics = has_graphics[ii]
        cpu.PCI = PCI[ii]
        cpu.PCI_amount = PCI_amount[ii]
        cpu.bandwidth = bandwidth[ii]
        cpu.support_x64 = support_x64[ii]
        cpu.multi_thread = multi_thread[ii]
        cpu.add_freq_tech = add_freq_tech[ii]
        cpu.energy_save_tech = energy_save_tech[ii]
        cpu.description = description[ii]
        cpu.price = price[ii]
        cpu.rating = rating[ii]
        cpu.rates = rates[ii]
        db_sess.add(cpu)
    db_sess.commit()


@login_manager.user_loader
def load_user(user_id):
    return db_sess.query(User).get(user_id)


app.register_blueprint(api_users.blueprint)
app.register_blueprint(api_cpu.blueprint)
app.register_blueprint(api_gpu.blueprint)
app.register_blueprint(api_motherboard.blueprint)
app.register_blueprint(api_ram_dimm.blueprint)
app.register_blueprint(api_ram_so_dimm.blueprint)
app.register_blueprint(api_ssd.blueprint)
PATH = os.path.abspath(os.getcwd())
needtofill = os.path.isfile(PATH + '\\db\\e_shop.db')
db_session.global_init("db/e_shop.db")
db_sess = db_session.create_session()
# if not needtofill:
#     db_main()
db.create_all()
if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')