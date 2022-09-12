import re
from flask import Flask, jsonify,request,render_template,redirect,url_for
import config
from project_data.utils import HousePrice

app = Flask(__name__)


@app.route('/') 
def hello_flask():
    return render_template('home.html',)
    
#@app.route('/predict_charges')
@app.route('/predict_charges',methods = ['POST','GET'])
def get_house_cost():

    data=request.form
       
    crime_rate = eval(data['a'])
    resid_area = eval(data['b'])
    air_qual = eval(data['c'])
    room_num = eval(data['d'])
    age = eval(data['e'])
    dist1 = eval(data['f'])
    dist2 = eval(data['g'])
    dist3 = eval(data['h'])
    dist4 = eval(data['i'])
    teachers = eval(data['j'])
    poor_prop = eval(data['k'])
    airport = data['l']
    n_hot_rooms = eval(data['m'])
    rainfall = eval(data['n'])
    bus_ter = data['o']
    parks = eval(data['p'])
    waterbody = data['q']


    
    price_hs = HousePrice(crime_rate,resid_area,air_qual,room_num,age,dist1,dist2,
                 dist3,dist4,teachers,poor_prop,airport,n_hot_rooms,rainfall,bus_ter,parks,waterbody)
    charges = price_hs.get_predicted_charges()
     
    return render_template('pred.html', data = charges)   
    #return jsonify({"Result": f"Predicted house cost are : {charges}"})

    


if __name__ == "__main__":
    app.run(host= '0.0.0.0', port = config.PORT_NUMBER,debug=False)
