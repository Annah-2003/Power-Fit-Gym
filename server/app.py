from flask import Flask, request, jsonify, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource
from flask_swagger_ui import get_swaggerui_blueprint
from models import db, User, Plan, Instructor

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False  # Set this to False to disable pretty printing

migrate = Migrate(app, db)

db.init_app(app)
api = Api(app)

# Create Swagger UI Blueprint
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGER_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Power'f GYM API"
    }
)

app.register_blueprint(SWAGGER_BLUEPRINT, url_prefix=SWAGGER_URL)

# Create Flask-RESTful API
api = Api(app)

# GET /users
class UsersEndpoint(Resource):
    def get(self):
        return make_response(jsonify([user.to_dict(rules=('-plans',)) for user in User.query.all()]), 200)

    def post(self):
        data = request.get_json()
        user = User(
            name=data.get('name'),
            gender=data.get('gender'),
            age=data.get('age'),
            email=data.get('email'),
            phone=data.get('phone')
        )
        db.session.add(user)
        db.session.commit()

        user_dict = user.to_dict(rules=('-plans.instructor',))
        return make_response(jsonify(user_dict), 201)

# GET, PATCH, DELETE /users/<int:id>
class UsersByIdEndpoint(Resource):
    def get(self, id):
        user = User.query.filter_by(id=id).first()
        if user is None:
            return make_response({"error": "User not found."}, 404)
        return make_response(jsonify(user.to_dict()), 200)

    def patch(self, id):
        user = User.query.filter_by(id=id).first()
        if user is None:
            return make_response({"error": "User not found."}, 404)

        for attr in request.form:
            setattr(user, attr, request.form.get(attr))

        db.session.add(user)
        db.session.commit()

        user_dict = user.to_dict()
        return make_response(user_dict, 200)

    def delete(self, id):
        user = User.query.filter_by(id=id).first()
        if user is None:
            return make_response({"error": "User not found."}, 404)

        db.session.delete(user)
        db.session.commit()

        response_body = {
            "delete_successful": True,
            "message": "User deleted."
        }

        return make_response(response_body, 200)

# GET /plans
class PlansEndpoint(Resource):
    def get(self):
        return make_response(jsonify([plan.to_dict() for plan in Plan.query.all()]), 200)

    def post(self):
        data = request.get_json()
        plan = Plan(
            user_id=data.get('user_id'),
            plan_name=data.get('plan_name'),
            package=data.get('package'),
        )
        db.session.add(plan)
        db.session.commit()

        return make_response(jsonify({'id': plan.id, 'user_id': plan.user_id, 'plan_name': plan.plan_name, 'package': plan.package}), 201)

# GET, PATCH /plans/<int:id>
class PlanByIdEndpoint(Resource):
    def get(self, id):
        plan = Plan.query.filter_by(id=id).first()
        if plan is None:
            return make_response({"error": "Plan not found."}, 404)
        return make_response(jsonify(plan.to_dict()), 200)

    def patch(self, id):
        plan = Plan.query.filter_by(id=id).first()
        if plan is None:
            return make_response({"error": "Plan not found."}, 404)

        for attr in request.form:
            setattr(plan, attr, request.form.get(attr))

        db.session.add(plan)
        db.session.commit()

        plan_dict = plan.to_dict()
        return make_response(plan_dict, 200)

# GET /plans/plan_name
class PlansPlanNameEndpoint(Resource):
    def get(self):
        plans_plan_name = Plan.query.order_by(Plan.plan_name).all()
        plans_plan_name_serialized = [pn.to_dict() for pn in plans_plan_name]
        return make_response(jsonify(plans_plan_name_serialized), 200)

# GET /instructors
class InstructorsEndpoint(Resource):
    def get(self):
        return make_response(jsonify([instructor.to_dict() for instructor in Instructor.query.all()]), 200)

# Add resources to the API
api.add_resource(UsersEndpoint, '/users')
api.add_resource(UsersByIdEndpoint, '/users/<int:id>')
api.add_resource(PlansEndpoint, '/plans')
api.add_resource(PlanByIdEndpoint, '/plans/<int:id>')
api.add_resource(PlansPlanNameEndpoint, '/plans/plan_name')
api.add_resource(InstructorsEndpoint, '/instructors')

if __name__ == '__main__':
    app.run(port="5555", debug=True)



