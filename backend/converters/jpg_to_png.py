from PIL import Image

def convert(input_path, output_path) -> None:


    with Image.open(input_path) as img:

        try:
            with Image.open(input_path) as img:
                img.save(output_path, "PNG")
                return output_path
        except Exception as e:
            print(f"Error converting image: {e}")
            return None