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
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from sqlalchemy_serializer import *
import requests
from flask_restful import reqparse, abort, Api, Resource
app = Flask(__name__)
api = Api(app)
api.add_resource(UserListResource, '/api/v2/users')
api.add_resource(UserResource, '/api/v2/users/<int:user_id>')
api.add_resource(CPUListResource, '/api/v2/cpu')
api.add_resource(CPUResource, '/api/v2/cpu/<int:cpu_id>')
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)
levels = {}


@app.errorhandler(404)
def not_found(error):
    return make_response(flask.jsonify({'error': '404'}), 404)


@app.route('/')
def index():
    url_style = url_for('static', filename='styles/style3.css')
    return render_template('index.html', title="Главная", style=url_style)


@app.route('/cpu')
def works_list():
    d = []
    for cpu in db_sess.query(CPU).all():
        d.append({'title': cpu.title,
                  'price': cpu.price,
                  'rating': cpu.rating})
        d[-1]["id"] = cpu.id
    style = url_for('static', filename='/styles/style3.css')
    return render_template('list.html', style=style, title='Процессоры',
                           dictionary=d)


class DBLoginForm(FlaskForm):
    surname = StringField("Surname", validators=[DataRequired()])
    name = StringField("Name", validators=[DataRequired()])
    email = EmailField("Login / Email", validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    repeat_password = PasswordField('Repeat password',
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
                           header='<h2>Register form</h2>',
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
    description = {'AMD FX-4300': ''''Четырехъядерный «народный процессор» AMD FX-4300 OEM, способный работать в четыре потока, позволяет насладиться преимуществами параллельных вычислений в полном объеме. Представитель линейки Vishera AMD FX-4300 OEM гармонично впишется в вашу игровую систему.
3.8 ГГц — номинальная тактовая частота модели, однако чип из серии Black Edition AMD FX-4300 OEM, благодаря открытому множителю и технологии AMD Turbo Core 3.0, способен работать и на частоте 4 ГГц.
Общий объем кэша 8 МБ гарантирует работу процессора AMD FX-4300 OEM на полную мощность, Socket AM3+ делает его совместимым с большинством системных плат, а двухканальный контроллер ОЗУ добавляет поддержку памяти до 1866 МГц частотой и до 128 ГБ объемом.
Вы также останетесь удовлетворены широкой поддержкой наборов команд и технологий — в процессор AMD FX-4300 OEM внедрена поддержка виртуализации, технология экономии энергии, широкий спектр наборов инструкций, в частности, SSE вплоть до 4.2, FMA3, EVP, MMX, XOP и другие.'''}
    price = {'AMD FX-4300': 3299}
    rating = {'AMD FX-4300': 0}
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
    app.run(port=8080, host='127.0.0.1')