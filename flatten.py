"""
Write a recursive function called flatten, which accepts an array of arrays and
returns a new array with all values flattened.
"""


def flatten(arr, ret = None):
  if ret == None:
    ret = []
  for elem in arr:
    if isinstance(elem, int):
      ret.append(elem)
    else:
      flatten(elem, ret)
  result = ret
  #ret = None
  return result

#TEST"
"""
print(flatten([1, 2, 3, [4, 5] ]))
#[1, 2, 3, 4, 5]
print(flatten([1, [2, [3, 4], [[5]]]]))
#[1, 2, 3, 4, 5]
print(flatten([[1],[2],[3]]))
#[1,2,3]
print(flatten([[[[1], [[[2]]], [[[[[[[3]]]]]]]]]]))
#[1,2,3]"""

"""
NOTES:

interesting case of abstactions that happens here. oftentimes beginners will choose to set
ret in line one as an empty list. thisd will cause the class instance to create a list, not
the function itelf, and make memory of previous function calls. tyhe above method shows a
solution to the issue.

"""