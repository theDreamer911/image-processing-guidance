from PIL import Image, ImageDraw, ImageFilter
from numpy import imag

filters = {
    "Blur": ImageFilter.BLUR,
    "Contour": ImageFilter.CONTOUR,
    "Detail": ImageFilter.DETAIL,
    "Edge Enchance": ImageFilter.EDGE_ENHANCE,
    "Edge Enchance More": ImageFilter.EDGE_ENHANCE_MORE,
    "Emboss": ImageFilter.EMBOSS,
    "Find Edges": ImageFilter.FIND_EDGES,
    "Sharpen": ImageFilter.SHARPEN,
    "Smooth": ImageFilter.SMOOTH,
    "Smooth More": ImageFilter.SMOOTH_MORE,
    "Box Blur": ImageFilter.BoxBlur(10),
    "Gaussian Blur": ImageFilter.GaussianBlur(35),
    "Unsharp Mark": ImageFilter.UnsharpMask,
}

if __name__ == "__main__":
    for key, value in filters.items():
        with Image.open("img/aslan.jpg") as im:
            im = im.filter(value)
            im.save(f"saved/aslan-{key}.jpg")
