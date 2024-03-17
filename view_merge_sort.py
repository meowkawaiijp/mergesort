import matplotlib.pyplot as plt
import numpy as np
N = 100
array = np.random.rand(N)
array_original = array.copy()
fig, ax = plt.subplots()
bar_rects = ax.bar(range(len(array)), array, align="edge")
ax.set_xlim(0, N)
ax.set_ylim(0, int(1.1 * max(array)))
def merge_sort(arr, l, r):
    if l < r:
        m = (l + r) // 2
        merge_sort(arr, l, m)
        merge_sort(arr, m + 1, r)
        merge(arr, l, m, r)
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = arr[l:m + 1].copy()
    R = arr[m + 1:r + 1].copy()

    i = j = 0
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
def visualize_merge_sort(arr, l, r):
    if l < r:
        m = (l + r) // 2
        visualize_merge_sort(arr, l, m)
        visualize_merge_sort(arr, m + 1, r)
        merge(arr, l, m, r)
        ax.cla()
        ax.bar(range(len(array)), array, align="edge", color='g', alpha=0.6)
        ax.bar(range(l, r + 1), array[l:r + 1], align="edge", color='r')
        plt.pause(0.05)
visualize_merge_sort(array, 0, len(array) - 1)
plt.show()