def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
values_list = [54.32, 'asd', False]
values_dict = {'a' : 1, 'b' : 'Popup', 'c' : True}
values_list_2 = [54.32, 'Str']

print_params()
print_params(1, 25)
print_params(1, 'Str',[1, 2, 3])
print_params(*values_list)
print_params(**values_dict)
print_params(values_dict)
print_params(*values_dict)
print_params(**values_dict)
print_params(values_list_2)
print_params(*values_list_2)
print_params(*values_list_2, 42)
print_params(b=25)
print_params(c = [1,2,3])

values_list_2 = [54.32, 'Строка' ]