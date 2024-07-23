def ascii_caesar_shift_decrypt(message, shift):
    decrypted = ""
    for char in message:
        new_value = ord(char) - shift
        
        if new_value < 32:
            new_value += 95 
        elif new_value > 126:
            new_value -= 95
        
        decrypted += chr(new_value)
    return decrypted

encrypted_message = """42m{y!"%w2'z{&o2UfX~ws%!._s+{ (&@Vwu{ (&@_w%{v{(&0"""

for i in range(-100, 100):
    print(ascii_caesar_shift_decrypt(encrypted_message, i))
