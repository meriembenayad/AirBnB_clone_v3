#!/usr/bin/python3
"""
Create a view Amenity objects that handles all default RESTFul API
"""
from flask import jsonify, abort, request
from api.v1.views import app_views
from models import Amenity


@app_views.route('/amenities', methods=['GET'])
def get_amenities():
    """
        Retrieves the list of all Amenity objects:
        GET /api/v1/amenities
    """
    amenities = Amenity.query.all()
    amenities_list = [Amenity.to_dict() for amenity in amenities]

    return jsonify(amenities_list)


@app_views.route('/amenities/<amenity_id>', methods=['GET'])
def get_amenity(amenity_id):
    """
        Retrieves a Amenity object:
        GET /api/v1/amenities/<amenity_id>

        Args:
        amenity_id -- Amenity Id
    """
    amenity = Amenity.query.get(amenity_id)
    if amenity is None:
        abort(404)

    return jsonify(amenity.to_dict())


@app_views.route('/amenities/<amenity_id>', methods=['DELETE'])
def delete_amenity(amenity_id):
    """
        Deletes a Amenity object:
        DELETE /api/v1/amenities/<amenity_id>

        Args:
        amenity_id -- Amenity Id
    """
    amenity = Amenity.query.get(amenity_id)
    if amenity is None:
        abort(404)

    amenity.delete()
    return jsonify({}), 200


@app_views.route('/amenities', methods=['POST'])
def create_amenity():
    """
        Creates a Amenity: POST /api/v1/amenities
    """
    if not request.json:
        abort(400, 'Not a JSON')
    if 'name' not in request.json:
        abort(400, 'Missing name')

    amenity = Amenity(name=request.json['name'])
    amenity.save()
    return jsonify(amenity.to_dict()), 201


@app_views.route('/amenities/<amenity_id>', methods=['PUT'])
def update_amenity(amenity_id):
    """
        Updates a Amenity object: PUT /api/v1/amenities/<amenity_id>

        Args:
        amenity_id -- Amenity id to updated
    """
    amenity = Amenity.query.get(amenity_id)
    if amenity is None:
        abort(404)
    if amenity not in request.json:
        abort(400, 'Not a JSON')

    for key, value in request.json.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(amenity, key, value)
    amenity.save()
    return jsonify(amenity.to_dict())
