import os
from PIL import Image
import pyheif


class ImageObject:

    def __init__(self, source_path):
        
        self.source_path = source_path
        _, self.source_format = os.path.splitext(source_path)
        self.source_format_upper = self.source_format.strip(".").upper()
        if self.source_format_upper == 'HEIC':
            print("HEIC file is required.")
            heif_file = pyheif.read(source_path)
            self.image_data = Image.frombytes(
            heif_file.mode, 
            heif_file.size, 
            heif_file.data,
            "raw",
            heif_file.mode,
            heif_file.stride,
            )
        else:
            print("NOT HEIC file is required.")
            self.image_data = Image.open(source_path)

    def save_image(self, output_path):

        _, self.output_format = os.path.splitext(output_path)
        self.output_format_upper = self.output_format.strip(".").upper()

        if self.output_format_upper not in ['HEIC', 'JPG', 'JPEG', 'PNG']:
            raise ValueError("Unsupported output format. Choose from 'HEIC', 'JPG', 'JPEG', 'PNG'.")
        
        if self.output_format_upper == 'JPG':
            self.save_format = 'JPEG'
        else:
            self.save_format = self.output_format_upper

        self.image_data.save(output_path, format=self.save_format)
        return output_path
