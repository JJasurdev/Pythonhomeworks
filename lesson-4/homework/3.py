def insert_underscore(txt):
    vowels = 'aeiou'
    result = []
    count = 0

    for i, ch in enumerate(txt):
        result.append(ch)
        count += 1
        
    
        if count == 3:
            count = 0
            if ch in vowels:
                # Add underscore after the next character if it exists
                if i + 1 < len(txt):
                    result.append(txt[i + 1])
                    result.append('_')
                    count = 0
                else:
                    break
            else:
                if i + 1 < len(txt):
                    result.append('_')

    return ''.join(result)


# Test cases
print(insert_underscore("hello"))  # hel_lo
print(insert_underscore("assalom"))  # ass_alom
print(insert_underscore("abcabcdabcdeabcdefabcdefg"))  # abc_abcd_abcdeab_cdef_abcdefg
