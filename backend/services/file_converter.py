import os
from services.converter_registery import CONVERTERS

UPLOAD_FOLDER = "uploads"

def convert_file(file, from_type: str, to_type: str) -> str:
    key = (from_type.lower(), to_type.lower())

    if key not in CONVERTERS:
        raise ValueError(f"Conversion {from_type} → {to_type} not supported")

    input_path = os.path.join(UPLOAD_FOLDER, file.filename)
    output_filename = file.filename.rsplit(".", 1)[0] + f".{to_type}"
    output_path = os.path.join(UPLOAD_FOLDER, output_filename)

    file.save(input_path)

    converter = CONVERTERS[key]
    converter(input_path, output_path)

    return output_path
