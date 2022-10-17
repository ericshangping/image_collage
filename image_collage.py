from PIL import Image

rows = 3
cols = 3

ss = Image.open("SLAM JAM FINAL.jpg")
w = ss.width
h = ss.height

out = Image.new('RGB', size=(cols*w, rows*h))

for x in range(rows):
    for y in range(cols):
        out.paste(ss, (x*w, y*h))

out.show()
out.save("output.jpg")
