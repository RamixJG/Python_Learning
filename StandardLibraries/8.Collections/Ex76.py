from collections import deque

wishlist = deque([])

wishlist.extend(['003','001','004','002','005'])

print(wishlist.popleft())