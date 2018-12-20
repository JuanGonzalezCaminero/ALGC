
def exponentiate(a, n):
    if n == 1:
        return a
    if n % 2 == 0:
        return exponentiate(a, n / 2) ** 2
    else:
        return a * exponentiate(a, n - 1)

print(exponentiate(3, 5))