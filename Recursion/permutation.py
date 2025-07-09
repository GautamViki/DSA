def get_permutations(word,ans):
    if len(word)==0:
        print(ans)
        return
    for i in range(len(word)):
        get_permutations(word[:i]+word[i+1:],ans+word[i])

get_permutations('abc','')