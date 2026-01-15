from converters.txt_to_pdf import convert as txt_to_pdf
from converters.jpg_to_png import convert as jpg_to_png
from converters.png_to_jpg import convert as png_to_jpg
from converters.csv_to_json import convert as csv_to_json
from converters.json_to_csv import convert as json_to_csv

CONVERTERS = {
    ("txt", "pdf"): txt_to_pdf,
    ("jpg", "png"): jpg_to_png,
    ("jpeg", "png"): jpg_to_png,
    ("png", "jpg"): png_to_jpg,
    ("png", "jpeg"): png_to_jpg,
    ("csv", "json"): csv_to_json,
    ("json", "csv"): json_to_csv,
}
