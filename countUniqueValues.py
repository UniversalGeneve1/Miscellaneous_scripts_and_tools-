#unique values counter in a sorted list.


def countUniqueValues(arr):
  #arr = arr.sort()  
  if len(arr) == 0:
    print(0)
  else:
    counter = 1
    for i in range(1,len(arr)):
      if arr[i] != arr[i-1]:
        counter += 1
    print(counter)