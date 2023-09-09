name_he = input('Enter his name: ')
name_she = input('Enter her name: ')
name = name_he + name_she
char_cnt = {}
#count = 0
def count_char(name):
    count1 = 0
    for char in name:
        if char in char_cnt:
            #count1 = count1 +  count
            char_cnt[char] += count
        else:
            count = 1
            char_cnt[char] =  count
    return  char_cnt
count_he = count_char(name)
#count_she = count_char(name_she)
print(count_he)
#print(count_she)