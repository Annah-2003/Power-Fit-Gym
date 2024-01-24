## FullStack- Software-Project
## Power-Fit-Gym

## Project Overview:
Power Fit Gym is a full-stack developed project aimed at providing users with a great and personal fitness experience. Users can easily register, create personalized profiles, choose from various fitness plans, switch between plans based on evolving goals, and view profiles of available instructors to make informed choices.

## User Stories

1. As a user, I can easily register on the gym website to access fitness services.
Personalized Profile

2. As a user, I can create a personalized profile, specifying my fitness goals and preferences.

3. As a user, I can choose from a variety of fitness plans that suit my needs and objectives.

4. As a user, I have the ability to switch between different plans based on my evolving fitness goals.

5. As a user, I can view profiles and credentials of available instructors to make informed choices.

## Group Members



## Project Setup
Backend (Flask)
Clone the repository:


git clone https://github.com/Moses-Oyelade/power-fit-gym.git
Navigate to the server directory:

Copy code
cd server
Install dependencies:
bash
Copy code
pipenv install
Activate virtual environment:
bash
Copy code
pipenv shell
Seed the Database:
bash
Copy code
flask db --autogenerate -m "message"
flask db upgrade
python seed.py
Run the Flask app:
bash
Copy code
python app.py
Frontend (React)
Navigate to the client directory:
bash
Copy code
cd client
Install dependencies:
bash
Copy code
npm install
Run the React app:
bash
Copy code
npm start
Dependencies
Python
Flask
React.js
SQLAlchemy
npm
Vercel
Code Samples
Frontend (React)
jsx
Copy code
// Example React Component
import React from 'react';

const UserProfile = ({ user }) => {
  return (
    <div>
      <h2>{user.name}'s Profile</h2>
      <p>Fitness Goals: {user.fitnessGoals}</p>
      {/* Additional Profile Information */}
    </div>
  );
};

export default UserProfile;
Backend (Flask)
python
Copy code
# Example Flask Route
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/users/<int:user_id>')
def get_user_profile(user_id):
    # Fetch user profile from the database
    user = fetch_user_from_database(user_id)
    return jsonify(user.to_dict())

if __name__ == '__main__':
    app.run(debug=True)
Deployment
The project can be deployed using platforms like Vercel for the frontend and Heroku or another suitable service for the backend.
License
The content of this site is licensed under the MIT license.
Copyright © 2023 Moses O. Oyelade.

