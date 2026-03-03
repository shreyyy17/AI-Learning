# import lec_5_file_operations as file_operations
#
#
# file_operations.save_to_file('rolf','new_file_demo')


# 2nd way of import

# from  lec_5_file_operations import save_to_file, read_file
#
#
# save_to_file('rolf','new_file_demo')


## 3rd way of imporing while file in other folder

# from utils.common.lec_5_file_operations import save_to_file, read_file
# from utils.find import find_in
#
#
# data = read_file('new_file_demo')
# print(data)



## DUNDER NAME VARIABLE
# like __name__ etc.
from utils.common.lec_5_file_operations import save_to_file, read_file
from utils.find import find_in

print(__name__) #__main__ output

