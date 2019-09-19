dict = {"cat" : "chat", "dog" : "chien", "horse" : "cheval"}

for key in dict.keys():
    print(key, "->", dict[key])


dict = {"cat" : "chat", "dog" : "chien", "horse" : "cheval"}

for english, french in dict.items():
    print(english, "->", french)

dict = {"cat" : "chat", "dog" : "chien", "horse" : "cheval"}

dict['cat'] = 'minou'
print(dict)
