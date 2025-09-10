from flask import Flask, url_for
app = Flask(__name__)

@app.route("/")
@app.route("/web")
def start():
    return """<!doctype html>
        <html>
           <body>
               <hl>web-сервер на flask</h1>
               <p><a href="/author">author</a></p>
           </body>
        </html>"""

@app.route("/author")
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
                <a href="/web">web</a>
            </body>
        </html>"""

@app.route("/lab1/image")
def image():
    path = url_for("static", filename="oak.jpg")
    return '''
<!doctype html>
<html>
    <body>
        <h1>Дуб</h1>
        <img src="''' + path + '''">
    </body>
</html>'''