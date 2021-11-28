from flask import Flask, request
app = Flask(__name__)

response = ""

@app.route('/', methods=['POST', 'GET'])
def ussd_callback():
    global response
    session_id = request.values.get("sessionId", None)
    service_code = request.values.get("serviceCode", None)
    phone_number = request.values.get("phoneNumber", None)
    text = request.values.get("text", "default")

    if text == '':
        response  = "CON You have recently got your hair done at siyakhula salon. \n"
        "How would you rate the service on the scale of 1 to 5? \n"
        response += "1. Worst \n"
        response += "2. Bad "
        response += "3. Ok"
        response += "4. Good"
        response += "5. Great"
    
    elif text == '5':
        response = "CON Would you recommend it \n"
        response += "1. Yes \n"
        response += "2. No "
    
    elif text == '5*1':
        response = "END Thank you for Feedback\n"
        
    
    elif text == '1':
        response = "END Thank you for Feedback\n"
    
if __name__ == '__main__':
    app.run(debug=True)