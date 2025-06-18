from flask import Flask
from flask import render_template
app = Flask(__name__)
#from app import app
from flask import request


@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname': 'Artyom' } # выдуманный пользователь
    return render_template("chat2.html",
        #title = 'Home',
        user = user)
#app.run(debug=True)

@app.route('/feedback', methods=['POST'])
def feedback():
    user_feedback = request.form.get('feedback')
    print(user_feedback)
    return f'Вы отправили следующую обратную связь: {user_feedback}'


@app.route('/command', methods=['POST'])
def send_command():
    user_command = request.form.get('command')

    # Здесь можно выполнить обработку команды и отправить ответ
#    response = f'Вы отправили команду: {user_command}'
    print(user_command)
    if (user_command == ('hi there')):
        print('OBIVAN KENOBY!!!!!!')
#    return response
    return user_command
app.run()

