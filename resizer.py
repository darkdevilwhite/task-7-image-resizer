import os
from PIL import Image

input_folder = 'input_images'
output_folder = 'output_images'
size = (800, 800)  # Resize to 800x800 pixels

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp')):
        img_path = os.path.join(input_folder, filename)
        try:
            with Image.open(img_path) as img:
                img = img.resize(size)
                base, _ = os.path.splitext(filename)
                new_path = os.path.join(output_folder, f"{base}_resized.png")
                img.save(new_path, "PNG")
                print(f"Saved: {new_path}")
        except Exception as e:
            print(f"Error processing {filename}: {e}")
