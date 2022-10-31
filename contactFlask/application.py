from flask import Flask, Response, request
import json
from columbia_student_resource import AccountResource
from flask_cors import CORS

# Create the Flask application object.
app = Flask(__name__)

CORS(app)

@app.route('/')
def index():
    message = "Please add the following format behind the current localhost url.  /api/ (your interested database)/(your interested table)/(accountId)"
    return message

@app.route("/api/contacts/payment/<accountId>", methods=["GET"])
def get_contacts_payment_by_uni(accountId):

    result = AccountResource.get_by_key("payment", accountId)

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp

@app.route("/api/contacts/phone/<accountId>", methods=["GET"])
def get_contacts_phone_by_uni(accountId):

    result = AccountResource.get_by_key("phone", accountId)

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp

@app.route("/api/contacts/email/<accountId>", methods=["GET"])
def get_contacts_email_by_uni(accountId):

    result = AccountResource.get_by_key("email", accountId)

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp

@app.route("/api/contacts/address/<accountId>", methods=["GET"])
def get_contacts_address_by_uni(accountId):

    result = AccountResource.get_by_key("address", accountId)

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp


@app.route("/api/contacts/Accountinfo/<accountId>", methods=["GET"])
def get_contacts_by_uni(accountId):

    result = AccountResource.get_by_union_info(accountId)

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5011)

