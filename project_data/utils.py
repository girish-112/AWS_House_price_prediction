from cgi import test
import pickle
import json
import config
import numpy as np

class HousePrice():
    def __init__(self,crime_rate,resid_area,air_qual,room_num,age,dist1,dist2,
                 dist3,dist4,teachers,poor_prop,airport,n_hot_rooms,rainfall,bus_ter,parks,waterbody):
        self.crime_rate = crime_rate
        self.resid_area = resid_area
        self.air_qual =air_qual
        self.room_num = room_num 
        self.age = age
        self.dist1 = dist1
        self.dist2 = dist2
        self.dist3 = dist3
        self.dist4 = dist4
        self.teachers = teachers
        self.poor_prop = poor_prop
        self.airport = airport
        self.n_hot_rooms = n_hot_rooms
        self.rainfall = rainfall
        self.bus_ter = bus_ter 
        self.parks = parks
        self.waterbody = 'waterbody_' + waterbody
        

    def load_model(self):
        with open(config.MODEL_FILE_PATH,'rb') as f:
            self.model = pickle.load(f)

        with open(config.JSON_FILE_PATH,'r') as f:
            self.json_data = json.load(f)

    def get_predicted_charges(self):
        self.load_model()
        
        waterbody_index = self.json_data['columns'].index(self.waterbody)

        test_array = np.zeros(len(self.json_data['columns']))
        
        print("Test Array :",test_array)
        
        test_array[0] = self.crime_rate
        test_array[1] = self.resid_area                                            
        test_array[2] = self.air_qual
        test_array[3] = self.room_num
        test_array[4] = self.age
        test_array[5] = self.dist1
        test_array[6] = self.dist2
        test_array[7] = self.dist3
        test_array[8] = self.dist4
        test_array[9] = self.teachers
        test_array[10] = self.poor_prop
        test_array[11] = self.json_data['airport'][self.airport]
        test_array[12] = self.n_hot_rooms
        test_array[13] = self.rainfall
        test_array[14] = self.json_data['bus_ter'][self.bus_ter]
        test_array[15] = self.parks
        test_array[waterbody_index] = 1


        print("Test Array :",test_array) 

        predicted_charges = np.around(self.model.predict([test_array])[0],2)
        return predicted_charges

if __name__ == "__main__":
        crime_rate=0.006320
        resid_area=32.310000
        air_qual=0.538000
        room_num=6.575000
        age=65.200000
        dist1=4.350000
        dist2=3.810000
        dist3=4.180000
        dist4=4.010000
        teachers=24.700000
        poor_prop=4.980000
        airport=1.000000
        n_hot_rooms=11.192000
        rainfall=23.000000
        bus_ter=1.000000
        parks=0.049347
        waterbody='River'

        price_hs = HousePrice(crime_rate,resid_area,air_qual,room_num,age,dist1,dist2,
                 dist3,dist4,teachers,poor_prop,airport,n_hot_rooms,rainfall,bus_ter,parks,waterbody)
        price_hs.get_predicted_charges()