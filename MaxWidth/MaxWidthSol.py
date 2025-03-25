S = input()
maxWidth = int(input())
list_words = S.split()
length = 0
words_in_line = 0
line = []
for i in range(len(list_words)):
    if (length+len(list_words[i])+words_in_line-1<=maxWidth ) :
        line += [list_words[i]]
        length += len(list_words[i])
        words_in_line += 1
    else:
        if words_in_line!=1:
            spaces_needed = (maxWidth-length)//(words_in_line-1)
            spaces_remaining = (maxWidth-length)%(words_in_line-1)
        else:
            spaces_needed = 0
            spaces_remaining = 0
        for j in line:
            if spaces_remaining!=0:
                print(j,end=" "*spaces_needed+" ")
                spaces_remaining -= 1
            else:
                print(j,end=" "*spaces_needed)
        print()
        line = []
        line += [list_words[i]]
        length = 0
        words_in_line = 0
        length += len(list_words[i])
        words_in_line += 1
if line != []:
    if words_in_line!=1:
        print((" ").join(line))
    else:
        print(("").join(line))
            

    
    
