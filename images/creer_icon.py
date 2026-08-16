from PIL import Image, ImageDraw, ImageFont

for taille, nom in [(192, "icon-192.png"), (512, "icon-512.png")]:
    img = Image.new("RGB", (taille, taille), (20, 20, 40))
    draw = ImageDraw.Draw(img)

    draw.ellipse(
        (taille//6, taille//6, taille*5//6, taille*5//6),
        fill=(0, 150, 255)
    )

    draw.text(
        (taille//2, taille//2),
        "S",
        fill="white",
        anchor="mm"
    )

    img.save(nom)

print("Icônes PWA créées")
