from flask import Flask, render_template, request
import numpy as np
import pickle


app = Flask(__name__, template_folder= 'template')
model = pickle.load(open('CKD.pkl', 'rb'))

@app.route('/',methods=['GET'])
def Home():
    return render_template('Home.html')

@app.route('/index',methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        bu = float(request.form['bu'])
        bgr = float(request.form['bgr'])
        cad = float(request.form['cad'])
        ane = float(request.form['ane'])
        pc = float(request.form['pc'])
        rbc = float(request.form['rbc'])
        dm = float(request.form['dm'])
        pe = float(request.form['pe'])

        values = np.array([[rbc,pc,bgr,bu,pe,ane,dm,cad]])
        prediction = model.predict(values)

        return render_template('result.html', prediction=prediction)


if __name__ == "__main__":
    app.run(debug=True)

