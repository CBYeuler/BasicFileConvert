from flask import Blueprint, request, jsonify
from registry import CONVERTERS
import os

convert_bp = Blueprint("convert", __name__)

@convert_bp.route("/convert", methods=["POST"])
def convert_file():
    file = request.files.get("file")
    target = request.form.get("target")

    if not file or not target:
        return jsonify({"error": "Missing file or target format"}), 400

    input_ext = file.filename.rsplit(".", 1)[-1]
    key = (input_ext, target)

    if key not in CONVERTERS:
        return jsonify({"error": "Conversion not supported"}), 400

    input_path = f"uploads/{file.filename}"
    output_filename = file.filename.rsplit(".", 1)[0] + "." + target
    output_path = f"uploads/{output_filename}"

    file.save(input_path)
    CONVERTERS[key](input_path, output_path)

    return jsonify({
        "message": "Converted",
        "download": f"/download/{output_filename}"
    })


@convert_bp.route("/download/<filename>", methods=["GET"])
def download_file(filename):
    file_path = os.path.join("uploads", filename)
    if not os.path.exists(file_path):
        return jsonify({"error": "File not found"}), 404

    return jsonify({
        "message": "File ready for download",
        "file_path": file_path
    })