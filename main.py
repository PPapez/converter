from flask import Flask, render_template, request

app = Flask(__name__)

# za index potrebujemo vstopno tocko
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/convert", methods=["POST"]) # zmozen pridobivati podatke 
def convert():
    km = float(request.form.get("km")) # iz forme v index.html vzamemo kar shranjeno pod name = km ::: to bo STRING
    # print("km =", km)

    miles = km * 0.62

    return render_template("result.html", km=km, miles=miles) # nalozimo result.html, kjer prikazemo rezultat
    # posljemo km in miles, ker jih potrebujemo na spletni strani za prikaz z jinjo

if __name__ == "__main__":
    app.run(use_reloader=True)