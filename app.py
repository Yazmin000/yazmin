from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/agregar", methods=["POST"])
def agregar():
    titulo = request.form["titulo"]
    autor = request.form["autor"]
    print("Título:", titulo)
    print("Autor:", autor)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)