n, m = map(int, input().split())

lines = list()
seleted_lines = list()

min_count = m

for _ in range(m):
    a, b = map(int, input().split())
    lines.append((b, a - 1))

lines.sort()

def possible():
    nums1 = [i for i in range(1, n + 1)]
    nums2 = [i for i in range(1, n + 1)]

    for _, st in lines:
        nums1[st], nums1[st + 1] = nums1[st + 1], nums1[st]
    for _, st in seleted_lines:
        nums2[st], nums2[st + 1] = nums2[st + 1], nums2[st]

    return nums1 == nums2

def find_min(cnt):
    global min_count
    
    if cnt == m :
        if possible():
            min_count = min(len(seleted_lines), min_count )
        return

    
    seleted_lines.append(lines[cnt])
    find_min(cnt + 1)
        
    seleted_lines.pop()
    find_min(cnt + 1) 


find_min(0)

print(min_count)