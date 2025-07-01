def find_subsequences(s, index=0, current=""):
    if index == len(s):
        return [current]
    include = find_subsequences(s, index + 1, current + s[index])
    exclude = find_subsequences(s, index + 1, current)
    return include+exclude

subsequences = find_subsequences("abc")
print(subsequences)
