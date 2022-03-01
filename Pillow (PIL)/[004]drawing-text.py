from PIL import Image, ImageDraw, ImageFont


def add_text(im, text, topleft, size, colour):
    font = ImageFont.truetype('fonts/PlayfairDisplay-Italic.ttf', size)
    draw = ImageDraw.Draw(im)
    draw.text(topleft, text, font=font, fill=colour)
    return im


if __name__ == "__main__":
    with Image.open("img/arya.jpg") as im:
        print(im.size)
        im = add_text(im, "Arya Stark", (600, 1550), 100, (200, 180, 240))
        im = add_text(im, "Hero of North",
                      (700, 1680), 50, (200, 180, 240))
        im.save("saved/arya-with-text.png")
