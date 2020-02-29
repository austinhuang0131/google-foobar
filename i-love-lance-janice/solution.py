import string

def solution(xs):
  a = string.ascii_lowercase
  b = a[::-1]
  print "".join(map(lambda l: b[a.find(l)] if (a.find(l) != -1) else l,list(xs)))
  
# I wrote this file after submission so this may not be my exact answer...
# Should this fail hidden cases, let me know
