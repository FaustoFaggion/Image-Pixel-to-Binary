from PIL import Image
import csv
import sys
import os

def change_file_extension(file_path, new_extension):
    # Get the directory path and base filename
    directory, filename = os.path.split(file_path)
    
    # Split the filename and extension
    old_name, old_extension = os.path.splitext(filename)
    
    # Construct the new filename with the desired extension
    new_filename = old_name + new_extension
    
    # Construct the new file path
    new_file_path = os.path.join(directory, new_filename)
    
    # Rename the file
    os.rename(file_path, new_file_path)

def convert_image_to_csv(image_path, output_csv_path):
    # Open the image
    image = Image.open(image_path)

    # Get the dimensions of the image
    width, height = image.size

    # Create a CSV file for writing
    with open(output_csv_path, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)

        # Iterate over each pixel in the image
        for y in range(height):
            row = []
            for x in range(width):
                # Get the RGB values of the pixel
                r, g, b = image.getpixel((x, y))

                # Convert RGB values to BINARY
                bin_value = '{:08b}\n{:08b}\n{:08b}'.format(r, g, b)

                # Append the BINARY value to the row
                row.append(bin_value)

            # Write the row to the CSV file
            csvwriter.writerow(row)

def main():
    if len(sys.argv) > 1:
        image_path = "images_to_convert/" + sys.argv[1]
        output_csv_path = "converted_images/" + sys.argv[1]
        output_csv_path = output_csv_path.split(".")[0] + ".csv"
        convert_image_to_csv(image_path, output_csv_path)
        print("Conversion complete. CSV file saved as", output_csv_path)
    else:
        print("Please provide an image file path.")


if __name__ == '__main__':
    main()