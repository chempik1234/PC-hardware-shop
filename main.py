import flask
from flask import Flask, render_template, url_for, redirect, request, abort, make_response
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, EmailField
from wtforms.validators import DataRequired, EqualTo
from random import randint
import os
import json
from data.api import blueprint
from data.reqparse_cpu import *
from data.reqparse_user import *
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from sqlalchemy_serializer import *
import requests
from flask_restful import reqparse, abort, Api, Resource
app = Flask(__name__)
api = Api(app)
db = SQLAlchemy(app)
api.add_resource(UserListResource, '/api/v2/users')
api.add_resource(UserResource, '/api/v2/users/<int:user_id>')
api.add_resource(CPUListResource, '/api/v2/cpu')
api.add_resource(CPUResource, '/api/v2/cpu/<int:cpu_id>')
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)
levels = {}


def net_yest(a):
    return 'есть' if a else 'нет'


def net_da(a):
    return 'да' if a else "нет"


def human_read_format(size):
    l, k = ['бит', 'Б', 'КБ', 'МБ', 'ГБ', 'ТБ'], 0
    if size > 8:
        size /= 8
        k += 1
    while size >= 1024:
        k += 1
        size /= 1024
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
             'gpu': ('Видеокарты', GPU)}
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
    tables = {'cpu': CPU, 'gpu': GPU}
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
        print(item.max_efficiency_FP32)
        d = {'Гарантия': item.warranty,
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
    if not d:
        return abort(404)
    return render_template('product.html', style=style, title=title,
                           item=d, product_type=pr_type, keys=d.keys())


@app.route('/product/<pr_type>/<title>/<rate>')
def leave_rate(pr_type, title, rate):
    types = {'cpu': CPU, 'gpu': GPU}
    table = types[pr_type]
    item = db_sess.query(table).filter(table.title == title).first()
    if item:
        item.rates += 1
        item.rating += int(rate)
    db_sess.commit()
    return redirect(f'/product/{pr_type}/{title}')


@app.route('/profile')
def profile():
    style = url_for('static', filename='/styles/style3.css')
    if current_user.is_authenticated:
        return render_template('profile.html', style=style, title="Профиль")
    else:
        return redirect('/login')


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


@app.route('/register', methods=['GET','POST'])
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
        db_sess = db_session.create_session()
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


if __name__ == '__main__':
    app.register_blueprint(blueprint)
    PATH = os.path.abspath(os.getcwd())
    needtofill = os.path.isfile(PATH + '\\db\\e_shop.db')
    db_session.global_init("db/e_shop.db")
    db_sess = db_session.create_session()
    if not needtofill:
        db_main()
    db.create_all()
    app.run(port=8080, host='127.0.0.1')