from flask import Blueprint, request, jsonify
from services.file_converter import txt_to_pdf

convert_bp = Blueprint("convert", __name__)



@convert_bp.route("/convert", methods=["POST"])
def convert_file():
    file = request.files["file"]
    input_path = f"uploads/{file.filename}"
    output_path = input_path.replace(".txt", ".pdf")
    file.save(input_path)
    txt_to_pdf(input_path, output_path)

    return jsonify({"message": "File converted", "output": output_path})

@convert_bp.route("/download/<filename>", methods=["GET"])
def download_file(filename):
    output_path = f"uploads/{filename}"
    return send_file(output_path, as_attachment=True)


