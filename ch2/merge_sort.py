from __future__ import print_function

def merge(a, p, r, q):
    sorted_a = []
    i = p
    j = r+1
    while i<=r and j<=q:
        if a[i]>a[j]:
            sorted_a.append(a[i])
            i+=1
        else:
            sorted_a.append(a[j])
            j+=1

    sorted_a.extend(a[i:r+1])
    sorted_a.extend(a[j:q+1])

    a[p:q+1] = sorted_a

def merge_sort(a, p=None, q=None):
    if p is None: p=0
    if q is None: q=len(a)-1

    if q-p>1:
        r = (p+q)//2
        merge_sort(a, p, r)
        merge_sort(a, r+1, q)
        merge(a, p, r, q)

if __name__ == '__main__':
    a = [5, 7, 8, 3, 1, 2]
    merge_sort(a)
    print(a)


