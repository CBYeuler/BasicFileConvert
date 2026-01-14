from flask import Flask, request, send_file
from routes.convert import conver_bp
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(conver_bp, url_prefix='/api/convert')
CORS(app)
if __name__ == '__main__':
    app.run(debug=True)

    