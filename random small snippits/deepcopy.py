import copy
#Deepcopy() create a new object with a complete copy of the original object
original_list = [1,2, [3, 4]]
copied_list = copy.deepcopy(original_list)
#Modify the copied list
copied_list[0] = 5
copied_list[2][0] = 6
#Print both lists
print("Original list:", original_list)
print("Copy list:", copied_list)