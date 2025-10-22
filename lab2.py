from flask import Blueprint, url_for, abort, render_template
lab2 = Blueprint('lab2', __name__)

@lab2.route('/lab2/a/')
@lab2.route('/lab2/a')
def a():
    return 'ok'


flower_list = ['роза', 'тюльпан', 'незабудка', 'ромашка']


@lab2.route('/lab2/flowers/<int:flower_id>')
def flowers(flower_id):
    if flower_id >= len(flower_list):
        abort(404)
    else:
        return "цветок: " + flower_list[flower_id]


@lab2.route('/lab2/add_flower/')
def add_flower_error():
    return 'Вы не задали имя цветка', 400


@lab2.route('/lab2/add_flower/<name>')
def add_flower(name):
    flower_list.lab2end(name)
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


@lab2.route('/lab2/example/')
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


@lab2.route('/lab2/')
def lab():
    return render_template('lab2.html')


@lab2.route('/lab2/filters/')
def filters():
    phrase = "О <b>сколько</b> <u>нам</u> <i>открытий</i> чудных..."
    return render_template('filter.html', phrase=phrase)