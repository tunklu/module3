def test(*params):
    print(params)


def factoria(n):
    if n == 1:
        return n
    else:
        return n * factoria(n - 1)


test('adf', False, 828)
print(factoria(int(input('Введите число n: '))))
