from flask import Flask
from flask import render_template
from flask import request, send_file
import data


app = Flask(__name__)


@app.route("/")
def home():
    movies = data.popularMovies()
    return render_template("index.html", movies = movies)
    
    


# @app.route('/result', methods=['GET', 'POST'])
# def result():
#     if request.method == 'POST' and len(dict(request.form)) > 0:
#         data = dict(request.form)
#         user = data["user"]
#         getData.getData(user)
#         return render_template("result.html")
#     else:
#         return "Sorry, there was an error."


if __name__ == "__main__":
    app.run(debug=True, port=8080, use_reloader=True)
