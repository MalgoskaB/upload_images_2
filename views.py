from flask import render_template
from flask import request, redirect
import os

from flask import Flask
app = Flask(__name__)

app.config["IMAGE_UPLOADS"] = r"\Users\Gosia_Piotrek\Documents\PROGRAMOWANIE GOSIA\Zadanie Egnyte 02.10.2019\backend\static\upload"

list = []

@app.route("/", methods=["GET", "POST"])
def upload_image():
    if request.method == "POST":
        image = request.files["image"]
        if request.files:
            image.save(os.path.join(app.config["IMAGE_UPLOADS"], image.filename))
            print("Image saved")
            print(image.filename)
            list.append(image.filename)
            print(list)
            return redirect(request.url)

    return render_template("upload_image.html")


@app.route("/gallery", methods=["GET", "POST"])
def gallery():
    query = str(request.args.get('query'))
    for name in list:
        if query in name:
            return name
    return render_template("gallery.html", list=list, query=query)


if __name__ == '__main__':
    app.run(debug=True)
