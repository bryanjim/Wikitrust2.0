from Firestore import Firestore

# Create object
f = Firestore()

id_a = "aaaa"
id_b = "bbbb"

data_a = {
    u"diff_moves": ["(A,B,C,D)", "(E,F,G,H)"],
    u"diff_trust": [11, 22],
    u"trust": 1,
}

data_b = {
    u"diff_moves": ["(I,J,K,L)", "(M,N,O,P)"],
    u"diff_trust": [88, 99],
    u"trust": 99,
}

print("Writing diff a...")
f.writeDiff(id_a, data_a)
print("Writing diff b...")
f.writeDiff(id_b, data_b)

print(f.readDiff(id_a))
print(f.readDiff(id_b))

