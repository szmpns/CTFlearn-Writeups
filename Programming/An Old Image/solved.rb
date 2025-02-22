require 'chunky_png'

image = ChunkyPNG::Image.from_file('old_image.png')

for x in 0...image.height
    for y in 0...image.width
    pixel_value = image[x, y]
    new_x = ChunkyPNG::Color.r(pixel_value)
    new_y = ChunkyPNG::Color.g(pixel_value)
    
    new_color = ChunkyPNG::Color.rgb(x, y, 0)
    
    image[new_x, new_y] = new_color
    end
end

image.save('flag.png')

system('xdg-open flag.png')