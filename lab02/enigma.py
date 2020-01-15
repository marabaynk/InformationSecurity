from rotors import rotors_f, rotors_b, reflector, letters

shifts = [0 for i in range(len(rotors_f))]

encr = False

if (encr):
    src_file = "picture.jpg"
    dst_file = "picture_enc.jpg"
else:
    src_file = "picture_enc.jpg"
    dst_file = "picture_dec.jpg"
    
with open(src_file, "rb") as f:
    src = bytearray(f.read())
dst = bytearray()

for b in src:
    
    for inds, shift in zip(rotors_f, shifts):
        b = (inds[(b + shift) % letters] + shift) % letters;
    
    
    b = reflector[b]
    
    
    for inds, shift in zip(rotors_b[::-1], shifts[::-1]):
        b = (inds[(b - shift) % letters] - shift) % letters;
    
    
    shifts[0] += 1
    
    for i in range(len(shifts)-1):
        if shifts[i] == letters:
            shifts[i] = 0
            shifts[i+1] += 1

    dst.append(b)

with open(dst_file, "wb") as f:
    f.write(dst)
