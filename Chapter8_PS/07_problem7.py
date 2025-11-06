def remove(l,word):
    for item in l:
        l.remove(word) 
        return l


l = ["Manish", "Tannu", "Raghav", "Khushi"]

print(remove(l,"Raghav"))