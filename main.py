from flask import Flask
from flask import url_for

app = Flask(__name__)


@app.route("/")
def name_of_operation():
    return "Миссия Колонизация Марса"


@app.route("/index")
def slogan_of_operation():
    return "И на Марсе будут яблони цвести!"


@app.route("/promotion")
def promotion():
    text = ["Человечество вырастает из детства.",
            "Человечеству мала одна планета.",
            "Мы сделаем обитаемыми безжизненные пока планеты.",
            "И начнем с Марса!",
            "Присоединяйся!"]
    return "<br>".join(text)


@app.route("/image_mars")
def mars():
    return f"""
<html>
    <head>
        <title>Привет, Марс!</title>
    </head>
    <body>
        <h1>Жди нас, Марс!</h1>
        <img src="{url_for('static', filename='image/mars2.jpg')}">
        <p>Вот она какая, красная планета.</p>
    </body>
</html>"""


@app.route("/promotion_image")
def promotion_image():
    return f"""
<html>
    <head>
        <title>Привет, Марс!</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/main2.css')}" >
    </head>
    <body>
        <h1>Жди нас, Марс!</h1>
        <img src="{url_for('static', filename='image/mars2.jpg')}">
        <div class="alert alert-secondary" role="alert">
            Человечество вырастает из детства.
        </div>
        <div class="alert alert-success" role="alert">    
            Человечеству мала одна планета.
        </div>
        <div class="alert alert-secondary" role="alert">
            Мы сделаем обитаемыми безжизненные пока планеты.
        </div>
        <div  class="alert alert-warning" role="alert">
            И начнем с Марса!
        </div>
        <div  class="alert alert-danger" role="alert">
            Присоединяйся!
        </div>
    </body>
</html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
