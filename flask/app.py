import numpy as np 
import pickle
import os
from flask import Flask , render_template , url_for , request



app = Flask(__name__, template_folder="templates")

#StartUpPredictModel = pickle.load(open('kickstart.pkl', 'rb'))
file_path = 'kickstart.pkl'  # Adjust the file path as needed

if os.path.exists(file_path):
    StartUpPredictModel = pickle.load(open(file_path, 'rb'))
else:
    print(f"File '{file_path}' does not exist.")

# The rest of your Flask application code


@app.route('/')
def index():
   return render_template('index.html')


@app.route('/PredictStartUpService')
def PredictStartUp():
    return render_template('PredictStartUp.html')

@app.route('/PredictStartUpFuture', methods=['POST'])
def PredictStartUpFuture():

    int_features = [x for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction =StartUpPredictModel.predict(final_features)

    output = prediction[0]
    if output == 1:
        predictionText ='Failed'
    elif output == 3:
        predictionText = 'successful' 
    elif output == 4:
        predictionText = 'canceled' 
    elif output == 2:
        predictionText = 'live'
    elif output == 5:
        predictionText = ' Suspended' 

    return render_template('PredictStartUp.html', prediction_text='Kickstart will{}'.format(predictionText))
if __name__ == '__main__':

  app.run(debug=True)                 