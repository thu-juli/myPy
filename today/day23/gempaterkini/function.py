import requests
from bs4 import BeautifulSoup

def ekstrasi_data():
    """
    Tanggal: 11 Februari 2022, 21:25:16 WIB
    Magnitude: 5.2
    Kedalaman: 10 km
    Lokasi: 5.77 LU - 124.43 BT
    Pusat: 267 km BaratLaut TAHUNA-KEP.SANGIHE-SULUT
    Keterangan: tidak berpotensi TSUNAMI
    """
    try:
        content = requests.get('https://www.bmkg.go.id/')
    except Exception:
        return None
    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')
        result = soup.find('ul', {'class':'list-unstyled'})
        result = result.findChildren('li')

        i = 0
        tanggal = None
        jam = None
        magnitude = None
        kedalaman = None
        ls = None
        bt = None
        lokasi = None
        keterangan = None

        for value in result:
            if i == 0:
                result = value.text.split(', ')
                tanggal = result[0]
                jam = result[1]
            if i == 1:
                magnitude = value.text
            if i == 2:
                kedalaman = value.text
            if i == 3:
                result = value.text.split(' - ')
                ls = result[0]
                bt = result[1]
            if i == 4:
                lokasi = value.text
            if i == 5:
                keterangan = value.text

            i += 1


        data = dict()
        data['tanggal'] = tanggal
        data['jam'] = jam
        data['magnitude'] = magnitude
        data['kedalaman'] = kedalaman
        data['koordinat'] = {
        'ls': ls,
        'bt': bt 
        }
        data['lokasi'] = lokasi
        data['keterangan'] = keterangan
        return data
    else:
        return None


def menampilkan_data(result):
    if result is None:
        print('Tidak bisa menampilkan data Gempa Terkini')
        return

    print('Aplikasi Deteksi Gempa Terkini')
    print(f"Tanggal: {result['tanggal']}")
    print(f"Jam: {result['jam']}")
    print(f"Magnitude: {result['magnitude']}")
    print(f"Kedalaman: {result['kedalaman']}")
    print(f"Koordinat: {result['koordinat']['ls']} - {result['koordinat']['bt']}")
    print(f"Lokasi: {result['lokasi']}")
    print(f"Keterangan: {result['keterangan']}")
