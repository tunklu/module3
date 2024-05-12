def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

values_list = [13, 'string', 15.5]
values_dict = {'a': 17, 'b': 'текст', 'c': False}
values_list_2 = [True, 234.34]

print_params()
print_params(b = 25)
print_params(c = [1, 2, 3])
print_params(* values_list)
print_params(** values_dict)
print_params(* values_list_2, 42)
