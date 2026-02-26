cars = ["ok","ok","ok","ok","ok","ok","ok","ok","ok","ok","ok"]

# this is Break example

for status in cars:
    if status == 'faulty':
         print("Stopping the production line")
         break
        
    print(f"car is {status}")
    print("shipping this car to customer")
    
    
    
# this is continue example
# in the for loop in python we can use else with the foe loop like below and elow is the example 
for status in cars:
    if status == 'faulty':
        print("found faulty car, skipping ...")
        continue
    
    print(f"car is {status}")
    print("shipping this car to customer!!")
else:
    print("all the cars are successfully build and shipped to customers")
    
    
# nested for loop for finding prime number 

for n in range(2,10):
    for x in range (2 , n):
        if n % x == 0:
            print(f"{n} equals {x} * {n//x}")
            break
    else:
        print(f"{n} is a prime number")

