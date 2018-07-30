import json, codecs

with open('data_bruta.txt', encoding="utf-8") as f:
    lines = f.readlines()

dict_champ = dict()
dict_nomes = dict()
dict_links = dict()
dict_imgs = dict()

a = b = c = 0

for line in lines:
    line = line.rstrip()
    if line.startswith('https:'):
        dict_imgs[a] = line
        a = a + 1
    elif line.startswith('"'):
        aux = line.split('"')
        dict_links[b] = aux[3]
        b = b + 1
    else:
        dict_nomes[c] = line
        c = c + 1

for x in range(140):
    dict_champ[dict_nomes[x]] = {
        "nome":dict_nomes[x],
        "img":dict_imgs[x],
        "url":dict_links[x]
        }

with open('champs_name.json', 'wb') as f:
    json.dump(dict_nomes, codecs.getwriter('utf-8')(f), ensure_ascii=False)

with open('champs_link.json', 'wb') as f:
    json.dump(dict_links, codecs.getwriter('utf-8')(f), ensure_ascii=False)

with open('champs_img.json', 'wb') as f:
    json.dump(dict_imgs, codecs.getwriter('utf-8')(f), ensure_ascii=False)
 
with open('champs.json', 'wb') as f:
    json.dump(dict_champ, codecs.getwriter('utf-8')(f), ensure_ascii=False)
