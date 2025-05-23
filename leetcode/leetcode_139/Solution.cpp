def wordBreak(s, wordDict):
    word_set = set(wordDict)
    dp = [false] * (len(s) + 1)
    dp[0] = true

    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break

    return dp[len(s)]        
