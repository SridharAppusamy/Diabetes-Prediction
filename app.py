from flask import Flask,render_template,request
import pickle
import numpy as np


filename='knn_model.pkl'
model=pickle.load(open(filename,'rb'))

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    collection=list()
    if request.method=='POST':
        Glucose=float(request.form['Glucose'])
        BMI = float(request.form['BMI'])
        Age = int(request.form['Age'])
        Insulin = float(request.form['Insulin'])

        data = np.array([Glucose,Insulin,BMI,Age]).reshape(1, 4)
        print(data)
        my_prediction = int(model.predict(data))
        print(my_prediction)

        return render_template('result.html', diabetes=my_prediction)





if __name__ == '__main__':
    app.run(debug=True)