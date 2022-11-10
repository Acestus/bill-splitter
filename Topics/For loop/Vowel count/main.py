import TODO as TODO

string = "red yellow fox bite orange goose beeeeeeeeeeep"
vowels = 'aeiou'
counter = 0

for i in vowels:
    #print(i, string.count(i))
    counter += string.count(i)
print(counter)


