from flask import Blueprint, jsonify, request, current_app
from sqlalchemy.exc import IntegrityError

from ..services.user_service import fetch_users

from ..models import db, User

api_blueprint = Blueprint('api', __name__)


@api_blueprint.route("/", methods=['GET'])
def home():
    return jsonify(message="Flask API working")

@api_blueprint.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')

    if not name or not email:
        return jsonify({'message': 'Both name and email are required'}), 400
    
    try:
        new_user = User(name=name, email=email)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({"message": "User Created"}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"message": "Email already exists"}), 400

@api_blueprint.route('/users', methods=['GET'])
def get_users():
    try:
        user_data = fetch_users()
        return jsonify(user_data), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@api_blueprint.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    try:
        user = User.query.get(id)

        return jsonify(user=user.to_dict())
    except AttributeError as e:
        return jsonify({"error": f"User data is missing: {str(e)}"}), 500

@api_blueprint.route("/users/<int:id>", methods=['PUT'])
def update_user(id):
    try:
        user = User.query.get(id)

        data = request.get_json()
        user.name = data.get('name', user.name)
        user.email = data.get('email', user.email)

        db.session.commit()

        return jsonify(message="User updated", user=user.to_dict())
    except Exception as e:
        return jsonify({"error": f"Error updating user data {str(e)}"})

@api_blueprint.route("/users/<int:id>", methods=['DELETE'])
def delete_user(id):
    try:
        user = User.query.get(id)

        db.session.delete(user)
        db.session.commit()

        return jsonify(message="User deleted")
    except Exception as e:
        return jsonify({"error": f"Error deleting user data {str(e)}"})
