import random

list_subject = ['the goat', 'the school', 'the girl', 'xenolith', 'zeolite', 'the lepidolite', 'the aquifer', 'mantle',
                'some boys', 'some animals', 'Dr ifakolade']

list_verb = ['ate', 'defeated', 'ran', 'drove', 'kicked', 'drew', 'cut', 'crept', 'lacked', 'destroyed']

list_object = ['the fruit', "the food", "the black hood", "arrow", 'the gang', 'the cult']


def form_sent(x: list, y: list, z: list) -> str:
    i = 0
    while i < 10:
        print(random.choice(x) + " " + random.choice(y) + ' ' + random.choice(z))
        i = i + 1


print(form_sent(list_subject, list_verb, list_object))


def spec_form_sent(x: list, y: list, z: list, a: int) -> str:
    i = 0
    while i < a:
        print(random.choice(x) + " " + random.choice(y) + ' ' + random.choice(z))
        i = i + 1


def mod_uniq_sent(x: list, y: list, z: list, a: int) -> str:
    prot = []
    i = 0
    while i < (a + 1):
        prot.append(random.choice(x) + " " + random.choice(y) + ' ' + random.choice(z))
        i = i + 1

    for char in prot:
        for chara in prot:
            if char == chara:
                prot.remove(char)
                return " ,".join(prot)

    #


print(mod_uniq_sent(list_subject, list_verb, list_object, 5))
