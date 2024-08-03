# import libraries
import os
import argparse
import json
from utils import pdf_to_jpg_path, removeText, removeTop, removeStateID, \
    run_ocr, convert_OCR_result_to_json, \
        openJpgImage, remove_extension, \
        save_image
import cv2
import numpy as np

def process_single_image(file_name, input_folder_path):
    redacted_image = process_image(file_name, input_folder_path)

    filename = os.path.basename(remove_extension(file_name))
    redacted_img_path = "Redacted/" + str(filename) + '.jpg'
    save_image(redacted_image, redacted_img_path)

    


# should return boolean for english learner status - ( turn into .txt file / files later... )
# return un-tilted image  with tilt degrees in name
# return column edges image
#   col top, col edges, col bottoms?
def process_image(filename, input_folder_path):

    print("processing transcript " + str(filename) + " in folder " + str(input_folder_path))

    file_path = os.path.join(input_folder_path, filename)

    # convert image to jpg 
    original_jpg_path, width, height = pdf_to_jpg_path(file_path)
    # do ocr read if necessary
    result = run_ocr(original_jpg_path)
    OCR_Data_Path = convert_OCR_result_to_json(result, filename)

    with open(OCR_Data_Path, 'r') as json_file:
        OCR_Data = json.load(json_file)

    originalImg = openJpgImage(original_jpg_path)
    textlessImg = removeText(original_jpg_path, OCR_Data)
    toplessImg, coursesHeaderRow = removeTop(textlessImg, OCR_Data)


    # REDACTED IMAGE
    cleanImage = cv2.imread(original_jpg_path, cv2.IMREAD_GRAYSCALE)
    semi_redacted_image, coursesHeaderRow = removeTop(cleanImage, OCR_Data)
    redacted_image = removeStateID(semi_redacted_image, OCR_Data, coursesHeaderRow)

    # Remove temporary image file
    OUTPUT_IMAGE_PATH = "Temp/temp.jpg"
    if os.path.exists(OUTPUT_IMAGE_PATH):
        os.remove(OUTPUT_IMAGE_PATH)

    return redacted_image




def process_images_in_folder(folder_path):
    print("processing all images in " + str(folder_path) + " folder")
    # scan in image
     # List all files in the folder
    for filename in os.listdir(folder_path):
        # Construct the full file path
        file_path = os.path.join(folder_path, filename)
        
        # Check if the file is an image
        if filename.lower().endswith(('.pdf')):

            redacted_image = process_image(filename, folder_path)

            fileName = os.path.basename(remove_extension(filename))
            redacted_img_path = "Redacted/" + str(fileName) + ".jpg"
            
            save_image(redacted_image, redacted_img_path)



def main():
    parser = argparse.ArgumentParser(description="Run OCR on images.")
    parser.add_argument('command', choices=['run'], help="The command to run.")
    parser.add_argument('target', help="The target to process: 'all' for all images in the folder or the specific image filename.")
    parser.add_argument('folder', help="The path to the folder containing images.")
    
    args = parser.parse_args()
    
    if args.command == 'run':
        if args.target == 'all':
            process_images_in_folder(args.folder)
        else:
            image_path = os.path.join(args.folder, args.target)
            if os.path.isfile(image_path):
                process_single_image(args.target, args.folder)
            else:
                print(f"File {args.target} not found in folder {args.folder}")

if __name__ == "__main__":
    main()




