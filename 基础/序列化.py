import pickle

a1 = "haha"
a2 = 2435
a3 = [23,52,6,29]

with open("haha.dat", "wb") as f:
    pickle.dump(a1, f)
    pickle.dump(a2, f)
    pickle.dump(a3, f)
with open("haha.dat", "rb") as f:
    b1 = pickle.load(f)
    b2 = pickle.load(f)
    b3 = pickle.load(f)
    print(b1)
    print(b2)
    print(b3)
