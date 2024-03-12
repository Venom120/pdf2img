from pdf2image import convert_from_path
import sys
import os
import argparse
def make_dir(fname):
    try:
        os.mkdir(f"{fname}")
        dup_folder = fname
    except FileExistsError:
        dup_folder = os.listdir(os.getcwd())
        dup_folder = [file for file in dup_folder if file.startswith(fname) and not '.' in file[len(fname):]]
        dup_folder = max(dup_folder)
        t = dup_folder[-1]
        if t.isnumeric():
            dup_folder = dup_folder[:-1] + str(int(t) + 1)
        else:
            dup_folder = dup_folder + "1"
        os.mkdir(dup_folder)
    return dup_folder

def main():
    parser = argparse.ArgumentParser(description="Convert PDF to images")
    parser.add_argument('pdf_file', help='PDF file to convert')
    parser.add_argument('-nodir', '--nodir', '-nodirectory', action='store_true', help='if used then the images will not be saved inside a directory')

    args = parser.parse_args()
    dir = args.pdf_file
    fname = dir[:-4]

    if dir not in os.listdir(os.getcwd()):
        print("PDF file not found\n")
        sys.exit(1)
    elif dir[-4:] != ".pdf":
        print("Given file is not a PDF file\n")
        sys.exit(1)
    else:
        dup_folder = ''
        if not args.nodir:
            dup_folder = make_dir(fname)
            print("Converting Wait!!")

        # Convert PDF to images
        images = convert_from_path(dir)

        # Save each image
        for i, img in enumerate(images):
            if dup_folder:
                img.save(f'{dup_folder}/{fname}{i+1}.jpg', 'JPEG')
            else:
                img.save(f'{fname}{i+1}.jpg', 'JPEG')

        if not args.nodir and dup_folder:
            print("", (i+1), ("image" if i == 1 else "images"), "saved in", dup_folder)
        else:
            print("", (i+1), ("image" if i == 1 else "images"), "saved in current working directory")

if __name__ == "__main__":
    main()
