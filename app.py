# a flask app 
from flask import Flask
from flask import render_template
from flask import request, redirect
import pandas as pd

app = Flask(__name__)

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
    
    # create results dictionary
    results_dict =  {'guests': guests, 'bedrooms': bedrooms,
                     'bathrooms': bathrooms, 'total_reviews': total_reviews,
                     'review_score': review_score}
    # create df
    new_submission = pd.DataFrame(results_dict,index=[0])
    
    print("Below is a new submission: ",'\n', new_submission)
    return redirect('/')
if __name__ == "__main__":
    app.run()