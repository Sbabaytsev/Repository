class EvenLengthMixin:
    def even_length(self):
        return len(self) % 2 == 0


class MyList(list, EvenLengthMixin):
    pass


ml = MyList([1, 12, 5, 32, 3, 6])
ml.sort()
print(ml)
