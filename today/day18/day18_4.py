# popular module in python
## string

## os
import os
from urllib.request import urlopen

print(os.getcwd())

## input and output
string = input('Masukkan sesuatu: ')
print(f'ini adalah input yang anda masukan: {string}')

## pickle
import pickle
contoh_dictionary = {1:'6', 2:'2', 3:'f'}
pickle_keluar = open('dict.pickle','wb')
pickle.dump(contoh_dictionary, pickle_keluar)
pickle_keluar.close()

pickle_masuk = open('dict.pickle','rb')
contoh_dictionary = pickle.load(pickle_masuk)

## json
import json

# contoh json
x = '{"nama":"Buchori", "umur":22, "Kota":"New York"}'

# parse x:
y = json.loads(x)

print(y["umur"])

## scrapper

### urrlib
url = "http://python.org/"
page = urlopen(url)
html = page.read().decode("utf-8")
start_index = html.find("<title>") + len("<title>")
end_index = html.find("</title>")
title = html[start_index:end_index]
title

### Beautifulsoup
# url = "http://python.org/"
# page = urlopen(url)
# html = page.read().decode("utf-8")
# soup = Beautifulsoup(html, "html.parser")
# soup.title

## Regex (re)
import re

pola='^a...s$'
string_tes= 'abiss'
hasil= re.match(pola, string_tes)

if hasil:
    print('Pencarian berhasil.')
else:
    print('Pencarian gagal.')

## Argumnt Parser (argparse)
import argparse
 
parser = argparse.ArgumentParser()
parser.add_argument('-o', '--output', action='store_true', help="tampilkan output")
args = parser.parse_args()
 
if args.output:
    print("Halo, ini merupakan sebuah output mengunakan argparse")