from PIL import Image
import pillow_heif
import os

# Function to convert multiple HEIC, PNG, and JPG images to a single PDF
def images_to_pdf(folder_path, pdf_path):
    try:
        # Get all HEIC, PNG, and JPG image files in the folder
        image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.heic', '.png', '.jpg', '.jpeg'))]

        if not image_files:
            raise ValueError("No HEIC, PNG, or JPG images found in the specified folder.")

        # Sort the images by name or any other criteria if needed
        image_files.sort()

        # Open each image and append to the list of images
        image_list = []
        for file in image_files:
            image_path = os.path.join(folder_path, file)
            try:
                if file.lower().endswith('.heic'):
                    heif_image = pillow_heif.read_heif(image_path)
                    image = Image.frombytes(
                        heif_image.mode,
                        heif_image.size,
                        heif_image.data,
                        "raw",
                        heif_image.mode,
                        heif_image.stride,
                    )
                else:  # For PNG and JPG images
                    image = Image.open(image_path)

                image_list.append(image.convert('RGB'))
            except Exception as e:
                print(f"Error opening image {file}: {e}")

        # Save all images as a single PDF
        if image_list:
            try:
                image_list[0].save(pdf_path, save_all=True, append_images=image_list[1:])
                print(f"PDF saved at {pdf_path}")
            except Exception as e:
                print(f"Error saving PDF: {e}")
        else:
            print("No images to save to PDF.")
    except Exception as e:
        print(f"Error processing images: {e}")

# Example usage
folder_path = r"C:\\Users\\richardp\\Pictures\\2651empiredrpictures"
pdf_path = r"C:\\Users\\richardp\\Pictures\\2651empiredrpictures\\output.pdf"
images_to_pdf(folder_path, pdf_path)
