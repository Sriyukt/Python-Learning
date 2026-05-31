# checking mutability for a string
print(f'\nchecking for mutability in a string')
test_string_1 = "Hello"
test_string_2 = test_string_1
print(f'test_string_1 refers to {test_string_1} and has id \t {id(test_string_1)}')
print(f'test_string_2 refers to {test_string_2} and has id \t {id(test_string_2)}')
test_string_1 = test_string_1 + "!"
print(f'test_string_1 refers to {test_string_1} and has id \t {id(test_string_1)}')
print(f'test_string_2 still refers to {test_string_2} and has id \t {id(test_string_2)}')

# checking mutability for a list
print(f'\nchecking for mutability in a list')
test_list_1 = [1, 2, 3]
test_list_2 = test_list_1
print(f'test_list_1 refers to {test_list_1} and has id \t {id(test_list_1)}')
print(f'test_list_2 refers to {test_list_2} and has id \t {id(test_list_2)}')
test_list_1.append(4)
print(f'test_list_1 refers to {test_list_1} and has id \t {id(test_list_1)}')
print(f'test_list_2 refers to {test_list_2} and has id \t {id(test_list_2)}')