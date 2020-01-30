import os
os.chdir(os.path.dirname(__file__))
font_dir = "../fonts/static"

def main():
    files = os.listdir(font_dir)
    if not files:
        print("No files TTF files in directory")


    for f in files:
        
        if not f.endswith(".ttf"):
            continue
    
        file_path = os.path.join(font_dir, f)
        os.system("gftools fix-hinting {}".format(file_path))
        os.system("mv {} {}.tmp".format(file_path, file_path))
        success = os.system("mv {}.fix {}".format(file_path, file_path)) == 0

        if success:
            print("Fixed Hinting on {}".format(file_path))
            os.system("rm {}.tmp".format(file_path))
        else:
            print("Hinting failed on {} (Font may already have bit 3 enabled). Reverting...".format(file_path))
            os.system("mv {}.tmp {}".format(file_path, file_path))

    return 0
        

if __name__ == "__main__":
    exit(main())