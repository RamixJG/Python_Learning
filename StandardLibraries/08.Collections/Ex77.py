from collections import deque


wishlist = deque()

user_ids = ['003', '001', '004', None, '002', '005']

for user in user_ids:
    if not user:
        wishlist.clear()
    else:
        wishlist.append(user)

print(wishlist)