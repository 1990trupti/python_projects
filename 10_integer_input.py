
print("Take 10 integer inputs from user and store them in a list and print them on screen")

list = []
n = 10
for i in range(0,n):
    list.append(i)
print(list)

print("-------------------------------------------------------------------------------------------")
print("using function")

def store_in_list(list):
      list1 = []
      for i in range(0, list):
            list1.append(i)
      print(list1)
list = 10
store_in_list(list)



print("========================================================================================")
print("Take 10 integer inputs from user and store them in s list. Again Ask"
      "user to give a number. Now, tell user whether that number is present in list or not"
      "(Iterate over list using while loop)")

list1 = []
n = 10
for i in range(0,n):
    list1.append(i)
print(list1)
n1 = 6
if n1 in list1:
    print("Number is present in the list")
else:
    print("Number is not present in the list")



print("=================================================================================================================")
print("Take 20 integer inputs from user and print the following:"
      "number of positive numbers"
      "number of negative numbers"
      "number of odd numbers"
      "number of even numbers"
      "number of 0s")

def numbers(numbers):
      positive_num = 0
      negative_num = 0
      odd_num = 0
      even_num = 0
      zero_num =0

      for num in numbers:
            if num > 0:
                  positive_num += 1
            elif num < 0:
                  negative_num += 1

            if num % 2 == 0:
                  even_num += 1
            else:
                  odd_num += 1

            if num == 0:
                  zero_num += 1

      print("Number of positive numbers: ", positive_num)
      print("Number of negative numbers: ", negative_num)
      print("Number of odd numbers: ", odd_num)
      print("Number of even numbers: ", even_num)
      print("Number of zeros: ", zero_num)

numbers = []
for i in range(20):
      num = int(input("Enter an integer: "))
      numbers.append(num)

numbers(numbers)





print("=====================================================================================")
print("Take 10 integer inputs from user and store them in a list. "
      "now, copy all the elements in another list but in reverse order. ")

n3 = 10
list =[]
for i in range(0,n3):
    list.append(i)
print("Original List ", list)
list.reverse()
print("Reversed List", list)

# =======================================================================================
print("Write a program to find the sum of all elements of a list")

num = 10
list = []
for i in range(0,num):
    list.append(i)
print(list)
total = sum(list)
print(total)

print("=======================================================================================")
print("Write a program to find the product of all elements of a list")
def multiply_list(list):
      n = 1
      for i in list:
            n = n*i
      return n

list1 = [5,4,2]
print(multiply_list(list1))


print("=========================================================================================")
print("Initialize and print each element in new line of a list inside list.")

# list5 = [[4,5,2],[5,2],[8,4,6]]
# i = 0
# while i < len(list5):
#       j = 0
#       while j < len(list5[i]):
#             print(list5[i][j])
#             j = j+1
#       i = i+1


print(" ============================================================================")
print("Find largest and smallest elements of a list.")
list = [4,8,7,52,65,33,12]
list.sort()
print("sorted list: ",list)
print("Largest number of list is: ", list[-1])
print("Smallest number of list is: ", list[0])

print("======================================================================================")
print("Write a program to print sum, average of all numbers, smallest and largest element of a list.")
list = [54,7,2,56,42,22]

list.sort()
print("sorted list: ",list)

list2 = sum(list)
print("sum of list: ",list2)

list1 = sum(list) / len(list)
print("average of all numbers: ", list1)

print("Largest number of list is: ", list[-1])

print("Smallest number of list is: ", list[0])

print("====================================================================================")
print("Write a program to check if elements of a list are same or not it read from front or back"
      "e.g. 2   3   15   15     3   2")

# def front_back_same(list):
#       list = list.replace(" ", " ").split()
#
#
# list = [2,3,15,15,3,2]
# front_back_same(list)



print("=====================================================================")
print("Make a list by taking 10 input from user. Now delete all repeated elements of the list."
      "input-- [1,2,3,2,1,3,12,12,32]"
      "output-- [1,2,3,12,32]")

list1 = [1,2,3,2,1,3,12,12,32]
list2 = []
for i in list1:
      if i not in list2:
            list2.append(i)
print(list2)

def remove_duplicate(duplicates):
      not_duplicte = []
      for i in duplicates:
            if i not in not_duplicte:
                  not_duplicte.append(i)
      print(not_duplicte)

remove_duplicate([1,2,3,2,1,3,12,12,32])

print("================================================================================")
print("Take a list of 10 elements. split it into middle and store the elements in two different lists."
      "initial list-- 58  24  13  15  63  9  8  81  1  78"
      "After splitting-- 58  24  13  15  63"
      "                  9   8  81  1   78")

# initial_list = [58, 24, 13, 15, 63, 9, 8, 81, 1, 78]
# first_half =[]
# second_half =[]
# half = len(initial_list) /2
# print(half)
#
# for i in range(0,len(initial_list)):
#       if i < half:
#             initial_list.append(first_half)
#             print(first_half)
#       else:
#             initial_list.append(second_half)
#             print(second_half)






