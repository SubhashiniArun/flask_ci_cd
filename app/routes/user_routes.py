from flask import Blueprint, jsonify, request
from sqlalchemy.exc import IntegrityError
import os
from dotenv import load_dotenv

from ..services.user_service import fetch_users

from ..models import db, User

api_blueprint = Blueprint('api', __name__)

load_dotenv()
USER_SERVICE_URL = os.getenv("USER_SERVICE_URL")


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
    user = User.query.get(id)

    return jsonify(user=user.to_dict())

@api_blueprint.route("/users/<int:id>", methods=['PUT'])
def update_user(id):
    user = User.query.get(id)

    data = request.get_json()
    user.name = data.get('name', user.name)
    user.email = data.get('email', user.email)

    db.session.commit()

    return jsonify(message="User updated", user=user.to_dict())

@api_blueprint.route("/users/<int:id>", methods=['DELETE'])
def delete_user(id):
    user = User.query.get(id)

    db.session.delete(user)
    db.session.commit()

    return jsonify(message="User deleted")
