import os
import glob
from ImageObject import ImageObject
import argparse


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="Image extention converter")
    
    parser.add_argument('-s', '--source', help='* source image file directry path')
    parser.add_argument('-o', '--output', help='* save directry path')
    
    args = parser.parse_args()

    target_file_list = glob.glob(args.source + "/*.HEIC")

    for target_file_path in target_file_list:
        image = ImageObject(target_file_path)
        output_file_name = os.path.basename(target_file_path).strip('.HEIC') + '.JPG'
        output_path = args.output + '/' + output_file_name
        image.save_image(output_path)
        print(f"Image converted and saved to {output_path}")

    print("All photos were converted.")
