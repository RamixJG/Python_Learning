import itertools

chessboard = itertools.product("ABCDEFGH", "12345678")
chessboard = ["".join(fields) for fields in chessboard]
#chessboard = map(lambda x : ''.join([item for item in x]), list(chessboard))
print(list(chessboard))