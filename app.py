
# app.py

from flask import Flask 

def create_app():
    app = Flask(__name__)
    @app.route('/')
    def home():
        return 'Hi Devops Geeks Welcome to the class123 New Data 123456 New PR dodo'

    return app

    
if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=80, debug=True)
