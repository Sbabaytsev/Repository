class NonPositiveError(Exception):
    pass


class PositiveList(list):
    def append(self,x:int):
        if x <= 0:
            raise NonPositiveError
        super().append(x)

a = PositiveList ()
while True:
    x = int(input())
    a.append(x)
    print("x = ", x, "list = ", a)



