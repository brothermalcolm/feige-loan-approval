from flask import Flask, json, request
from models import pred_loan 

api = Flask(__name__)

@api.route('/loans', methods=['POST'])
def post_loans():
    x1 = request.form['is_male']
    x2 = request.form['is_married']
    x3 = request.form['is_family']
    x4 = request.form['is_graduate']
    x5 = request.form['is_employed']
    x6 = request.form['is_creditworthy']
    x7 = request.form['is_urban']
    x8 = request.form['is_semi']
    x9 = request.form['is_rural']
    y = pred_loan(x1, x2, x3, x4, x5, x6, x7, x8, x9)
    return json.dumps({"loan": y}), 201

if __name__ == '__main__':
    api.run()