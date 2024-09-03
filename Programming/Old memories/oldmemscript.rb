require 'chunky_png'

image1 = ChunkyPNG::Image.from_file('1.png')
image2 = ChunkyPNG::Image.from_file('2.png')

if image1.height == image2.height && image1.width == image2.width
    image1.height.times do |i|
        image1.width.times do |j|
            if image1[i,j] == image2[i,j]
                image1[i,j] = ChunkyPNG::Color('black')
            else
                image1[i,j] = ChunkyPNG::Color('white')
            end
        end
    end
end

image1.save("flag.png")

system("xdg-open flag.png")