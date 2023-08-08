from collections import deque

daynames = deque(['Tue.', 'Wed.', 'Thu.', 'Fri.', 'Sat.'])

daynames.appendleft("Mon.")
daynames.append("Sun.")

print(daynames)