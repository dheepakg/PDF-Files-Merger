# import the Flask class from the flask module
from flask import Flask, render_template, request
from werkzeug import secure_filename


# create the application object
app = Flask(__name__)

# use decorators to link the function to a url
@app.route("/")
def home():
    return "Hello, World!"  # return a string


@app.route("/upload")
def welcome():
    return render_template("upload.html")  # render a template


@app.route("/uploader", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        for f in request.files.getlist("photo"):
            f.save(secure_filename(f.filename))
        return "file uploaded successfully"


# todo files getiing saved somewherer in drive, should explicitly
# todo mention the path


# start the server with the 'run()' method
if __name__ == "__main__":
    app.run(debug=True)
