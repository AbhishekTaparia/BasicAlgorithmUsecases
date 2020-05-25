# [1,4,2,3]->-1
# [2,3,1,4,2]->2
# [2,1,3,4,3,2,5]->3
# 1. number inside the array should be less then size of array and range should be 1-N(size of array)
# Ex-[12,3,5,14]->not valid

# solution 1

a1 = [1, 4, 2, 3]
a2 = [2, 3, 1, 4, 2]
a3 = [2, 1, 3, 4, 7, 1, 2, 3, 2, 5]


def firstDuplicate1(a):
    s = set()
    for i in range(len(a)):
        if a[i] in s:
            return a[i]
        else:
            s.add(a[i])
    return -1


def firstDuplicate2(a):
    for i in range(len(a)):
        if a[abs(a[i])-1] > 0:
            a[abs(a[i])-1] = -1*a[abs(a[i])-1]
        else:
            return a[i]
    return -1


print(firstDuplicate2(a1))
print(firstDuplicate2(a2))
print(firstDuplicate2(a3))
