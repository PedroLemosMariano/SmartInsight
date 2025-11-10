from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Bem-vindo à minha aplicação Flask!</h1><p>Feito por Manoel 😎</p>"

if __name__ == '__main__':
    app.run(debug=True)
