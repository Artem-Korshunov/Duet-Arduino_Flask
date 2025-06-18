from flask import Flask
from flask import render_template
app = Flask(__name__)
#from app import app
from flask import request
import requests as r


# DELETE "#" IN 23, 42, 51 (optional 49) WHILE USING PLATA WITH DUET!!!!

current_pl = '100'

def plata(cur_pl, fi):
    co = fi[0]
    nu = fi[1]
    par = 0
    # print(co)
    # print()
    # print(nu)
    url = 'http://192.168.15.' + cur_pl
# следующей строчкой попытался учесть, что лазером управляет всегда одна плата
    urllas = 'http://192.168.15.73'
    s = r.get(url)
    # move=url+'/rr_gcode?gcode=G1'
    urlg = url + '/rr_gcode?gcode='
    urlglas = urllas + '/rr_gcode?gcode='
    iic = urlglas + 'M260A8B'
    if (co == 's'):
        co = '83'
        par = 1
    if (co == 'p'):
        co = '80'
        par = 1
    if (co == 'k'):
        co = '75'
        par = 1
    if (co == 'l'):
        co = '76'
        par = 1
    if (par == 1):
        par = 0
        r.get(iic + co + ':' + nu)
        print('sent:')
        print()
        print(iic + co + ':' + nu)
    else:
#        if (fi != '00'):
        print('sent:')
#            print()
        print(urlg + fi)
        r.get(urlg + fi)
    return 0

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Artyom'}# выдуманный пользователь
    return render_template("chat2.html",
        #title = 'Home',
        user = user)
#app.run(debug=True)

@app.route('/feedback', methods=['POST'])
def feedback():
    user_feedback = request.form.get('feedback')
#    print(user_feedback)
    global current_pl
    if((user_feedback == '201') or (user_feedback == '101') or (user_feedback == '301')):
        current_pl = user_feedback
        print("plata ip changed to")
        print(current_pl)
    else:
        plata(current_pl, user_feedback)
    return 'Отправлено: {user_feedback}'


@app.route('/command', methods=['POST'])
def send_command():
    user_command = request.form.get('command')
    global current_pl
    # Здесь можно выполнить обработку команды и отправить ответ
#    response = f'Вы отправили команду: {user_command}'
#    print(user_command)
    plata(current_pl, user_command)
    if (user_command == ('hello there')):
        print('OBIVAN KENOBY!!!!!!')
#    return response
    return 'Отправлено: {user_command}'
app.run()

