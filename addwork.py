def calculate_structure_sum(*args):
    return sum(calculate_structure_sum(*a) if hasattr(a, '__iter__') else (type(a) in (int, float)) (a) for a in args)

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)


