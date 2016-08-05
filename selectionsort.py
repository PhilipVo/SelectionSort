from random import randint

def selectionSort(li):
	idx, start, i = 0, 0, 0
	min = li[idx]

	while i < len(li):
		# Find the min and save its index:
		if min > li[i]:
			min = li[i]
			idx = i

		# Once the end is reached and the min is found:
		if i == len(li) - 1:
			# Swap:
			temp = li[start]
			li[start] = min
			li[idx] = temp

			# Reset min to start of new array:
			start += 1
			# Don't go out of bounds:
			if start < len(li):
				i = start
				min = li[start]
				idx = start
				continue
			else:
				break

		i += 1




# li = [5,7,2,6,86,34,8,23]
li = []
for i in range (0, 100):
	li.append(randint(0, 10000))
print 'Unsorted:'
print li
print
selectionSort(li)
print 'Sorted:'
print li
