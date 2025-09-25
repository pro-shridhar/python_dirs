"""
Can contain duplicate items
Mutable: items can be modified, replaced, or removed
Ordered: elements maintain the order in which they were added
Index-based: items are accessed using their position (starting from 0)
Can store mixed data types (integers, strings, booleans, even other lists)
"""

list = [23, 34, 45, 56, 67, 78, 89]
list.append(90)
print(list)

list.extend([12, 11])
print(list)

list.insert(0, 9)
print(list)

"""pop(): Removes the element at a specific index or the last element if no
index is specified."""
list.remove(list[0])
print(list, " using remove")
list.pop()
print(list, " using pop")
list.pop(8)
print(list, " using pop with index")
del list[7]
print(list, " using del")

"""list List Comprehension"""
list1 = [1, 2, 3, 4, 5, 6]
list1 = [ele for ele in list1 if ele % 2 == 0]
print(list1)

print([val * 2 for val in list1])

a = [i for i in range(10)]
print(a)

arr2D = [[1, 2, 3], [4, 5], [7, 8, 9]]
print([element for row in arr2D for element in row])

freshfruit = ["  banana", "  loganberry ", "passion fruit  "]
print([word.strip() for word in freshfruit])
