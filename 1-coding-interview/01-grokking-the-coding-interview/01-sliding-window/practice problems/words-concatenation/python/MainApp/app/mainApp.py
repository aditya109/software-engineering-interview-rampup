import sys


class MainApp:
    def __init__(self):
        pass
    '''
    Given an array of strings words (without duplicates), return all the concatenated words in the given list of words.

    A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

    Example 1:

    Input: words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
    Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
    Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats"; 
    "dogcatsdog" can be concatenated by "dog", "cats" and "dog"; 
    "ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
    Example 2:

    Input: words = ["cat","dog","catdog"]
    Output: ["catdog"]
    '''

    '''
    Input :
    words -> list of unique words

    Output :
    result -> list of words which are a result of concatenation between words present in `words`

    TPFS:
    1.  we convert the `words` into a set. That way searching would result in O(1)
    2.  we take each word from `words` and iterate it through all the 0 to length(word).
        cat sdogcats
          ^
          i

    '''

    # def is_word_composite(self, word, wordset) -> bool:
    #     if word in wordset:
    #         return True
    #     for i in range(len(word), 0, -1):
    #         if word[:i] in wordset and self.is_word_composite(word[i:], wordset):
    #             return True
    #     return False

    # def run(self, words):
    #     wordset = set(words)
    #     result = []
    #     for word in words:
    #         wordset.remove(word)
    #         if self.is_word_composite(word, wordset):
    #             result.append(word)
    #         wordset.add(word)
    #     return result

    def run(self, words):
        wordset = set(words)

        def check(word):
            word_length = len(word)
            for word_index in range(word_length-1, 0, -1):
                if word[word_index:] not in wordset:
                    continue
                if word[:word_index] in wordset:
                    return True
                if check(word[:word_index]):
                    return True
            return False
        result = []
        for word in words:
            if check(word):
                result.append(word)
        return result
