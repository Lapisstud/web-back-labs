from flask import Blueprint, url_for, request, redirect, abort
lab1 = Blueprint('lab1', __name__)

@lab1.route("/lab1")
def lab():
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


@lab1.route("/lab1/web")
def web():
    Stylesheet = url_for("static", filename="lab1.css")
    return '''
    <!doctype html>
        <html>
            <head>
                <link rel="stylesheet" href="''' + Stylesheet + '''">
                <title> web </title>
            </head>
            <body>
                <div class="home-link-top">
                    <a href="/">На главную</a>
                </div>
                <div class="container">
                    <hl>web-сервер на flask</h1>
                    <p><a href="/author">author</a></p>
                </div>
            </body>
        </html>''', 200, {
            'X-Server': 'sample',
            'Content-Type': 'text/plain; charset=utf-8'
        }


@lab1.route("/lab1/author")
def author():
    name = "Калинин Игорь Евгеньевич"
    group = "ФБИ-32"
    faculty = "ФБ"
    Stylesheet = url_for("static", filename="lab1.css")
    return '''
    <!doctype html>
        <html>
            <head>
                <link rel="stylesheet" href="''' + Stylesheet + '''">
                <title> author </title>
            </head>
            <body>
                <div class="home-link-top">
                    <a href="/">На главную</a>
                </div>
                <div class="container">
                    <p>Студент: ''' + name + '''</p>
                    <p>Группа: ''' + group + '''</p>
                    <p>Факультет: ''' + faculty + '''</p>
                    <a href="/lab1/web">web</a>
                </div>
            </body>
        </html>'''


@lab1.route("/lab1/image")
def image():
    path = url_for("static", filename="oak.jpg")
    Stylesheet = url_for("static", filename="lab1.css")
    response = f'''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" href="''' + Stylesheet + '''">
    </head>

    <body>
        <div class="home-link-top">
            <a href="/">На главную</a>
        </div>
        <div class="container">
            <h1 class="main-title">Дуб</h1>
            <img src="''' + path + '''" class "main-image">
        </div>
    </body>
</html>'''
    return response, 200, {
        'Content-Language': 'ru',
        'X-Custom-Header1': 'Value1',
        'X-Custom-Header2': 'Value2'
    }

count = 0

@lab1.route('/lab1/counter')
def counter():
    global count
    count +=1
    time = datetime.datetime.today()
    url = request.url
    client_ip = request.remote_addr
    Stylesheet = url_for("static", filename="lab1.css")
    return '''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" href="''' + Stylesheet + '''">
        <title> counter </title>
    </head>
    <body>
        <div class="home-link-top">
            <a href="/">На главную</a>
        </div>
        <div class="container">
            Сколько раз вы сюда заходили: ''' + str(count) + '''
            <hr>
            Дата и время ''' + str(time) + '''<br>
            Запрошенный адрес: ''' + url + '''<br>
            Ваш IP адрес: ''' + client_ip + '''<br>
            <a href="/lab1/discounter">Очистить счётчик</a>
        </div>
    </body>
</html>'''


@lab1.route('/lab1/discounter')
def discounter():
    global count
    count = 0
    return redirect("/lab1/counter")


@lab1.route('/lab1/info')
def info():
    return redirect("/lab1/author")


@lab1.route('/lab1/created')
def created():
    Stylesheet = url_for("static", filename="lab1.css")
    return '''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" href="''' + Stylesheet + '''">
        <title> CREATED </title>
    </head>
    <body>
        <div class="home-link-top">
            <a href="/">На главную</a>
        </div>
        <div class="container">
            <h1>Создано успешно</h1>
            <div><i>что-то создано...</i></div>
        </div>
    </body>
</html>
''', 201


@lab1.route("/lab1/error")
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
        <div class="home-link-top">
            <a href="/">На главную</a>
        </div>
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


@lab1.route('/418')
def route_error_418():
    abort(418)


@lab1.route('/400')
def route_error_400():
    abort(400)


@lab1.route('/401')
def route_error_401():
    abort(401)


@lab1.route('/403')
def route_error_403():
    abort(403)


@lab1.route('/404')
def route_error_404():
    abort(404)


@lab1.route('/405')
def route_error_405():
    abort(405)


@lab1.route('/500')
def route_error_500():
    abort(500)