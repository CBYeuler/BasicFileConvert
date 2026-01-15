from converters.txt_to_pdf import convert as txt_to_pdf
from converters.csv_to_json import convert as csv_to_json
from converters.jpg_to_png import convert as jpg_to_png

CONVERTERS = {
    ("txt", "pdf"): txt_to_pdf,
    ("csv", "json"): csv_to_json,
    ("jpg", "png"): jpg_to_png,
}
def get_converter(input_format, output_format):
    return CONVERTERS.get((input_format, output_format))

