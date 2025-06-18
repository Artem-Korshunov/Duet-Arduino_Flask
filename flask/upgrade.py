from flask import Flask
from flask import render_template
app = Flask(__name__)
#from app import app
from flask import request
import requests as r
import subprocess


# DELETE "#" IN 23, 42, 51 (optional 49) WHILE USING PLATA WITH DUET!!!!


def plata(f):
    cur_pl=''
    fi=''
    par=0
    for i in f:
        if i=='&':
            par=1
            continue
        if par==1:
            fi=fi+i
        if par==0:
            cur_pl=cur_pl+i

    # print(co)
    # print()
    # print(nu)
    url = 'http://192.168.0.' + cur_pl
#    s = r.get(url)
    # move=url+'/rr_gcode?gcode=G1'
    urlg = url + '/rr_gcode?gcode='

#        if (fi != '00'):
    print('sent:')
#            print()
    print(urlg + fi)
    print(r.get(urlg + fi))
#    resp=r.get(url, 'M114')
#    print(resp.text)
    return 0



@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Artyom'}# выдуманный пользователь
    return render_template("rentgen_ult5.html",
        #title = 'Home',
        user = user)
#app.run(debug=True)

@app.route('/feedback', methods=['POST'])
def feedback():
    user_feedback = request.form.get('feedback')
#    print(user_feedback)
    plata(user_feedback)
    return f'Отправлено: {user_feedback}'


@app.route('/command', methods=['POST'])
def send_command():
    user_command = request.form.get('command')

    # Здесь можно выполнить обработку команды и отправить ответ
#    response = f'Вы отправили команду: {user_command}'
#    print(user_command)
    plata(user_command)
    if (user_command == ('hello there')):
        print('OBIVAN KENOBY!!!!!!')
#    return response
    return f'Отправлено: {user_command}'
app.run()

