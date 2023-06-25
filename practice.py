
# Practice 1
def reverse_list(l):
    return l[::-1]

aList = [100, 200, 300, 400, 500]
reverse_list(aList)


# Practice 2
def concatenate_list(l1, l2):
    return [i+j for i, j in zip(l1, l2)]

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
concatenate_list(list1, list2)


# Practice 3
def square_list(l):
    return [i*i for i in l]

aList = [1, 2, 3, 4, 5, 6, 7]
square_list(aList)


# Practice 4
def concatenate_list2(l1, l2):
    return [i+j for i in l1 for j in l2]

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
concatenate_list2(list1, list2)


# Practice 5
def iterate_list(l1, l2):
    for x, y in zip(l1, l2[::-1]):
        print (x, y)

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
iterate_list(list1, list2)


# Practice 6
def remove_emptystr(l):
    return list(filter(None, l))

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
remove_emptystr(list1)


# Practice 7
def add_item(l):
    l[2][2].append(7000)
    return l

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
add_item(list1)


# Practice 8
def add_sublist(l, sl):
    l[2][1][2].extend(sl)
    return l

list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sublist = ["h", "i", "j"]
add_sublist(list1, sublist)


# Practice 9
def item_replace(l):
    l[l.index(20)] = 200
    return l

list1 = [5, 10, 15, 20, 25, 50, 20]
item_replace(list1)


# Practice 10
def item_remove(l, n):
    return [i for i in l if i != n]

list1 = [5, 20, 15, 20, 25, 50, 20]
item_remove(list1, 20)
