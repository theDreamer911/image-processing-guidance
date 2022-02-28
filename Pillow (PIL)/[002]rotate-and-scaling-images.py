from PIL import Image


class InvalidFactor(Exception):
    pass


# Scae image by factorization
def scale_by_factor(im, factor):
    if factor < 0:
        raise InvalidFactor("The size of scaling must more than zeros")
    return im.resize((round(im.width * factor), round(im.height * factor)))


if __name__ == '__main__':
    with Image.open("img/stargirl.jpeg") as im:
        # Rotating function, expand makes the size follow the rotation sizes
        rotated_im = im.rotate(45, expand=True)
        rotated_im.save("saved/rotated-stargirl.jpg")

        # Scaling with custom size
        scaled_im1 = im.resize((1500, 200))
        scaled_im1.save("saved/scaled-ac-syndicate-1.png")

        # Scaling with factor
        scaled_im2 = scale_by_factor(im, 4)
        scaled_im2.save("saved/scaled-stargirl.png")
