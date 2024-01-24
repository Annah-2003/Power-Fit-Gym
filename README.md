## FullStack- Software-Project
## Power-Fit-Gym

## Project Overview:
Power Fit Gym is a full-stack developed project aimed at providing users with a great and personal fitness experience. Users can easily register, create personalized profiles, choose from various fitness plans, switch between plans based on evolving goals, and view profiles of available instructors to make informed choices.

## User Stories

1. As a user, I can easily register on the gym website to access fitness services.

2. As a user, I can create a personalized profile, specifying my fitness goals and preferences.

3. As a user, I can choose from a variety of fitness plans that suit my needs and objectives.

4. As a user, I have the ability to switch between different plans based on my evolving fitness goals.

5. As a user, I can view profiles and credentials of available instructors to make informed choices.

## Group Members

1. Irene Gitau - `Scrum Master`
2. Mary Shekinah Murega 
3. Linda Kabugi

## Project Setup

For the project we:
1. Created a new GitHub repository
2. Created our various Branches using the following command:

                git branch <branchname>

Note: The branches are created such that they follow the following convetion:

                MR-<Branch-owner>

## Backend (Flask)

`Navigate to the server directory`:
            cd server

`Install dependencies`:
         pipenv install 

`Activate virtual environment`:
         pipenv shell

`Seed the Database`:
        flask db --autogenerate -m "message"
        flask db upgrade
        python seed.py

`Run the Flask app`:
         python app.py


## Frontend (React)

`Navigate to the client directory`:
        cd client

`Install dependencies`:
        npm install

`Run the React app`:
        npm start

### Dependencies
1. Python
2. Flask
3. React.js
4. SQLAlchemy
5. npm

## Code Samples

## Frontend (React)

`// components folder`
```import { useState } from "react";
    import { Link } from "react-router-dom";

   function Form({ userId, onAddPlan }) {
  const [planName, setPlanName] = useState("");
  const [packageList, setPackageList] = useState("");
  const [formErrors, setFormErrors] = useState([]);
  const [refreshPage, setRefreshPage] = useState(false);

  const packages = [
    "Strength, Circuit training, Swimming,  Dance, Kick bocking",
    "Burpee, Aerobic exercise, Yoga, Walking, Aerobics",
    "Stretching, Plank, Skipping rope, Pilates, Cycling",
    "Running, Squats, Lunge, Interval training, Rowing",
    "Push_up, High-intensity interval training, Hiking, Weightlifting",] }
    const planType = [
    "Basic",
    "Jungle",
    "Premium",
    "Pro-max",
    "Master",
    ]
```

 ### Backend (Flask)
python```
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
    return f'<User {self.name}, {self.age}, {self.gender}, {self.email}, {self.phone}>'```



## Deployment
This project has been deployed by Netlify(Front end) and Render (Back end)
The links will direct you to the deployed pages



## License
The content of this site is licensed under the MIT license.
`Copyright © 2024`

