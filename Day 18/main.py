import colorgram

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    r = color.rgb_colors.r
    g = color.rgb_colors.g
    b = color.rgb_colors.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)




































print(rgb_colors)
