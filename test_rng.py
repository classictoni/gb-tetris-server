import random

max_rand_increase = 4
interval = 0

def update_div_register(div_register):
    return (div_register + interval + random.randint(0, max_rand_increase)) % 256
    
def generate_tiles_real(num_pieces):
    tiles = [
        "00", # L
        "04", # J
        "08", # I
        "0C", # O
        "10", # Z
        "14", # S
        "18"  # T
    ]
    div_register = random.randint(0, 255)
    pieces_array = []
    pieces_array.append(div_register % 7)
    div_register = update_div_register(div_register)
    pieces_array.append(div_register % 7)
    three = 0
    for i in range(2,num_pieces):
        for j in range(2):
            div_register = update_div_register(div_register)
            new_piece = div_register % 7
            # according to hard drop it compares the current piece to the OR clause (and not the new_piece)
            if pieces_array[i-2] != (pieces_array[i - 2] | pieces_array[i - 1] | new_piece):
                break
        pieces_array.append(new_piece)
        if pieces_array[i] == 2 and pieces_array[i-2] == pieces_array[i-1] and pieces_array[i-2] == pieces_array[i]:
            three += 1
    #return ''.join(list(map(lambda x : tiles[x], pieces_array)))
    #print(three)
    return pieces_array
    #return three


print('interval,L,J,I,O,Z,S,T')
for interval in range(256):
    pieces = generate_tiles_real(100000)
    a = [0 for i in range(7)]
    for piece in pieces:
        a[piece] += 1
    print(interval, end=',')
    for num_piece_a in a: 
        print(num_piece_a, end=',')
    print('')