import itertools
 
 
def make_three(iterable):
    iter1, iter2, iter3 = itertools.tee(iterable, 3)
    next(iter3)
    return zip(
        itertools.chain([None], iter1),
        iter2,
        itertools.chain(iter3, [None]),
    )
 
 
print(f'[1, 2, 3, 4] -> {list(make_three([1, 2, 3, 4]))}')
print(
    f"['a', 'b', 'c', 'd', 'e'] -> "
    f"{list(make_three(['a', 'b', 'c', 'd', 'e']))}"
)
print(f"'Python' -> {list(make_three('Python'))}")