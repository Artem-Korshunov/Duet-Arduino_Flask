from flask import Flask
from flask import render_template
app = Flask(__name__)
#from app import app
from flask import request
import requests as r


# DELETE "#" IN 23, 42, 51 (optional 49) WHILE USING PLATA WITH DUET!!!!

current_pl = '136'

def plata(cur_pl, fi):
    print("fi=", fi)
    co = fi[0]
    nu = fi[1::]
    print("nu=", nu)
    par = 0
    # print(co)
    # print()
    # print(nu)
    # etot nomer NADO PROVERYAT!!!!
    url = 'http://192.168.11.' + cur_pl
    urllas = 'http://192.168.11.136'
    s = r.get(url)
    # move=url+'/rr_gcode?gcode=G1'
    urlg = url + '/rr_gcode?gcode='
    urlglas = urllas + '/rr_gcode?gcode='
    iic = urlg + 'M260A8B'
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
    return render_template("chat4.html",
        #title = 'Home',
        user = user)
#app.run(debug=True)

@app.route('/feedback', methods=['POST'])
def feedback():
    user_feedback = request.form.get('feedback')
#    print(user_feedback)
    global current_pl
    # v SLEDUYUSHEY STROCHKE HOTYA BI ODNO IZ CHISEL DOILOZHNO BIT' POSLYEDNIM NOMEROM RABOCHEY PLATI!!!!
    if((user_feedback == '56') or (user_feedback == '89') or (user_feedback == '71')):
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

