from flask import Flask, render_template, request
import numpy as np
from model.predict import predict_price_range

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get values from the form
    features = {
        'battery_power': float(request.form['battery_power']),
        'blue': float(request.form['blue']),
        'clock_speed': float(request.form['clock_speed']), 
        'dual_sim': float(request.form['dual_sim']),
        'fc': float(request.form['fc']),
        'four_g': float(request.form['four_g']),
        'int_memory': float(request.form['int_memory']),
        'm_dep': float(request.form['m_dep']),
        'mobile_wt': float(request.form['mobile_wt']),
        'n_cores': float(request.form['n_cores']),
        'pc': float(request.form['pc']),
        'px_height': float(request.form['px_height']),
        'px_width': float(request.form['px_width']), 
        'ram': float(request.form['ram']),
        'sc_h': float(request.form['sc_h']),
        'sc_w': float(request.form['sc_w']),
        'talk_time': float(request.form['talk_time']),
        'three_g': float(request.form['three_g']),
        'touch_screen': float(request.form['touch_screen']),
        'wifi': float(request.form['wifi'])
    }
    
    prediction = predict_price_range(features)
    
    price_ranges = {
        0: "Budget Phone (Low Cost Range)",
        1: "Mid-Range Phone", 
        2: "Premium Phone",
        3: "High-End Phone"
    }
    
    result = price_ranges[prediction]
    
    return render_template('predict.html', prediction=result)

if __name__ == '__main__':
    app.run(debug=True) 