from flask import Blueprint, request, jsonify, send_file
from services.file_converter import convert_file
import os

convert_bp = Blueprint("convert", __name__)

@convert_bp.route("/convert", methods=["POST"])
def convert():
    file = request.files.get("file")
    from_type = request.form.get("from_type")
    to_type = request.form.get("to_type")

    if not file or not from_type or not to_type:
        return jsonify({"error": "Missing data"}), 400

    try:
        output_path = convert_file(file, from_type, to_type)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    return jsonify({
        "download_url": f"/download/{os.path.basename(output_path)}"
    })

@convert_bp.route("/download/<filename>")
def download(filename):
    return send_file(f"uploads/{filename}", as_attachment=True)
