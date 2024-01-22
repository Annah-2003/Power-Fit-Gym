from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'
    
    serialize_rules = ('-plans.user',)
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    gender = db.Column(db.String)
    age = db.Column(db.Integer)
    email = db.Column(db.String, nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    
    # Change the backref name from 'user' to 'member'
    plans = db.relationship('Plan', back_populates='member')
    
    def __repr__(self):
        return f'<User {self.name}, {self.age}, {self.gender}, {self.email}, {self.phone}>'

class Plan(db.Model, SerializerMixin):
    __tablename__ = 'plans'
    
    serialize_rules = ('-instructor.plans', '-member.plans',)
    
    id = db.Column(db.Integer, primary_key=True)
    plan_name = db.Column(db.String, nullable=False)
    package = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    instructor_id = db.Column(db.Integer, db.ForeignKey('instructors.id'))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    member = db.relationship('User', back_populates='plans')
    instructor = db.relationship('Instructor', back_populates='plans')

    def __repr__(self):
        return f'<Plan {self.plan_name}: {self.package}'

class Instructor(db.Model, SerializerMixin):
    __tablename__ = 'instructors'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    gender = db.Column(db.String)
    level = db.Column(db.String)

    plans = db.relationship('Plan', back_populates='instructor')

    def __repr__(self):
        return f'<Instructor {self.name} {self.level} {self.gender}>'
