from flask import Flask, jsonify, request
from http import HTTPStatus

app = Flask(__name__)  # instance of Flask application

# http://127.0.0.1:5000/
@app.route("/", methods=["GET"])
def index():
    return "Welcome to Flask Framework"

# http://127.0.0.1:5000/cohort-62
@app.route("/cohort-62", methods=["GET"])
def cohort62():
    students_list = ["Michael", "Tyler", "Carlos", "Jonathan", "Ashton", "Robert", "Kirt"]
    return students_list

# http://127.0.0.1:5000/cohort-100
@app.route("/cohort-100", methods=["GET"])
def cohort100():
    students_list = ["Pam", "Dwight", "Michael", "Oscar"]
    return students_list

# http://127.0.0.1:5000/contact
@app.route("/contact", methods=["GET"])
def contact():
    information = {"email": "kirtgerman@sdgku.edu", "phone": "123-456-7890"}
    return information

# http://127.0.0.1:5000/course-information
@app.route("/course-information", methods=["GET"])
def course_information():
    course_information = {
        "title": "Introduction Web API with Flask",
        "duration": "4 session",
        "level": "beginner"
    }
    return course_information

# ------- MiniChallenge ------
# Create a /user endpoint
# Return a dictionary with: name, role, is_active, and favorite_technologies
@app.route("/user", methods=["GET"])
def user_information():
    user_information = {
        "name": "Kirt",
        "role": "Collections Agent",
        "is-active": True,
        "favorite_technologies": ["Internet", "Laptop", "Chrome-Book"]
    }
    return user_information, HTTPStatus.OK

# Path parameter
# A dynamic part of the URL used to identify a specific item or resource
@app.route("/greet/<string:name>")
def greet(name):
    return {"message": f"Hello {name}"}

# ------------ Products -------------
products = [
    {
        "_id": 1,
        "title": "Nintendo Switch",
        "price": 299.99,
        "category": "Entertainment",
        "image": "https://picsum.photos/seed/1/300/300"
    },
    {
        "_id": 2,
        "title": "Smart Refrigerator",
        "price": 999.99,
        "category": "Kitchen",
        "image": "https://picsum.photos/seed/2/300/300"
    },
    {
        "_id": 3,
        "title": "Bluetooth Speaker",
        "price": 79.99,
        "category": "Electronics",
        "image": "https://picsum.photos/seed/3/300/300"
    }
]

# ------------------- COUPONS ---------------
coupons = [
    {"_id": 1, "code": "WELCOME10", "discount": 10},
    {"_id": 2, "code": "SPOOKY25", "discount": 25},
    {"_id": 3, "code": "VIP50", "discount": 50},
    {"_id": 4, "code": "HOLLY40", "discount": 40}
]


# Endpoint 1: GET /api/coupons
@app.route("/api/coupons", methods=["GET"])
def get_coupons():
    return coupons

# Endpoint 2: GET /api/coupons/count
@app.route("/api/coupons/count", methods=["GET"])
def coupon_count():
    # len counts the number of items in the list named coupons
    return {"count": len(coupons)}

# POST /api/coupons
@app.route("/api/coupons", methods=["POST"])
def add_coupons():
    data = request.get_json()  # get data from request
    coupons.append(data)       # add new coupon to list
    return data, 201           # return the new coupon with HTTP 201 Created

# GET /api/coupons/<id>
@app.route("/api/coupons/<int:id>", methods=["GET"])
def get_coupon_by_id(id):
    # Search for matching coupon
    for coupon in coupons:
        if coupon["_id"] == id:
            return coupon, 200

    # If not found
    return {"error": f"Coupon with ID {id} not found."}, 404

if __name__  == "__main__":
    app.run(debug=True)
    

# When this file is run directly: __name__ == "__main__"
# When this file is imported as a module: __name__ == "server.py"