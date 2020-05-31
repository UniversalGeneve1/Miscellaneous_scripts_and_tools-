""" hackerrank Q to search for the number of digits in between two sets a and b
so that a divides into this set, and this set divides into b."""

def in_between(arr1, arr2):

  intermed_list = []
  results = []

  for num in range(min(arr1), min(arr2)+1):
    if all([1-(num % i) == 1 for i in arr1]):
      intermed_list.append(num) 

  for digit in intermed_list:
    if all([1-(j % digit) == 1 for j in arr2]):
      results.append(digit) 
  return len(results)