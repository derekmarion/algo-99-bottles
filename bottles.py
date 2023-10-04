def bottle_song(bottles):
	count = bottles
	while count > 0:
		if count != 1:
			print(f"{count} bottles of beer on the wall, {count} bottles of beer.")
		else:
			print(f"{count} bottle of beer on the wall, {count} bottle of beer.")
		if count > 0:
			print(f"Take one down and pass it around, {count -1} bottles of beer on the wall.")
		count -= 1
	print("No more bottles of beer on the wall, no more bottles of beer.")
	print(f"Go to the store and buy some more, {bottles} bottles of beer on the wall.")	