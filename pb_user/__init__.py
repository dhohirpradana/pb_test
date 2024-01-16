import requests
from flask import Flask, jsonify, request
import dotenv
dotenv.load_dotenv()
import os

PB_URL = os.environ.get("PB_URL")

def list_user():
    try:
        res = requests.get(f'{PB_URL}/api/collections/tes_bda/records')
        data = res.json()
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
def detail_user(id):
    try:
        body = request.get_json()
        url = f'{PB_URL}/api/collections/tes_bda/records/{id}'
        res = requests.get(url, json=body)
        data = res.json()
        
        status_code = res.status_code
        
        return jsonify(data), status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def create_user():
    try:
        body = request.get_json()
        res = requests.post('{PB_URL}/api/collections/tes_bda/records', json=body)
        data = res.json()
        status_code = res.status_code
        
        return jsonify(data), status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
def update_user(id):
    try:
        body = request.get_json()
        url = f'{PB_URL}/api/collections/tes_bda/records/{id}'
        
        res = requests.patch(url, json=body)
        data = res.json()
        
        status_code = res.status_code
        if status_code == 404:
            return jsonify({"error": "Not found"}), 404
        
        return jsonify('User updated successfully'), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
def delete_user(id):
    try:
        res = requests.delete(f'{PB_URL}/api/collections/tes_bda/records/{id}')
        data = res.json()
        status_code = res.status_code
        
        return jsonify(data), status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500