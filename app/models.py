from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime
from sqlalchemy.sql import func


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Admin:
    ___tableme__ = 'admin'
    id=  db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_hash = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannnot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)
  

    def __repr__(self):
        return f'User {self.username}'

class Doctor:
    ___tableme__ = 'doctor'
    id=  db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    phone_number = db.Column(db.Integer())
    email = db.Column(db.String(255),unique = True,index = True)
    profile = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_hash = db.Column(db.String(255))
    @property
    def password(self):
        raise AttributeError('You cannnot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)
  

    def __repr__(self):
        return f'User {self.username}'


class Patient:
    __tablename__ = 'patient'
    id = db.Column(db.Integer,primary_key = True)
    body = db.Column(db.String())
    talks = db.relationship("Talks", backref="patient", lazy = "dynamic")



    def save_patients(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_patients(cls):
        Patient = patient.query.all()
        return patient
    @classmethod
    def clear_pitches(cls):
        Patient.all_patient.clear()
    def get_pitches(id):
        patient = Patient.query.all()
        return patient
    

class Talks:
    id = db.Column(db.Integer,primary_key = True)
    patient_id = db.Column(db.Integer, db.ForeignKey("patient.id"))

    body=db.Column(db.String)
    
