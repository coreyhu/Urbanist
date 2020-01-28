import os

def main():
    files = os.listdir(".")
    if not files:
        print("No files TTF files in directory")


    for file in files:
        if not file.endswith(".ttf"):
            continue
    
        os.system("gftools fix-hinting {}".format(file))
        os.system("rm {}".format(file))
        os.system("mv {}.fix {}".format(file, file))
        print("Fixed Hinting on {}".format(file))

    return 0
        

if __name__ == "__main__":
    main()