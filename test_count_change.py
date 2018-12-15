def ordinal(n):
  suffix = ['th', 'st', 'nd', 'rd', 'th', 'th', 'th', 'th', 'th', 'th']

  if n < 0:
    n *= -1

  n = int(n)

  if n % 100 in (11, 12, 13):
    s = 'th'
  else:
    s = suffix[n % 10]

  return str(n) + s
print(ordinal(101))
