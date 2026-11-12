from flask import Flask
app=Flask(__name__)
@app.route("/")
def home():
    return"Hello world"
if _name__="__main__":
    app.run(host="0.000",port=5000)
