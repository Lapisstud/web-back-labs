from flask import Flask, url_for, request, redirect, abort
import datetime
app = Flask(__name__)

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

@app.route("/lab1")
def lab1():
    Stylesheet = url_for("static", filename="lab1.css")
    return '''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" href="''' + Stylesheet + '''">
        <title> Лабораторная 1 </title>
    </head>
    <body>
        <div class="container">
            <p>Flask — фреймворк для создания веб-приложений на языке программирования Python, использующий набор инструментов 
            Werkzeug, а также шаблонизатор Jinja2. Относится к категории так называемых микрофреймворков — минималистичных каркасов 
            веб-приложений, сознательно предоставляющих лишь самые базовые возможности.</p>

            <a href="/">Вернуться на главную</a> 
            <h2>Список роутов</h2>
            <a href="/lab1/web">web</a><br>
            <a href="/lab1/author">author</a><br>
            <a href="/lab1/image">image</a><br>
            <a href="/lab1/counter">counter</a><br>
            <a href="/lab1/info">info</a><br>
            <a href="/lab1/created">created</a><br>
            <a href="/lab1/error">error</a>
        </div>
    </body>
</html>'''

@app.route("/lab1/web")
def web():
    return '''
    <!doctype html>
        <html>
           <body>
               <hl>web-сервер на flask</h1>
               <p><a href="/author">author</a></p>
           </body>
        </html>''', 200, {
            'X-Server': 'sample',
            'Content-Type': 'text/plain; charset=utf-8'
        }

@app.route("/lab1/author")
def author():
    name = "Калинин Игорь Евгеньевич"
    group = "ФБИ-32"
    faculty = "ФБ"

    return """<!doctype html>
        <html>
            <body>
                <p>Студент: """ + name + """</p>
                <p>Группа: """ + group + """</p>
                <p>Факультет: """ + faculty + """</p>
                <a href="/lab1/web">web</a>
            </body>
        </html>"""

@app.route("/lab1/image")
def image():
    path = url_for("static", filename="oak.jpg")
    Stylesheet = url_for("static", filename="lab1.css")
    return'''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" href="''' + Stylesheet + '''">
    </head>

    <body>
        <div class="container">
            <h1 class="main-title">Дуб</h1>
            <img src="''' + path + '''" class "main-image">
        </div>
    </body>
</html>'''

count = 0

@app.route('/lab1/counter')
def counter():
    global count
    count +=1
    time = datetime.datetime.today()
    url = request.url
    client_ip = request.remote_addr
    return '''
<!doctype html>
<html>
    <body>
        Сколько раз вы сюда заходили: ''' + str(count) + '''
        <hr>
        Дата и время ''' + str(time) + '''<br>
        Запрошенный адрес: ''' + url + '''<br>
        Ваш IP адрес: ''' + client_ip + '''<br>
        <a href="/lab1/discounter">Очистить счётчик</a>
    </body>
</html>'''

@app.route('/lab1/discounter')
def discounter():
    global count
    count = 0
    return redirect("/lab1/counter")

@app.route('/lab1/info')
def info():
    return redirect("/lab1/author")

@app.route('/lab1/created')
def created():
     return '''
<!doctype html>
<html>
    <body>
        <h1>Создано успешно</h1>
        <div><i>что-то создано...</i></div>
    </body>
</html>
''', 201
@app.route('/418')
def route_error_418():
    abort(418)

@app.route('/400')
def route_error_400():
    abort(400)

@app.route('/401')
def route_error_401():
    abort(401)

@app.route('/403')
def route_error_403():
    abort(403)

@app.route('/404')
def route_error_404():
    abort(404)

@app.route('/405')
def route_error_405():
    abort(405)

@app.route('/500')
def route_error_500():
    abort(500)

@app.route("/lab1/error")
def route_error():
    Stylesheet = url_for("static", filename="lab1.css")
    return '''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" href="''' + Stylesheet + '''">
        <title> Ошибки </title>
    </head>
    <body>
        <div class="container">
            <a href="/lab1">Вернуться к первой лабораторной</a> 
            <h1>Список роутов для вызова ошибок</h1>
            <a href="/400">400</a><br>
            <a href="/401">401</a><br>
            <a href="/403">403</a><br>
            <a href="/404">404</a><br>
            <a href="/405">405</a><br>
            <a href="/418">418</a><br>
            <a href="/500">500</a><br>
        </div>
    </body>
</html>'''