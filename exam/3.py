def check(my_str):
    brack = ['()', '{}', '[]']
    while any(x in my_str for x in brack):
        for br in brack:
            my_str = my_str.replace(br, '')
    return not my_str
str = input()
print(str, "-", "balanced"
if check(str) else "unbalanced")