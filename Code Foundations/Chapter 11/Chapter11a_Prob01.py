def sort(elements):
    for i in range(1,len(elements)):
        j = i-1
        nxt = elements[i]
        while(elements[j] > nxt) and (j >= 0):
            elements[j+1] = elements[j]
            j = j-1
        elements[j+1] = nxt
    return elements

height = [5, 21, 14, 51, 30]
height = sort(height)
print(height)