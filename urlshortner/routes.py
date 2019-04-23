import secrets
import re
import json
from flask import request, render_template
from .templates import forms
from urlshortner import app

urlstore = {}


@app.route("/", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"])
def urlform():
    form = forms.URLForm()
    return render_template("home.html", form=form)


@app.route("/postURL", methods=["POST"])
def postURL():
    # Parse URL from request
    # request_data = request.json
    url = request.form["URL"]

    # url = request_data["url"]
    # Define url alias
    base_url = "https://tiny/"
    urlsecret = returnSecret()
    new_url = base_url + urlsecret
    urlstore[urlsecret] = url

    return render_template("form.html", url=new_url)


def returnSecret():
    return secrets.token_hex(5)


@app.route("/postTinyURL/", methods=["POST"])
def postTinyURL():
    # Parse URL from request
    request_data = request.json
    url = request_data["url"]
    # Parse secret from url
    secret_regex = re.compile(r"(?<=tiny/)[a-z0-9]+")
    parsed_secret = secret_regex.search(url).group()
    saved_url = urlstore[parsed_secret]

    return json.dumps(saved_url)
