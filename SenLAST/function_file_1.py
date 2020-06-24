# initializing list
test_list = [True, True, True, False]
flag = 0

# using naive method
# to check for False list
for i in test_list:
    if i == False:
        flag = 1
        break

# printing result
print("Is List completely true ? : " + str(bool(not flag)))