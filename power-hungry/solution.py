def solution(xs):
  nonzero = filter(lambda x: x!=0, xs)
  positive_list = filter(lambda x: x>0, xs)
  positive = 1 if (not positive_list) else reduce(lambda x,y: x*y, positive_list)
  negative_list = filter(lambda x: x<0, xs)
  negative_min = 0 if (not negative_list) else max(negative_list)
  negative = 1 if (not negative_list) else reduce(lambda x,y: x*y, negative_list)
  negative = negative if (len(negative_list) % 2 == 0) else negative / negative_min
  product = 0 if (not nonzero) else (0 if (negative_list == nonzero and len(negative_list) == 1 and len(xs) > 1) else (negative_list[0] if (negative_list == nonzero and len(negative_list) == 1 and len(xs) == 1) else negative * positive))
  print str(product)
