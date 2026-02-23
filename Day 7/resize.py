import os
from PIL import Image

# ===== SETTINGS =====
INPUT_FOLDER = "input_images"
OUTPUT_FOLDER = "output_images"
NEW_WIDTH = 800
NEW_HEIGHT = 600
CONVERT_FORMAT = "JPEG"   # Change to "PNG" if needed
# ====================

# Create output folder if not exists
if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

# Supported formats
SUPPORTED_FORMATS = (".jpg", ".jpeg", ".png", ".webp")

for filename in os.listdir(INPUT_FOLDER):
    if filename.lower().endswith(SUPPORTED_FORMATS):

        input_path = os.path.join(INPUT_FOLDER, filename)

        try:
            with Image.open(input_path) as img:

                # Resize image
                resized_img = img.resize((NEW_WIDTH, NEW_HEIGHT))

                # Remove old extension and create new filename
                name_without_ext = os.path.splitext(filename)[0]
                output_filename = f"{name_without_ext}.{CONVERT_FORMAT.lower()}"
                output_path = os.path.join(OUTPUT_FOLDER, output_filename)

                # Save resized image
                resized_img.save(output_path, CONVERT_FORMAT)

                print(f"Resized and saved: {output_filename}")

        except Exception as e:
            print(f"Error processing {filename}: {e}")

print("\nBatch resizing completed successfully!")