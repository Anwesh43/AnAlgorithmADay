def swap_a_pair(arr1,arr2):
    s1 = sum(arr1)
    s2 = sum(arr2)
    n = (s1-s2)/2
    num_set = set([])
    for ar in arr1:
        num_set.add(ar)
    for ar in arr2:
        if ar+n in num_set:
            return (ar+n,ar)
    return None

print swap_a_pair([4, 1, 2, 1, 1, 2],[3, 6, 3, 3])
