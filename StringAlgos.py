from string import ascii_letters


def all_anagrams(string: str):
    """
    For given string s, find all possible anagrams
    :param string: str -> string s for finding anagrams
    :return: list of possible anagrams
    """
    ls = string.split(" ")
    dic = {}
    for word in ls:
        s = "".join(sorted(word))
        if s not in dic:
            dic[s] = [word]
        else:
            dic[s].append(word)
    answer = [dic[word] for word in dic if len(dic[word]) >= 2]
    return answer


def levenshtein(string_a: str, string_b: str) -> int:
    """
    Given two strings string_a and string_b how many operations are required to convert string_b to string_a
    Available operations - Insertion, deletion and substitution
    """
    length_a = len(string_a)
    length_b = len(string_b)

    table = [[i + j for j in range(length_b + 1)] for i in range(length_a + 1)]
    for i in range(length_a):
        for j in range(length_b):
            table[i + 1][j + 1] = min(table[i][j + 1] + 1,
                                      table[i + 1][j] + 1,
                                      table[i][j] + int(string_a[i] != string_b[j]))
    return table[length_a][length_b]


if __name__ == "__main__":
    print(all_anagrams("ramo mora lex xsl sxl"))
