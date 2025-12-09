from flask import Flask

app = Flask(__name__) #instance of Flask application

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

# http:127.0.0.1:5000/course-information
@app.route("/course-information", methods=["GET"])
def course_information():
     course_information = {
          "title": "Introduction Web API with Flask", 
          "duration": "4 session", 
          "level": "beginner"
        }
     return course_information 

# ------------------- COUPONS ---------------
coupons = [
  {"_id": 1, "code": "WELCOME10", "discount": 10},
  {"_id": 2, "code": "SPOOKY25", "discount": 25},
  {"_id": 3, "code": "VIP50", "discount": 50}
]

#endpoint1
@app.route("/api/coupons", methods=["GET"])
def get_coupons():
    return coupons

#endpoint2
@app.route("/api/coupons/count", methods=["GET"])
def coupon_count():
     return {"count": len(coupons)} # len counts the number of items in the list named coupons


if __name__  == "__main__":
    app.run(debug=True)
    

# When this file is run directly: __name__ == "__main__"
# When this file is imported as a module: __name__ == "server.py"