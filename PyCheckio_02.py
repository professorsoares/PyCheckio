from timeit import timeit as t


def first_word(text: str):
    return text[:text.find(" ")] if text.find(" ") != -1 else text


def first_word_1(text: str):
    index = text.find(" ")
    return text[:index] if index != -1 else text


def say(text1: str):  # (var: from type string)
    return text1.split(" ")[0]


if __name__ == '__main__':
    print("Example:")
    print(first_word("Hello world"))

    print(t('first_word(x)', setup='x = "asdf we"*10', number=10000, globals=globals())*1000)  # ~13.1 ms
    print(t('first_word(x)', setup='x = "asdfawe"*10', number=10000, globals=globals()) * 1000)  # ~71.1 ms
    print(t('first_word(x)', setup='x = "asdf we"*100000', number=10000, globals=globals()) * 1000)  # ~13.1 ms
    print(t('first_word(x)', setup='x = "asdfawe"*100000', number=10000, globals=globals()) * 1000)  # ~788793.7 ms
    print("----------------------------------------------")

    print(t('first_word_1(x)', setup='x = "asdf we"*10', number=10000, globals=globals()) * 1000)  # ~13.1 ms
    print(t('first_word_1(x)', setup='x = "asdfawe"*10', number=10000, globals=globals()) * 1000)  # ~71.1 ms
    print(t('first_word_1(x)', setup='x = "asdf we"*100000', number=10000, globals=globals()) * 1000)  # ~13.1 ms
    print(t('first_word_1(x)', setup='x = "asdfawe"*100000', number=10000, globals=globals()) * 1000)  # ~788793.7 ms

    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word("a word") == "a"
    assert first_word("hi") == "hi"
    print("Coding complete? Click 'Check' to earn cool rewards!")

    print("----------------------------------------------")

    print(say("kkk teste 123"))
    print("kkk teste 123".split(" ")[0])

    text0 = "teste 123"
    print(text0[0:text0.find(" ")])

print("----------------------------------------------")
#
#
# def first_word(text: str):
#     return str.split(" ")[0]
#
#
# if __name__ == '__main__':
#     print("Example:")
#     print(first_word("Hello world"))
#
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert first_word("Hello world") == "Hello"
#     assert first_word("a word") == "a"
#     assert first_word("hi") == "hi"
#     print("Coding complete? Click 'Check' to earn cool rewards!")
#

# FIM -------------------------------------------------------------------------------------------------
# PESQUISAS:
# https://stackoverflow.com/questions/2294493/how-to-get-the-position-of-a-character-in-python

# https://www.datacamp.com/community/tutorials/python-string-split?utm_source=adwords_ppc&utm_campaignid=1455363063&utm_adgroupid=65083631748&utm_device=c&utm_keyword=&utm_matchtype=b&utm_network=g&utm_adpostion=&utm_creative=278443377095&utm_targetid=aud-763347114660:dsa-429603003980&utm_loc_interest_ms=&utm_loc_physical_ms=9100780&gclid=CjwKCAjw8KmLBhB8EiwAQbqNoN8fOZH73IXR-kaR6eod4skuprSHzUKVerVepOfYBCsa9bwjc_Mw5hoCDswQAvD_BwE

# https://www.w3schools.com/python/ref_string_split.asp

# https://docs.python.org/pt-br/3.8/library/stdtypes.html


######################################################
# EXPLANATION #
#
# """
# It's worth to look at the performance of different methods under the same predefined conditions.
# Let's check runtime of the 4 methods (10000 executions for each) defined below for the next 4 cases:
# -a short str which contains space chars: "asdf we"*10;
# -a short str which doesn't contain space chars: "asdfawe"*10;
# -a long str which contains space chars: "asdf we"*100000;
# -a long str which doesn't contain space chars: "asdf we"*100000.
# ############################################################################################################
# from timeit import timeit as t
#
#
# def first_word_1(text):
#     return text.split(" ")[0]
#
# print(t('first_word_1(x)', setup='x = "asdf we"*10', number=10000, globals=globals()))       #  ~11.7 ms
# print(t('first_word_1(x)', setup='x = "asdfawe"*10', number=10000, globals=globals()))       #  ~6.1 ms
# print(t('first_word_1(x)', setup='x = "asdf we"*100000', number=10000, globals=globals()))   #  ~90928.2 ms
# print(t('first_word_1(x)', setup='x = "asdfawe"*100000', number=10000, globals=globals()))   #  ~5562.9 ms
#
#
# def first_word_2(text):
#     index = text.find(" ")
#     return text[:index] if index != -1 else text
#
# print(t('first_word_2(x)', setup='x = "asdf we"*10', number=10000, globals=globals()))       #  ~6.3 ms
# print(t('first_word_2(x)', setup='x = "asdfawe"*10', number=10000, globals=globals()))       #  ~4.7 ms
# print(t('first_word_2(x)', setup='x = "asdf we"*100000', number=10000, globals=globals()))   #  ~7.0 ms
# print(t('first_word_2(x)', setup='x = "asdfawe"*100000', number=10000, globals=globals()))   #  ~2108.4 ms
#
#
# def first_word_3(text):
#     try:
#         index = text.index(" ")
#         return text[:index]
#     except ValueError:
#         return text
#
# print(t('first_word_3(x)', setup='x = "asdf we"*10', number=10000, globals=globals()))       #  ~5.8 ms
# print(t('first_word_3(x)', setup='x = "asdfawe"*10', number=10000, globals=globals()))       #  ~8.5 ms
# print(t('first_word_3(x)', setup='x = "asdf we"*100000', number=10000, globals=globals()))   #  ~5.8 ms
# print(t('first_word_3(x)', setup='x = "asdfawe"*100000', number=10000, globals=globals()))   #  ~2005.8 ms
#
#
# def first_word_4(text):
#     index = -1
#     for pos, letter in enumerate(text):
#         if letter == " ":
#             index = pos
#             break
#     return text[:index] if index != -1 else text
#
# print(t('first_word_4(x)', setup='x = "asdf we"*10', number=10000, globals=globals()))       #  ~13.1 ms
# print(t('first_word_4(x)', setup='x = "asdfawe"*10', number=10000, globals=globals()))       #  ~71.1 ms
# print(t('first_word_4(x)', setup='x = "asdf we"*100000', number=10000, globals=globals()))   #  ~13.1 ms
# print(t('first_word_4(x)', setup='x = "asdfawe"*100000', number=10000, globals=globals()))   #  ~788793.7 ms
# ############################################################################################################
# So what conclusions can be made from all of this?
#
# 1.Since every string is an instance of the string class, it's preferred to use its methods rather than implement
# a new function which seems to be faster. It won't work faster in most of the cases. Compare first_word_2 and
# first_word_4 for example.
#
# 2.Despite the fact first_word_1 (which uses .split() method) looks nice and concise it works worse with long strings
# than first_word_2 and first_word_3 do(they use .find() and .index() methods respectively). Especially in case there are
# lots of spaces in the text.
#
# 3.str.index() method works a bit faster than str.find() but only in case there is a space in the text. Otherwise it's
# needed to handle an exception which takes some extra time.
#
# Thus, I'd use str.find() method in such kind of tasks.
# """