from flask import Flask, render_template, request
from model import predict_image
# import utils
import json

app = Flask(__name__)

with open('./disease_data.json') as file:
    disease_data = json.load(file)

@app.route('/', methods=['GET'])
def home():
    return render_template('Home_Page.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            file = request.files['file']
            img = file.read()
            prediction = predict_image(img)
            print(prediction)
            if prediction in disease_data:
                disease_details = disease_data[prediction]
                print(disease_details)
                disease_details['Disease'] = prediction.replace("_", " ").capitalize()
                print("result", disease_details)
                return render_template('Result_Page.html', status=200, result=disease_details)
            else:
                return render_template('Result_Page.html', status=200, result="Disease not found in the database.")
        except:
            pass
    return render_template('Home_Page.html', status=500, res="Internal Server Error")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
