# with Flyod hare and tortoise algo
a1 = [2, 1, 4, 3, 2]
a2 = [4, 6, 5, 2, 5, 1, 3]
a3 = [3, 4, 1, 6, 2, 7, 2, 1]


def findDuplicate(nums):
    h = nums[0]
    t = nums[0]
    while True:
        print(t, '--', h)
        t = nums[t]
        h = nums[nums[h]]
        if(t == h):
            break
    a = nums[0]
    b = t
    print("----")
    while a != b:
        print(a, '--', b)
        a = nums[a]
        b = nums[b]
    return a


# print(findDuplicate(a1))
# print(findDuplicate(a2))
print(findDuplicate(a3))
