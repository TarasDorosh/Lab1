print("type bool :", False,"\ntype Nonetype:", None)
x = [33,22,4343]
print(f'length of x is  {len(x)} ')
def forif(n=6):
    x = [33,22,4343]
    i = 1
    while i != n:
        if i % 2 == 0:
            for j in range(i):
                x.append(i)
        else:
            for j in range(i):
                x.pop()
        i = i + 1
    return x


print(forif())
try:
    print("What if pop many times from list:", forif(8))
except Exception as e:
    print(e)
finally:
    print("А вот воно що!")
with open("README.md", "a") as f:
    f.write('\n# end of Lab2a')
x = lambda a, b : a * b
print(x(10,20))

