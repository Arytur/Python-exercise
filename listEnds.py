a = [5, 10, 15, 20, 25]


def first_and_last(list_a):
    new_list = list()
    new_list.append(list_a[0])
    new_list.append(list_a[-1])
    return new_list


print(first_and_last(a))
