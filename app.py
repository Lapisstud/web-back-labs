from flask import Flask, url_for, request, redirect
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

@app.errorhandler(404)
def not_found(err):
    return "Нет такой страницы", 404

@app.errorhandler(405)
def method_not_alloowed(err):
    return "Это действие не поддерживается.", 405

@app.errorhandler(418)
def Im_teapot(err):
    return "Студент Калинин Игорь - чайник, пожалуйста не нужно <strike> просить его варить кофе </strike> спрашивать с него защиту лабораторной", 418

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
        </div>
    </body>
</html>'''

@app.route("/lab1/web")
def web():
    return '''<!doctype html>
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
    return '''
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