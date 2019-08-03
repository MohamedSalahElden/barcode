import numpy as np
import matplotlib.pyplot as plt
num0 = [1,0,1,0,0,1,1,0,1,1,0,1]
num1 = [1,1,0,1,0,0,1,0,1,0,1,1]
num2 = [1,0,1,1,0,0,1,0,1,0,1,1]
num3 = [1,1,0,1,1,0,0,1,0,1,0,1]
num4 = [1,0,1,0,0,1,1,0,1,0,1,1]
num5 = [1,1,0,1,0,0,1,1,0,1,0,1]
num6 = [1,0,1,1,0,0,1,1,0,1,0,1]
num7 = [1,0,1,0,0,1,0,1,1,0,1,1]
num8 = [1,1,0,1,0,0,1,0,1,1,0,1]
num9 = [1,0,1,1,0,0,1,0,1,1,0,1]
astr = [1,0,0,1,0,1,1,0,1,1,0,1]
whight = [0,0,0,0,0,0,0,0,0,0,0,0]


phone_number = input("enter your phone number")
print(phone_number)
barcode_decoding = whight  
barcode_decoding =barcode_decoding + astr
barcode_decoding  = barcode_decoding + [0]

print(phone_number)


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
barcode_decoding = barcode_decoding + astr
barcode_decoding  = barcode_decoding + [0]
barcode_decoding = barcode_decoding + whight
print (barcode_decoding)

for x in range(len(barcode_decoding)):
	if (barcode_decoding[x] == 0):
		barcode_decoding[x] = 1
	else :
		barcode_decoding[x] = 0
	pass

print (barcode_decoding)
image = np.array([barcode_decoding,barcode_decoding,barcode_decoding,barcode_decoding,barcode_decoding,barcode_decoding,barcode_decoding,barcode_decoding,barcode_decoding,barcode_decoding,barcode_decoding,barcode_decoding,barcode_decoding,barcode_decoding,barcode_decoding,barcode_decoding,barcode_decoding,barcode_decoding,barcode_decoding,barcode_decoding,barcode_decoding,barcode_decoding,barcode_decoding,barcode_decoding,barcode_decoding,barcode_decoding,barcode_decoding,barcode_decoding,barcode_decoding,barcode_decoding,barcode_decoding,barcode_decoding,barcode_decoding,barcode_decoding])

plt.axis('off')
plt.imshow(image , 'gray')
plt.savefig(phone_number)

plt.show()
