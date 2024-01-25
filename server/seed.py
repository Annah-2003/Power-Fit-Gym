from random import choice as rc, randint
from faker import Faker

from app import app, db
from models import User, Instructor, Plan

genders = ["Male", "Female"]

packages = [
    "Strength, Circuit training, Swimming, Dance, Kick boxing",
    "Burpee, Aerobic exercise, Yoga, Walking, Aerobics",
    "Stretching, Plank, Skipping rope, Pilates, Cycling",
    "Running, Squats, Lunge, Interval training, Rowing",
    "Push-up, High-intensity interval training, Hiking, Weightlifting",
]

plan_names = ["Basic", "Jungle", "Premium", "Pro-max", "Master"]

fake = Faker()

with app.app_context():

    # Clear existing data
    db.drop_all()
    db.create_all()

    users = []
    for i in range(20):
        u = User(
            name=fake.name(),
            gender=rc(genders),
            age=randint(17, 70),
            email=fake.email(),
            phone=fake.numerify('081-###-####'),
        )
        users.append(u)
    db.session.add_all(users)

    plans = []
    for i in range(20):
        p = Plan(
            plan_name=rc(plan_names),
            package=rc(packages),
            user_id=randint(1, 20),
        )
        plans.append(p)
    db.session.add_all(plans)

    instructors = []
    while len(instructors) < 10:
        ins = Instructor(
            name=fake.name(),
            gender=rc(genders),
            level=randint(1, 5),
        )
        instructors.append(ins)
    db.session.add_all(instructors)

    for user in users:
        user.plan = rc(plans)
        user.instructor = rc(instructors)

    db.session.commit()
