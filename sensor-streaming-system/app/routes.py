from flask import current_app, request, jsonify, Blueprint

bp = Blueprint('main', __name__)

@bp.route('/record', methods=['POST'])
def record_temperature():
    data = request.json
    temperature = data.get('temperature')
    if temperature is not None:
        current_app.redis.lpush('temperatures', temperature)
        return jsonify({'status': 'success'}), 201
    return jsonify({'status': 'error', 'message': 'Invalid data'}), 400

@bp.route('/collect', methods=['GET'])
def collect_temperature():
    temperatures = current_app.redis.lrange('temperatures', 0, -1)
    if temperatures:
        avg_temp = sum(map(float, temperatures)) / len(temperatures)
        return jsonify({'average_temperature': avg_temp})
    return jsonify({'status': 'error', 'message': 'No data available'}), 404
