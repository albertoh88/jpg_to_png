from PIL import Image
import os
import sys

def convert_jpg_to_png(input_path, output_path=None):
    """
    Convierte una imagen JPG a PNG.

    :param input_path: Ruta del archivo .jpg
    :param output_path: Ruta de salida (si es None, se guarda en el mismo directorio con extensión .png)
    """
    try:
        img = Image.open(input_path)
        if output_path is None:
            base, _ = os.path.splitext(input_path)
            output_path = base + ".png"
        img.save(output_path, "PNG")
        print(f"✅ Conversión exitosa: {output_path}")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python jpg_to_png.py <imagen.jpg> [imagen.png]")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2] if len(sys.argv) > 2 else None
        convert_jpg_to_png(input_file, output_file)