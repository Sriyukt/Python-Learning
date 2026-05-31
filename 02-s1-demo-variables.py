print(f'The number 1 is stored by Python at an address referenced by \t\t\t\t{id(1)}')
print(f'The works "Hello" is stored by Python at an address referenced by \t\t\t{id("Hello")}')

my_var_1 = 1
print(f'The variable my_var_1 if it points to 1 references the memory location \t\t\t{id(my_var_1)}')

my_var_2 = my_var_1
print(f'The variable my_var_2 if it points to variable my_var_1 references the memory location \t{id(my_var_2)}')

my_var_1 = "Hello"
print(f'The variable my_var_1 if it points to "Hello" references the memory location \t\t{id(my_var_1)}')

my_var_2 = my_var_1
print(f'The variable my_var_2 if it points to variable my_var_1 references the memory location \t{id(my_var_2)}')

my_var_2 = 1
print(f'The variable my_var_2 if it points to 1 references the memory location \t\t\t{id(my_var_2)}')