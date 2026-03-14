from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data structure for the water distribution system
water_sources = [
    {'id': 1, 'name': 'Source A', 'status': 'active'},
    {'id': 2, 'name': 'Source B', 'status': 'inactive'},
]

@app.route('/sources', methods=['GET'])
def get_sources():
    return jsonify(water_sources), 200

@app.route('/sources/<int:source_id>', methods=['GET'])
def get_source(source_id):
    source = next((s for s in water_sources if s['id'] == source_id), None)
    if source:
        return jsonify(source), 200
    return jsonify({'message': 'Source not found'}), 404

@app.route('/sources', methods=['POST'])
def add_source():
    data = request.get_json()
    new_source = {'id': len(water_sources) + 1, 'name': data['name'], 'status': data['status']}
    water_sources.append(new_source)
    return jsonify(new_source), 201

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)