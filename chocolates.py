def max_points(chocolates,initial):
  chocolates=sorted(chocolates)
  points=1
  l=[1]
  i=0
  while i < len(chocolates):
    if chocolates[i]<=initial:
      initial=initial-chocolates[i]
      points+=1
      i+=1
    else:
      points-=1
      initial+=chocolates[-1]
      chocolates.pop()
    l.append(points)
  return max(l)
# Example usage:
chocolates_list = list(map(int, input().split()))  # Input list of chocolates
initial_chocolates = int(input())  # Initial chocolates Bittu has
result = max_points(chocolates_list, initial_chocolates)
print(result,end="")