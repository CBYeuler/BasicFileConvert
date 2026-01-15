from PIL import Image

def convert(input_path, output_path):
    with Image.open(input_path) as img:
        if img.mode in ("RGBA", "LA"):
            background = Image.new("RGB", img.size, (255, 255, 255))
            background.paste(img, mask=img.split()[-1])
            background.save(output_path, "JPEG")
        else:
            img.convert("RGB").save(output_path, "JPEG")
