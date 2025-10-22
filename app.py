from flask import Flask, url_for, request, redirect, abort, render_template
import datetime
from lab1 import lab1

app = Flask(__name__)
app.register_blueprint(lab1)

@app.errorhandler(400)
def bad_request(err):
    return "Что-то пошло не так. Проверьте введённые данные", 400

@app.errorhandler(401)
def unauthorized(err):
    return "Требуется авторизация. Войдите в систему.", 401

@app.errorhandler(403)
def forbidden(err):
    return "У вас нет прав для доступа к этой странице.", 403

access_log = []

@app.errorhandler(404)
def not_found(err):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    client_ip = request.remote_addr
    requested_url = request.url
    
    access_log.append({
        'time': current_time,
        'ip': client_ip,
        'url': requested_url
    })
    
    Stylesheet = url_for("static", filename="lab1.css")
    
    log_html = ''
    for entry in access_log:
        log_html += f"<p class='log-entry'>{entry['time']}, пользователь {entry['ip']} зашёл на адрес: {entry['url']}</p>"
    
    return f'''
    <!doctype html>
<html>
    <head>
        <link rel="stylesheet" href="{Stylesheet}">
        <title>Страница не найдена</title>
    </head>
    <body>
        <div class="container error-page">
            <h1>404 - Страница не найдена</h1>
            <p>К сожалению, запрошенная страница не существует.</p>
            
            <div class="info-section">
                <h2>Информация о запросе:</h2>
                <p><strong>Ваш IP:</strong> {client_ip}</p>
                <p><strong>Время доступа:</strong> {current_time}</p>
                <p><strong>Запрошенный URL:</strong> {requested_url}</p>
            </div>
            
            <a href="/" class="home-link">Вернуться на главную страницу</a>
            
            <div class="log-section">
                <h2>Журнал посещений:</h2>
                {log_html}
            </div>
        </div>
    </body>
</html>''', 404

@app.errorhandler(405)
def method_not_alloowed(err):
    return "Это действие не поддерживается.", 405

@app.errorhandler(418)
def Im_teapot(err):
    return "Студент Калинин Игорь - чайник, пожалуйста не нужно <strike> просить его варить кофе </strike> спрашивать с него защиту лабораторной", 418

@app.errorhandler(500)
def internal_server_error(err):
    return "Технические шоколадки", 500

@app.route("/")
@app.route("/index")
def main():
    Stylesheet = url_for("static", filename="lab1.css")
    return '''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" href="''' + Stylesheet + '''">
        <title> НГТУ ФБ Лабораторные работы </title>
    </head>
    <body>
        <div class="container">
            <header>
                <h1> НГТУ ФБ </h1>
                <p>Веб-программирование часть 2. Список лабораторных работ</p>
            </header>

            <a href="/lab1">Лабораторная работа 1</a> 

            <footer>
                <p> Калинин Игорь Евгеньевич </p>
                <p>ФБИ-32, 3 курс, 2025</p>
            </footer>
        </div>
    </body>
</html>'''

@app.route('/lab2/a/')
@app.route('/lab2/a')
def a():
    return 'ok'

flower_list = ['роза', 'тюльпан', 'незабудка', 'ромашка']

@app.route('/lab2/flowers/<int:flower_id>')
def flowers(flower_id):
    if flower_id >= len(flower_list):
        abort(404)
    else:
        return "цветок: " + flower_list[flower_id]
    
@app.route('/lab2/add_flower/')
def add_flower_error():
    return 'Вы не задали имя цветка', 400

@app.route('/lab2/add_flower/<name>')
def add_flower(name):
    flower_list.append(name)
    Stylesheet = url_for("static", filename="lab1.css")
    return f'''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" href="{Stylesheet}">
        <title> Цветы </title>
    </head>
    <body>
        <div class="home-link-top">
            <a href="/">На главную</a>
        </div>
        <div class="container">
            <h1>Добавлен цветок</h1>
            <p>Название нового цветка: {name}</p>
            <p>Всего цветов: {len(flower_list)}</p>
            <p>Полный список: {flower_list}</p>
        </div>
    </body>
</html>
'''

@app.route('/lab2/example/')
def example():
    name = 'Игорь Калинин'
    groupe = 'ФБИ-32'
    year = 3
    lab = 2
    fruits = [
        {'name': 'апельсины', 'price': 100},
        {'name': 'мандарины', 'price': 120},
        {'name': 'манго', 'price': 90},
        {'name': 'бананы', 'price': 50},
        {'name': 'киви', 'price': 80}
    ]
    return render_template('example.html', name=name, groupe=groupe, lab=lab, year=year, fruits=fruits)

@app.route('/lab2/')
def lab2():
    return render_template('lab2.html')

@app.route('/lab2/filters/')
def filters():
    phrase = "О <b>сколько</b> <u>нам</u> <i>открытий</i> чудных..."
    return render_template('filter.html', phrase=phrase)