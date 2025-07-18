def toh(n,s,a,d):
    if n==1:
        print(f"move disk from {s} to {d}")
        return
    toh(n-1,s,d,a)
    print(f"move disk from {s} to {d}")
    toh(n-1,a,s,d)

toh(4,'S','A','D')