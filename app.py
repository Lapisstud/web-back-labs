from flask import Flask, url_for, request, redirect, abort, render_template
import datetime

from lab1 import lab1
from lab2 import lab2
from lab3 import lab3


app = Flask(__name__)
app.register_blueprint(lab1)
app.register_blueprint(lab2)
app.register_blueprint(lab3)

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
            <a href="/lab2">Лабораторная работа 2</a>
            <a href="/lab3">Лабораторная работа 3</a>

            <footer>
                <p> Калинин Игорь Евгеньевич </p>
                <p>ФБИ-32, 3 курс, 2025</p>
            </footer>
        </div>
    </body>
</html>'''

