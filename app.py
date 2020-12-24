from flask import Flask

app = Flask(__name__)

@app.route("/hello-word")
def hello_world():
    return "Olá, obrigado por acessar a nossa aplicação!", 204

app.run(debug=True)

