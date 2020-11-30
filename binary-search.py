def binary_search(array, target):
  start = 0
  end = len(array)
  pivot = (start + end)//2 #this will make a smaller left array in case of even items
  while start != end:
    if target == array[pivot]:
      return pivot
    elif target < array[pivot]:
      end = pivot
      pivot = (start + end)//2
    else:
      start = pivot+1 #we dont want to take in numbers on the left side
      pivot = (start + end)//2
  
  return -1

arr = [1, 3, 4, 5, 7, 9, 10, 11, 13, 15, 16]
t = [1, 2, 3, 5, 6]

for elem in t:
  print(binary_search(arr, elem))