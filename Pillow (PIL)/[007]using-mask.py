from PIL import Image, ImageDraw, ImageOps


def make_circle_round(im):
    mask = Image.new("L", im.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + im.size, fill=255)

    out = ImageOps.fit(im, mask.size, centering=(0.5, 0.5))
    out.putalpha(mask)
    return out


def make_circular(im):
    offset = (im.width - im.height) // 2
    im = im.crop((offset, 0, im.height + offset, im.height))

    mask = Image.new("L", im.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + im.size, fill=255)

    out = ImageOps.fit(im, mask.size, centering=(0.5, 0.5))
    out.putalpha(mask)
    return out


def round_edges(im, radius):
    mask = Image.new("L", (radius * 2, radius * 2), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, radius * 2, radius * 2), fill=255)

    alpha = Image.new("L", im.size, 255)
    w, h = im.size

    alpha.paste(mask.crop((0, 0, radius, radius)), box=(0, 0))
    alpha.paste(mask.crop((0, radius, radius, radius * 2)),
                box=(0, h - radius))
    alpha.paste(mask.crop((radius, 0, radius * 2, radius)),
                box=(w - radius, 0))
    alpha.paste(mask.crop((radius, radius, radius * 2, radius * 2)),
                box=(w - radius, h - radius))

    im.putalpha(alpha)
    return im


if __name__ == "__main__":
    with Image.open("img/ac-syndicate.png") as im:
        im = im.convert("RGBA")
        circular_im = make_circular(im)
        circular_im.save('saved/ac-syndicate-circular.png')

        circulround_im = make_circle_round(im)
        circulround_im.save('saved/ac-syndicate-circulround.png')

        rounded_im = round_edges(im, 100)
        rounded_im.save("saved/ac-syndicate-rounded.png")

    with Image.open("img/arya.jpg") as im:
        im = im.convert("RGBA")
        rounded_im = round_edges(im, 100)
        rounded_im.save("saved/arya-rounded.png")
