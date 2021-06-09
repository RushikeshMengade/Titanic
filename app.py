from flask import Flask,render_template,request
import pickle
import pandas as pd
import numpy as np

app=Flask(__name__)
model=pickle.load(open("titanic_dataset.pkl","rb"))

@app.route("/")

def home():
    return render_template('index.html')


@app.route("/predict",methods=["GET","POST"])

def predict():
    if request.method == "POST":
        # fetching gender
        gender=request.form["Gender"]
        if (gender == "MALE"):
            gender=1
            
            
        else:
            gender=0
        
        # fetching age
        age=request.form["Age"]
        if (int(age) <=20):
            age=0
        elif (int(age) > 20 and int(age) <=40):
            age=1
        elif (int(age) >40 and int(age) <=60):
            age=2
        else:
            age=3
            
            
        # fecthing title
        title=request.form["Title"]
        if  (title == "MISS"):
            title=1
        elif (title =="MR"):
            title=0
        elif (title =="MRS"):
            title=2
        else:
            title=3
            
        # fetching embarked 
        embarked=request.form["Embarked"]
        if (embarked == "SOUTHAMPON"):
            embarked=0
        elif (embarked == "CHERBOURG"):
            embarked=1
        else:
            embarked=2
            
        # fetching class
        pclass=request.form["Class"]
        if pclass == "FIRST CLASS":
            pclass=1
        elif pclass == "SECOND CLASS":
            pclass=2
        else:
            pclass=3
            
        # fetching fare
        fare=request.form["Fare"]
        if  float(fare)  <=17:
            fare=0
        elif (float(fare) >17 and float(fare) <=30):
            fare=1
        elif (float(fare) >30 and float(fare) <=100):
            fare=2
        else:
            fare=3
            
            
        # fetching familysize
        familysize=int(request.form["FamilySize"])
        
        
        prediction=model.predict([[ pclass,
            gender,
            age,
            fare,
            embarked,
            title,
            familysize]])
        output=round(prediction[0])
        if output == 1:
            return render_template('index.html',prediction_text=f" Congratulations !!You could have saved!!")
        else:
            return render_template('index.html',prediction_text=f"Sorry!! You could not have saved!! ")


    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

