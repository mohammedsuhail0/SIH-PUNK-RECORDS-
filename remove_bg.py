import os
import sys
from rembg import remove
from PIL import Image

def remove_background(input_path, output_path=None):
    if not os.path.exists(input_path):
        print(f"Error: File '{input_path}' not found.")
        return None
    
    if output_path is None:
        base, _ = os.path.splitext(input_path)
        output_path = f"{base}_no_bg.png"
    
    print(f"Processing: {input_path} ...")
    inp = Image.open(input_path)
    output = remove(inp)
    output.save(output_path, "PNG")
    print(f"Done! Saved transparent image to: {output_path}")
    return output_path

if __name__ == "__main__":
    if len(sys.argv) > 1:
        img_path = sys.argv[1]
        out_p = sys.argv[2] if len(sys.argv) > 2 else None
        remove_background(img_path, out_p)
    else:
        print("Usage: python remove_bg.py <path_to_image> [optional_output_path]")
