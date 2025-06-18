from flask import Flask
from flask import render_template
app = Flask(__name__)
#from app import app
from flask import request
import requests as r


# DELETE "#" IN 23, 42, 51 (optional 49) WHILE USING PLATA WITH DUET!!!!

current_pl = '73'

def plata(fi):
    cur_pl=""
    nu=""
    kr=0
    print("fi=", fi)
    for i in str(fi):
        if i=="&":
            kr=1
            continue
        if kr == 0:
            cur_pl=cur_pl+i
        if kr == 1:
            nu = nu+i
#    co = fi[0]
#    nu = fi[1::]
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
    print("sent")
    print(urlg + nu)
    r.get(urlg + nu)

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
        plata(user_feedback)

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

