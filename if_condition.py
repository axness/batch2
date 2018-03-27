# execute a block of statements if only the condition satisfies
"""
if condition:
    statements
    
if True:
  print "boolean"
  print "last statement"
print "out side if"
"""
a = 5
b = 10
c = 4
if a<b and a<c:
    print "I am in if condition"
    print "a is lesser"
    print "completing the block of statement"
print "outside the if"
