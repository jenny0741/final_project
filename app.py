from flask import Flask, render_template, redirect, request



app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
#app.config["MONGO_URI"] = "mongodb://localhost:27017/craigslist_app"
#mongo = PyMongo(app)

# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/craigslist_app")


@app.route("/")
def index():
    
    return render_template("index.html")


@app.route("/form")
def form():
     if request.method == "POST":
        print ("hello")
if __name__ == "__main__":
    app.run(debug=True)
