# PYTHON CHEATSHEET
> *"When you arise in the morning, think of what a precious privilege it is to be alive to breath, to think, to enjoy, to love."*
> *- Marcus Aurelius*

 

## 1. LISTS []

 

* **List Methods:**
  * len( arg1 ) - returns length of list
  * append( arg1 ) - appends element
  * insert( position, value ) - inserts value into an element's position
  * pop() - removes and returns last element
  * clear() - clears and mutates the list
  * reverse() - reverses and mutates the list
  * sort() - orders and mutates list incrementally
  * copy() - copies list into another and prevents mutation

 

* **List Functions:**
  * concat = list1 + list2; concatenates the lists
  * slice = list[0:]; returns list from the 0 element to the last element
  * slice = list[-2:]; returns the second to last element from list
  * slice = list[::2]; returns list with every 2 elements
  * slice = list[::-2]; returns reversed list and every 2 elements
  * copy = list[:]; copies list into another and prevents mutation
  * copy = list(mylist); copies list into another and prevents mutation
  * squared = [ i * i for i in list]; returns list with squared elements ( i * i == element * element)