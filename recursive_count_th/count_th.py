'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    the_count = 0
    split = list(word)
    index = len(split) - 1

    def inner_func(i):
        nonlocal the_count
        if i == 0:
            return
        elif split[i] == 'h' and split[i - 1] == 't':
            the_count += 1
            inner_func(i - 1)
        else:
            inner_func(i - 1)

    if len(split) == 0:
        pass
    else:
        inner_func(index)
    
    return the_count