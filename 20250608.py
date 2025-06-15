# age=20
#
# status="성인" if age>=18 else "미성년자"
# print(status)


def add(x, y):
    return x + y
def sub(x, y):
    return x - y


add_lambda=lambda x, y: x + y
sub_lambda=lambda x, y: x - y
print(add_lambda(1, 2))
print(sub_lambda(1, 2))