from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"message": "Welcome to the Body Scanner API"})

@app.route('/scan', methods=['POST'])
def scan():
    data = request.json
    # Process body scan data here (placeholder)
    return jsonify({"success": True, "data_received": data})

if __name__ == '__main__':
    app.run(debug=True)
