# Mutations
def mutate_string(word, index, letter):
 return word[:index] + letter + word[index+1:]
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)