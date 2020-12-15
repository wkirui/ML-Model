# a flask app 
from flask import Flask
from flask import render_template
from flask import request, redirect
import pandas as pd
import pickle

app = Flask(__name__)
# load model
model = pickle.load(open('/models/model_v1.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    guests = request.form.get('guests', type=int)
    bedrooms = request.form.get('bedrooms', type=int)
    bathrooms = request.form.get('bathrooms', type=int)
    total_reviews = request.form.get('total-reviews', type=int)
    review_score = request.form.get('review-score', type=int)
    kitchen = request.form.get('kitchen', type=str)
    is_superhost = request.form.get('is_superhost', type=str)
    wifi = request.form.get('wifi', type=str)
    parking = request.form.get('parking', type=str)
    pool = request.form.get('pool', type=str)
    shared_bath = request.form.get('shared_bath', type=str)
    
    # create results dictionary
    results_dict =  {
        'is_superhost': is_superhost,'guests': guests, 'bedrooms': bedrooms,
        'bathrooms': bathrooms, 'total_reviews': total_reviews,
        'review_score': review_score, 'kitchen': kitchen,
        'wifi': wifi, 'parking': parking, 'pool': pool,
        'shared_bath': shared_bath}
    # create df
    new_submission = pd.DataFrame(results_dict,index=[0])
    print("Below is a new submission: ",'\n', new_submission)
    
    # tranform data
    new_submission_tf = pd.get_dummies(new_submission)
    print(new_submission_tf)
    
    # make prediction
    predicted_price = model.predict(new_submission_tf)
    print(predicted_price)
    
    return redirect('/')
if __name__ == "__main__":
    app.run()