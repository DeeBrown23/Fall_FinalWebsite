from flask import Flask , render_template


app = Flask(__name__)     

 #Create a route to the home page    
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/services')
def services():
    return render_template("services.html")

if __name__ == "__main__":
     app.run(debug=True)