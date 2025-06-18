from flask import Flask
from flask import render_template
app = Flask(__name__)
#from app import app
from flask import request
import requests as r


# DELETE "#" IN 23, 42, 51 (optional 49) WHILE USING PLATA WITH DUET!!!!

current_pl = '73'

def plata(cur_pl, fi):
    print("fi=", fi)
    co = fi[0]
    nu = fi[1::]
    print("nu=", nu)
    par = 0
    # print(co)
    # print()
    # print(nu)
    url = 'http://192.168.0.' + cur_pl
    urllas = 'http://192.168.14.56'
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
        co = 'q6'
        par = 1
    if (co=='h'):
        co='72'
        par= 2
    if (par == 1):
        par = 0
        r.get(iic + co + ':' + nu)
        print('sent:')
        #print()
        print(iic + co + ':' + nu)
    else:
        if (par==2):
            be = nu[0:2:]
            en = nu[2::]
            r.get(iic + co + ':' + be + ':' + en)
            print('sent:')
            # print()
            print(iic + co + ':' + be + ':' + en)
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
    user = {'nickname': 'Artyom'}
    return render_template("rentgen_new1.html",
        #title = 'Home',
        user = user)
#app.run(debug=True)

@app.route('/feedback', methods=['POST'])
def feedback():
    user_feedback = request.form.get('feedback')
#    print(user_feedback)
    global current_pl
    if((user_feedback == '213') or (user_feedback == '205') or (user_feedback == '104')):
        current_pl = user_feedback
        print("plata ip changed to")
        print(current_pl)
    else:
        plata(current_pl, user_feedback)

    return ': {user_feedback}'


@app.route('/command', methods=['POST'])
def send_command():
    user_command = request.form.get('command')
    global current_pl

#    print(user_command)
    plata(current_pl, user_command)
    if (user_command == ('hello there')):
        print('OBIVAN KENOBY!!!!!!')
#    return response
    return ': {user_feedback}'
app.run()

