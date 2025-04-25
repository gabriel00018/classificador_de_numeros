from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/classificar", methods=["POST"])
def classificar():
        numero = int(request.form.get("numero"))

        # Classificar par/ímpar
        par_impar = "Ímpar"
        if numero % 2 == 0:
            par_impar = "Par"

        # Classificar positivo/negativo/zero
        positivo_negativo = "Positivo"
        if numero < 0:
            positivo_negativo = "Negativo"
        elif numero == 0:
            positivo_negativo = "Zero"

        return render_template("index.html", numero=numero, par_impar=par_impar, positivo_negativo=positivo_negativo, resultado=True)

if __name__ == "__main__":
    app.run(debug=True)