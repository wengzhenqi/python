from random import randint

def qsort(seq):
    if len(seq) < 2:
        return seq

    middle = seq[0]
    small = []
    larger = []

    for item in seq[1:]:
        if item <= middle:
            small.append(item)
        else:
            larger.append(item)

    return qsort(small) + [middle] + qsort(larger)


if __name__ == '__main__':
    nums = [randint(1,100) for i in range(10)]
    print(nums)
    print(qsort(nums))