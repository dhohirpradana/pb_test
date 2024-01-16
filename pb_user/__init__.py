import os
import requests
from flask import jsonify, request

import dotenv
dotenv.load_dotenv()

PB_URL = os.environ.get("PB_URL")


def list_user():
    try:
        body = request.get_json()
        res = requests.get(
            f'{PB_URL}/api/collections/tes_bda/records', json=body, timeout=10)
        data = res.json()
        status_code = res.status_code

        return jsonify(data), status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500


def detail_user(user_id):
    try:
        body = request.get_json()
        url = f'{PB_URL}/api/collections/tes_bda/records/{user_id}'
        res = requests.get(url, json=body, timeout=10)
        data = res.json()

        status_code = res.status_code

        return jsonify(data), status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500


def create_user():
    try:
        body = request.get_json()
        res = requests.post(
            '{PB_URL}/api/collections/tes_bda/records', json=body, timeout=10)
        data = res.json()
        status_code = res.status_code

        return jsonify(data), status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500


def update_user(user_id):
    try:
        body = request.get_json()
        url = f'{PB_URL}/api/collections/tes_bda/records/{user_id}'

        res = requests.patch(url, json=body, timeout=10)
        # data = res.json()

        status_code = res.status_code
        if status_code == 404:
            return jsonify({"error": "Not found"}), 404

        return jsonify('User updated successfully'), 200
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500


def delete_user(user_id):
    try:
        res = requests.delete(
            f'{PB_URL}/api/collections/tes_bda/records/{user_id}', timeout=10)
        data = res.json()
        status_code = res.status_code

        return jsonify(data), status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500
