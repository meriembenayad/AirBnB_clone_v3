from flask import Flask, jsonify, abort, request
from models import storage, State

app = Flask(__name__)

@app.route('/api/v1/states', methods=['GET'])
def get_states():
    states = [state.to_dict() for state in storage.all(State).values()]
    return jsonify(states)

@app.route('/api/v1/states/<state_id>', methods=['GET'])
def get_state(state_id):
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    return jsonify(state.to_dict())

@app.route('/api/v1/states/<state_id>', methods=['DELETE'])
def delete_state(state_id):
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    storage.delete(state)
    storage.save()
    return jsonify({}), 200

@app.route('/api/v1/states', methods=['POST'])
def create_state():
    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'name' not in request.get_json():
        abort(400, description="Missing name")
    state = State(name=request.get_json()['name'])
    state.save()
    return jsonify(state.to_dict()), 201

@app.route('/api/v1/states/<state_id>', methods=['PUT'])
def update_state(state_id):
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    if not request.get_json():
        abort(400, description="Not a JSON")
    for key, value in request.get_json().items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(state, key, value)
    state.save()
    return jsonify(state.to_dict()), 200
