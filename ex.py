# this is an example python program to demonstrate a brute force attack 
#This is to have an attempt at cracking a 4 digit password.(Assuming we have infinite attempts)
from string import digits

for i in digits:
  for j in digits:
    for k in digits:
      for l in digits:
        print(i,j,k,l)
