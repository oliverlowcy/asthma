from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class MedicineModel(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    concentration = db.Column(db.String(80))
    frequency = db.Column(db.Integer())
    dosage = db.Column(db.String(80))
    instructions = db.Column(db.String(80))
    effects = db.Column(db.String(80))
    
    
    def __init__(self,name,concentration,frequency,dosage,instructions,effects):
        self.name = name
        self.concentration = concentration
        self.frequency = frequency
        self.dosage = dosage
        self.instructions = instructions
        self.effects = effects
        

    def json(self):
        return {"name":self.name,"concentration":self.concentration,"frequency":self.frequency,
                "dosage":self.dosage,"instructions":self.instructions,"effects":self.effects}
    
