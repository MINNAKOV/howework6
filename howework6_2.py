my_dict = {'Sait Petersburg': 34242156342, "Moscow": 7878970, 'Samara': 455667392390}
print(my_dict.get('Sait Petersburg'))
print(my_dict.get('Novgorod'))

my_dict.update({'Kazan': 4345345235,'Saratov': 2423423525})

print(my_dict)

del my_dict['Moscow']
print(my_dict)

#my_dict.pop("Samara")
#print(my_dict)
#print(my_dict.items())
#print(my_dict.values())

set_ = {1, 11, 22, 31, 1, "Stavropol", False, (123, 2221)}
print(set_)
print(set_.add(5))
print(set_.add(123344))
print(set_)
print(set_.remove(22))
print(set_)

