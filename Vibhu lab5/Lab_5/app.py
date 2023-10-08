from sklearn.preprocessing import StandardScaler

ss = StandardScaler()
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
# open and load the pickle file provided in read mode.
model = pickle.load(open('predict_model.pkl', 'rb'))


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        age_of_the_car = request.form['age_of_the_car']
        Present_Price = float(request.form['Present_Price'])
        Kms_Driven = int(request.form['Kms_Driven'])
        Fuel_Type = request.form['Fuel_Type']
        Seller_Type = request.form['Seller_Type']
        Transmission = request.form['Transmission']
        Owner = request.form['Owner']

        prediction = model.predict(
            [[age_of_the_car, Present_Price, Kms_Driven, Fuel_Type, Seller_Type, Transmission, Owner]])
        output = round(prediction[0], 2)
        return render_template('index.html', prediction_text='You can sell your car at {} lakhs'.format(output))


if __name__ == "__main__":
    app.run(debug=True)
    app.config['TEMPLATES_AUTO_RELOAD'] = True
