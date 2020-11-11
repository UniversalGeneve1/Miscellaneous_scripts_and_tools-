"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation. Valid operators are +, -, *, /. Each operand may be an integer or another expression. For example:

  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
"""

from operator import add, mul, sub, floordiv
def RPNCalc(notation):
  stack = []
  ops = {"+":add, "-": sub, "*": mul, "/": floordiv}
  for sym in notation:
    if sym not in ops.keys():
      stack.append(int(sym))
    else:
      stack.append(ops[sym](stack.pop(-2), stack.pop(-1)))
  return stack[0]

ex1 = ["2", "1", "+", "3", "*"]
ex2 = ["4", "13", "5", "/", "+"]

#test examples
print(RPNCalc(ex1))
print(RPNCalc(ex2))

"""
NOTES:
* this evaluates with integer division. to change to float division,
  replace all instances of the word "floordviv" with "trudiv"
"""