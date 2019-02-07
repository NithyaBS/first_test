#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      admin
#
# Created:     18/01/2019
# Copyright:   (c) admin 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    a = [] # start an empty list
    n = int(input("Enter no.of elements:")) # read number of element in the list
    for i in range(n):
      new_element = int(input("Enter element:")) # read next element
      a.append(new_element) #
    even_lst = []
    odd_lst = []
    count_even=0
    count_odd=0
    even=0
    odd=0
    for j in a:
     if j % 2 == 0:
        even_lst.append(j)
        count_even+=1
        even=even+j
     else:
        odd_lst.append(j)
        count_odd+=1
        odd=odd+j
    print("FullList: ",a)
    print("Even numbers list \t", even_lst)
    print("Number of even num:", count_even)
    print("sum of even no:",even)
    print("Odd numbers list \t", odd_lst)
    print("Number of odd num:", count_odd)
    print("sum of odd no:",odd)

if __name__ == '__main__':
    main()
