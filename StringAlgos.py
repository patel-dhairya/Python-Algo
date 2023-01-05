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


if __name__ == "__main__":
    print(all_anagrams("ramo mora lex xsl sxl"))
