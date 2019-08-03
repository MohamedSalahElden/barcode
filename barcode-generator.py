import numpy as np
import matplotlib.pyplot as plt
num0 = [1,0,1,0,0,1,1,0,1,1,0,1]	#0
num1 = [1,1,0,1,0,0,1,0,1,0,1,1]	#1
num2 = [1,0,1,1,0,0,1,0,1,0,1,1]	#2
num3 = [1,1,0,1,1,0,0,1,0,1,0,1]	#3
num4 = [1,0,1,0,0,1,1,0,1,0,1,1]	#4
num5 = [1,1,0,1,0,0,1,1,0,1,0,1]	#5
num6 = [1,0,1,1,0,0,1,1,0,1,0,1]	#6
num7 = [1,0,1,0,0,1,0,1,1,0,1,1]	#7
num8 = [1,1,0,1,0,0,1,0,1,1,0,1]	#8
num9 = [1,0,1,1,0,0,1,0,1,1,0,1]	#9
astr = [1,0,0,1,0,1,1,0,1,1,0,1]	#*
whight = [0,0,0,0,0,0,0,0,0,0,0,0]	#


# get phone number from user and print it back
phone_number = input("enter your phone number")
print(phone_number)

# add * character (starting character)
# add space of white bar 

barcode_decoding = astr
barcode_decoding = barcode_decoding + [0]

#constructing barcode binary decoding --- each character must be followed by a white bar spacer
for x in phone_number:
	if x == '0':
		barcode_decoding  = barcode_decoding + num0
		barcode_decoding  = barcode_decoding + [0]
		
		pass
	elif x == '1':
		barcode_decoding  = barcode_decoding + num1
		barcode_decoding  = barcode_decoding + [0]
		pass
	elif x == '2':
		barcode_decoding  = barcode_decoding + num2
		barcode_decoding  = barcode_decoding + [0]
		pass
	elif x == '3':
		barcode_decoding  = barcode_decoding + num3
		barcode_decoding  = barcode_decoding + [0]
		pass
	elif x == '4':
		barcode_decoding  = barcode_decoding + num4
		barcode_decoding  = barcode_decoding + [0]
		pass
	elif x == '5':
		barcode_decoding  = barcode_decoding + num5
		barcode_decoding  = barcode_decoding + [0]
		pass
	elif x == '6':
		barcode_decoding  = barcode_decoding + num6
		barcode_decoding  = barcode_decoding + [0]
		pass
	elif x == '7':
		barcode_decoding  = barcode_decoding + num7
		barcode_decoding  = barcode_decoding + [0]
		pass
	elif x == '8':
		barcode_decoding  = barcode_decoding + num8
		barcode_decoding  = barcode_decoding + [0]
		pass
	elif x == '9':
		barcode_decoding  = barcode_decoding + num9
		barcode_decoding  = barcode_decoding + [0]
		pass
	
# add stop character *
barcode_decoding = barcode_decoding + astr
print (barcode_decoding)

# convert 0 into white bars and 1 into black bars
# inverting the list 
for x in range(len(barcode_decoding)):
	if (barcode_decoding[x] == 0):
		barcode_decoding[x] = 1
	else :
		barcode_decoding[x] = 0
	pass

print (barcode_decoding)
#creating the image array of (len(barcode_decoding) , 20) 
image = np.array([barcode_decoding for i in range(20)])

#disable axis , show barcode and save it 
plt.axis('off')
plt.imshow(image , 'gray')
plt.savefig(phone_number)
plt.show()
