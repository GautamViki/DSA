def kth_symbol_grammar(n,k):
    if n==1 and k==1:
        return 0
    size = pow(2,n-1)
    mid = int(size/2)
    if k<=mid:
        return kth_symbol_grammar(n-1,k)
    else:
        return 1 if kth_symbol_grammar(n-1,k-mid)==0 else 1

print(kth_symbol_grammar(4,5))