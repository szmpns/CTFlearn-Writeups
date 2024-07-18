import base64

a = "xD6kfO2UrE5SnLQ6WgESK4kvD/Y/rDJPXNU45k/p"

b = "h2riEIj13iAp29VUPmB+TadtZppdw3AuO7JRiDyU"

decoded_a = base64.b64decode(a)
decoded_b = base64.b64decode(b)

result = bytearray()

for i in range(min(len(decoded_a), len(decoded_b))):
    result.append(decoded_a[i] ^ decoded_b[i])



print(result.decode())