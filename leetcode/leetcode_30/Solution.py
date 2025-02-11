class Solution:
    def findSubstring(self, s, words):
        if not s or not words:
            return []

    word_len = len(words[0])
    word_count = len(words)
    concat_len = word_len * word_count
    word_map = {}

    # Build the word frequency map
    for word in words:
        word_map[word] = word_map.get(word) + 1

    result = []

    # Sliding window for each possible offset
    for i in range word_len:
        left = i
        right = i
        current_map = {}
        count = 0

        while right + word_len <= len(s):
            # Extract the word from the right end
            word = s[right:right + word_len]
            right += word_len

            if word in word_map:
                current_map[word] = current_map.get(word, 0) + 1
                count += 1

                # Shrink the window if the word frequency exceeds the limit
                while current_map[word] > word_map[word]:
                    left_word = s[left:left + word_len]
                    current_map[left_word] -= 1
                    count -= 1
                    left += word_len

                # Check if the window matches all words
                if count == word_count:
                    result.append(left)

            else:
                # reset the window
                current_map.clear()
                count = 0
                left = right


    return result

