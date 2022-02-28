from PIL import Image

if __name__ == "__main__":
    with Image.open('img/arya.jpg') as im:  # Read/load the image
        print(im.size)  # Checking the size of images
        im.save('./saved/arya.png')  # Saving images
