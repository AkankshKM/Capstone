import pandas as pd
import pickle

class Model:
    clf = None
    pkl_filename = "pickle_model.pkl"

    def __init__(self):
        with open(self.pkl_filename, 'rb') as file:
            self.clf = pickle.load(file)

    def getHour(self,encHour):
        hrs = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
        result = [0]*len(hrs)
        result[hrs.index(int(encHour))]=1
        return result
   
    def getDay(self,encDay):
        day = ["Friday","Monday","Saturday","Sunday","Thursday","Tuesday","Wednesday"]
        result = [0]*len(day)
        result[day.index(encDay)]=1
        return result

    def test_model(self,time,day,duration,esi,patientcount):
        input = []
        print("Data arrived - ",time,day,duration,esi,patientcount)
        print("new" , self.clf.predict([[duration,esi,patientcount]+self.getDay(day)+self.getHour(time)]))
        return self.clf.predict([[duration,esi,patientcount]+self.getDay(day)+self.getHour(time)])