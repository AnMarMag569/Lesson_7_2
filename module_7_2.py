def custom_write(file_name, strings):
    plik = open(file_name, 'w', encoding='utf-8')
    strings_positions = {}
    ns = 1
    bns = 0
    for strg in strings:
        plik.write(strg +'\n')
        strings_positions[ns, bns] = strg
        ns = ns + 1
        bns = plik.tell()
    plik.close()
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)