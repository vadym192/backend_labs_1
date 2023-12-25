from datetime import datetime
from flask import jsonify
from main import app

@app.route('/healthcheck', methods=['GET'])
def health_check():
    service_status = 200
    date = datetime.utcnow().isoformat()

    response_data = {
        "date": date,
        "status": service_status
    }

    return jsonify(response_data), service_status

if __name__ == '__main__':
    app.run(debug=True)
