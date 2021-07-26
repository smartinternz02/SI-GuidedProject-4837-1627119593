from flask import Flask, render_template , request
import pickle
import joblib

model = pickle.load(open("carperformanceml.pkl",'rb'))


app = Flask(__name__)
@app.route('/')
def hello_world():
    return render_template("index.html")
@app.route('/guest', methods = ["POST"])
def guest():
    cylinders = request.form["cylinders"]
    displacement = request.form["displacement"]
    horsepower = request.form["horsepower"]
    weight = request.form["weight"]
    acceleration = request.form["acceleration"]
    modelyear = request.form["modelyear"]
    origin = request.form["origin"]
    data = [[int(cylinders),int(displacement),int(horsepower),int(weight),int(acceleration),int(modelyear),int(origin)]]
    prediction = model.predict(data)
    
    return render_template("index.html",y = prediction)
app.run(debug = True) 