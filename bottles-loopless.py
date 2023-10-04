def bottle_song(bottles):
    if bottles == 0:
        print("No more bottles of beer on the wall, no more bottles of beer.")
        print(f"Go to the store and buy some more, {bottles} bottles of beer on the wall.")	
        return
    if bottles != 1:
        print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
    else:
        print(f"{bottles} bottle of beer on the wall, {bottles} bottle of beer.")
    if bottles > 0:
        print(f"Take one down and pass it around, {bottles -1} bottles of beer on the wall.")
    return bottle_song(bottles - 1)