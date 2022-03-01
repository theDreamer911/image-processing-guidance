from PIL import Image, ImageDraw


def add_cross_to(im, colour):
    draw = ImageDraw.Draw(im)
    draw.line((0, 0) + im.size, fill=colour, width=10)
    draw.line((0, im.size[1], im.size[0], 0), fill=colour, width=10)
    return im


def add_rectangle_to(im, topleft, bottomright, colour):
    draw = ImageDraw.Draw(im)
    draw.rectangle((topleft, bottomright), fill=colour)
    return im


def add_square_to(im, topleft, size, colour):
    draw = ImageDraw.Draw(im)
    draw.rectangle(
        (topleft, (topleft[0] + size, topleft[1] + size)), fill=colour)
    return im


def add_ellipse_to(im, topleft, bottomright, colour):
    draw = ImageDraw.Draw(im)
    draw.ellipse((topleft, bottomright), fill=colour)
    return im


def add_circle_to(im, topleft, size, colour):
    draw = ImageDraw.Draw(im)
    draw.ellipse(
        (topleft, (topleft[0] + size, topleft[1] + size)), fill=colour)
    return im


if __name__ == "__main__":
    with Image.open("img/rivendell.jpg") as im:
        print(im.size)
        im_cross = add_cross_to(im, (200, 180, 200))
        im_cross.save("saved/rivendell_crosss.png")

        im_rectangle = add_rectangle_to(im, (50, 50), (500, 350), (100, 50, 0))
        im_rectangle.save("saved/rivendell_rectangle.png")

        im_square = add_square_to(im, (675, 900), 240, (10, 200, 50))
        im_square.save("saved/rivendell_square.png")

        im_ellipse = add_ellipse_to(
            im, (990, 1030), (1500, 1200), (80, 50, 145))
        im_ellipse.save("saved/rivendell_ellipse.png")

        im_circle = add_circle_to(im, (2200, 1500), 314, (150, 90, 50))
        im_circle.save("saved/rivendell_circle.png")
