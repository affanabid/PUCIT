def recursive_reverse(string):
    if string == '':
        return ''
    return recursive_reverse(string[1:]) + string[0]


print(recursive_reverse('affan'))
    



