#Create bytesarray
ba= bytearray([10,20,30,40])
#              0   1  2  3
print(type(ba)) #<class 'bytearray'>

ba[0] = 100  # bytearray is - mutable object
print(ba[0])
print(ba[1])
print(ba[2])
print(ba[3])
