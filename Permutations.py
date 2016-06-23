#!/usr/bin/python

def findPermutations(list, title):
	# Make sure the filename has the correct extension (if not, add it)
	if title[-4:] != ".txt":
		ext = ".txt"
		title = title + ext

	# Open file with correct privileges
	text_file = open(title, "w")

	# This is the meat of the program. 
	# 
	for x in range(0, len(list)):
		# Write the SKU to be matched into the file first
		# (for formatting reason in excel)
		# text_file.write("SKU: " + list[x] + "\n")

		# Loop through each SKU and add the others as matches
		for y in range(0, len(list)):
			# As long as it isn't matching against itself. That's silly.
			if list[x] != list[y]:
				text_file.write(list[x] + "	" + list[y] + "\n")
		# Below line is for formatting only
		# text_file.write("\n")
	print ""
	print "Process complete!"
	print ""
	

# Variable for while loop
check = True

# This is the list where the SKUs will be stored
skuList = []

while check:
	# First check to see if we've already gotten a text file from the user
	ans = raw_input ("Got your own file? Enter the filename here, otherwise type 'no': ")
	# If we do...
	if ans != "no":
		# Open with r/w privileges
		f = open(ans, "r+")
		# Split the file by lines into an array (THIS GETS RID OF THE NEWLINE CHARACTER)
		arr = f.read().splitlines()
		# Prompt for name
		title = raw_input ("What do you want to name the output file? ")

		# Do the thing
		findPermutations(arr, title)

		# Break out when done
		check = False
	else:
		# If not, they can enter their own numbers
		sku = raw_input ("Enter as many SKUs as you need, or type exit at any time:\n")
		while sku != "exit":
			# add the number to the list
			skuList.append(sku)
			print ""
			print("Current SKUs:") 
			print skuList
			print ""
			sku = raw_input("Next: ")

		# Once they've finished typing SKUS, prompt for file name and make the permutations
		if sku == "exit":
			check = False
			title = raw_input ("What do you want to name the output file? ")
			findPermutations(skuList, title)