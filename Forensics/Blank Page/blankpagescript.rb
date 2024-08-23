blank_file = "TheMessage.txt"

data = File.read(blank_file)

message = ""

for i in 0...data.length
    if data[i] == " "
        message += "0"
    else
        message += "1"
    end 
end

puts message