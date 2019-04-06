from flask import  Flask,render_template,request
import urllib
import ssl

app=Flask(__name__)
ssl._create_default_https_context=ssl._create_unverified_context
@app.route("/",methods=["get"])
def index():
    return render_template("index.html")

@app.route("/notice",methods=["get"])
def notice():
    return render_template("notice.html")

@app.route("/face",methods=["get"])
def face():
    return render_template("face.html")


@app.route("/photo",methods=["POST"])
def photo():
    data = urllib.parse.urlencode(request.form).encode("utf8")
    print(data)
    res = urllib.request.urlopen("https://118.190.150.35:5000/api/photo", data=data)
    con = res.read()
    print(con)
    return con


@app.route("/checkpage",methods=["get"])
def checkpage():

    return render_template("check.html")

@app.route("/check",methods=["POST"])
def check():
    data = urllib.parse.urlencode(request.form).encode("utf8")
    print(data)
    res = urllib.request.urlopen("https://118.190.150.35:5000/api/check", data=data)
    con = res.read()
    print(con)
    return con

@app.route("/diff",methods=["get"])
def diff():

    return render_template("diff.html")

@app.route("/success",methods=["get"])
def success():

    return render_template("success.html")
app.run()