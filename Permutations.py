def findPermutations(list, title):
	ext = ".txt"
	text_file = open(title + ext, "w")
	for x in range(0, len(list)):
		text_file.write("SKU: " + list[x] + "\n")
		for y in range(0, len(list)):
			if list[x] != list[y]:
				toAdd = list[x] + "	" + list[y] + "\n" 
				text_file.write(toAdd)
		text_file.write("\n")
	print ""
	print "Process complete!"
	print ""
	


check = True
skuList = []
while check:
	sku = raw_input ("Enter SKU, or type exit: ")
	if sku == "exit":
		check = False
		title = raw_input ("What do you want to name the output file? ")
		findPermutations(skuList, title)
	elif len(sku) != 6:
		print ""
		print "Length might have been wrong..."
		print ""
	else:
		skuList.append(sku)
		print ""
		print("Current SKUs:") 
		print skuList
		print ""
