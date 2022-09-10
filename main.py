from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper_function():
        return f'<h2><strong>{function()}</strong></h2>'
    return wrapper_function


def make_emphasis(function):
    def wrapper_function():
        return f'<em>{function()}</em>'
    return wrapper_function


def make_underlined(function):
    def wrapper_function():
        return f'<u>{function()}</u>'
    return wrapper_function


@app.route('/')
@make_bold
@make_emphasis
@make_underlined
def hello_world():
    return 'Hello World'


if __name__ == "__main__":
    app.run(debug=True)
