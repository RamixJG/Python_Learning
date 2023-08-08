from collections import deque

daynames = deque(['Mon.', 'Tue.', 'Wed.', 'Thu.', 'Fri.', 'Sat.', 'Sun.'])

daynames.appendleft(daynames[-1])
daynames.pop()

#daynames.rotate(1)

print(daynames)