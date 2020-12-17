# a flask app 
from flask import Flask
from flask import render_template
from flask import request, redirect
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)
# load model
model = pickle.load(open('models/model_v1.pkl','rb'))
# load model features
features_df = pd.read_csv('models/feature_importances.csv')
features_list = [x for x in features_df['feature']]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    guests = request.form.get('guests', type=int)
    bedrooms = request.form.get('bedrooms', type=str)
    beds = request.form.get('beds', type=int)
    bathrooms = request.form.get('bathrooms', type=str)
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
        'is_superhost': is_superhost,'guests': guests,
        'bedrooms': bedrooms, 'beds': beds,
        'baths': bathrooms, 'reviews': total_reviews,
        'rating': review_score, 'kitchen': kitchen,
        'wifi': wifi, 'parking': parking, 'pool': pool,
        'shared_bath': shared_bath}
    # create df
    new_submission = pd.DataFrame(results_dict,index=[0])
    # print("Below is a new submission: ",'\n', new_submission)
    
    # tranform data
    new_submission_tf = pd.get_dummies(new_submission)
    # print(new_submission_tf)
    
    # check missing features
    submission_features = [x for x in new_submission_tf.columns]
    missing_features = [x for x in features_list if x not in submission_features]
    
    # add those features as dummy data
    new_submission_tf[missing_features] = 0
    
    # drop features missing from the model
    extra_columns_to_drop = [x for x in submission_features if x not in features_list]
    new_submission_tf = new_submission_tf.drop(extra_columns_to_drop,axis=1)
    
    # make prediction
    predicted_price = np.round(model.predict(new_submission_tf)[0],0)
    print('$'+str(predicted_price))
    
    # update values html
    return render_template('index.html', 
                           predicted_value='$ {} / night'.format(predicted_price),
                           guests = guests,bedrooms = bedrooms, beds = beds,
                           bathrooms = bathrooms,total_reviews = total_reviews,
                           review_score = review_score,is_superhost = is_superhost,
                           kitchen = kitchen,shared_bath = shared_bath,
                           wifi = wifi, free_parking = parking, pool = pool)
    
    # return redirect('/')
if __name__ == "__main__":
    app.run()