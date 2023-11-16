#Running Total
#National 5 Computing Science
#Mrs Brodie

'''Type 1
Running total from a set number of values input by the user
If the user were to be asked to enter five values one after the other #and without need to store the values in an array, the algorithm is as #follo'''

total=0
for counter in range (5):
  value=int(input("Please enter value "))
  total=total+value
print( "The total is ", total)

print("Now try type 2 running total")

'''Type 2
Running total from values in an array
In this example, the numbers to be added together are 
 already held in a 1D array of five integer values, so there is no need to request user input.'''

total2=0
numberlist=[2,3,4,5,6]
for number in numberlist:
  total2=total2+number
print( "The Total is ", total2)



print("Now try type 3 running total")


'''type 3
Running total from any number of values input by the user
If the functional requirements created during analysis state that the algorithm should accept any number of values (as opposed to a set number as in the previous examples), then the following algorithm could be used.'''

total3=0
carryOn=True
while carryOn==True:
  value3=int(input("Please enter value "))
  total3=total3+value3
  question=input("Do you want to continue? enter Yes or No ")
  if question=="No":
    carryOn=False
print( "The total is ", total3)


  
  



