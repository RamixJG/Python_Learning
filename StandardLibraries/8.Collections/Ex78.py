from collections import deque

wishlist = deque(maxlen=3)
user_ids = ['003', '001', '004', '006', '002', '005']

for user in user_ids:
    wishlist.append(user)
    print(wishlist)