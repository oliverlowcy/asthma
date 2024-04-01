from flask import Flask,request
from flask_restful import Api,Resource,reqparse
from models import MedicineModel,db


app = Flask(__name__)

from flask_cors import CORS,cross_origin

CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///medicine.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)
db.init_app(app)

with app.app_context():
    db.create_all()

class MedicinesView(Resource):
    def get(self):

        # new_medicine = MedicineModel("Dexcophan","15mg/tablet",3,"1 tablet","Take after food","For cough")
        # db.session.add(new_medicine)
        # new_medicine = MedicineModel("Meloxicam","7.5mg/tablet",2,"1 tablet","Take after food","For pain and inflammation")
        # db.session.add(new_medicine)
        # new_medicine = MedicineModel("Anarex","-",3,"2 tablet","Do not take with Panadol.","Muscle relaxant, may cause drowsiness")
        # db.session.add(new_medicine)
        # new_medicine = MedicineModel("Amocla","625mg/tablet",2,"1 tablet","Complete this course of antibiotics.Take after food.","-")
        # db.session.add(new_medicine)
        # new_medicine = MedicineModel("Prednisolone","5mg/tablet",3,"1 tablet","Take after food","For inflammation of throat")
        # db.session.add(new_medicine)
        # db.session.commit()
        # db.session.flush()

        medicines = MedicineModel.query.all()
        return {'Medicine':list(x.json() for x in medicines)}
    
    def post(self):
        data = request.get_json()
        new_medicine = MedicineModel(data['name'],data['concentration'],data['frequency'],data['dosage'],data['instructions'],data['effects'])
        db.session.add(new_medicine)
        db.session.commit()
        db.session.flush()
        return new_medicine.json(),201
    

   
api.add_resource(MedicinesView,"/medicines")


app.debug = True
if __name__ == '__main__':
    app.run(host = "localhost",port = 5000)
