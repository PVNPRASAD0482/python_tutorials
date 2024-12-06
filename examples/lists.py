numbers = [10,3,5,8,2,-3,-9]
names = ['Prasad','Nani','Siva','Krishna','Nithin']
mix_list=['Nithin',0,True,10.10]

print(numbers)          // o/p:[10,3,5,8,2,-3,-9]
print(names)           // o/p:['Prasad','Nani','Siva','Krishna','Nithin']
print(mix_list)        // o/p:['Nithin',0,True,10.10]

print(numbers[0])      // o/p:10
print(numbers[4])     // o/p:2
print(numbers[-1])    // o/p:-9 (because it return the back word order)
print(numbers[0:4])   // o/p:[10, 3, 5, 8]
print(numbers[:5])    // o/p:[10, 3, 5, 8, 2] (by default it will start 0th index)
print(numbers[0:5:2]) // o/p:[10, 5, 2] (it is leaving middle digit)

numbers.sort()
print(numbers)        // o/p:[-9, -3, 2, 3, 5, 8, 10]

numbers.reverse()
print(numbers)        // o/p:[-9, -3, 2, 8, 5, 3, 10]

print(min(numbers))   // o/p:-9
print(max(numbers))   // o/p:10

numbers.insert(2,15)
print(numbers)        // o/p:[10, 3, 15, 5, 8, 2, -3, -9] (the value 15 is inset in the 2 index)

numbers.extend([15,17,19,32,55])
print(numbers)        // o/p: [10, 3, 5, 8, 2, -3, -9, 15, 17, 19, 32, 55] (it is extend the list)

numbers.remove(5)
print(numbers)        // o/p:[10, 3, 8, 2, -3, -9]  (it is removed 5)

numbers.pop()
print(numbers)        // o/p:[10, 3, 5, 8, 2, -3]    (it is remove last digit in the list)

print(numbers.pop(5))
print(numbers)         // o/p:[10, 3, 5, 8, 2, -9]    (it is removing the 5th digit)
