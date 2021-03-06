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
        print(content.text)
        # soup = BeautifulSoup(content)
        # print(soup.prettify())

        data = dict()
        data['tanggal'] = '11 Februari 2022, 21:25:16 WIB'
        data['magnitude'] = 5.2
        data['kedalaman'] = '10 km'
        data['lokasi'] = {
        'lu': 5.77,
        'bt': 124.43 
        }
        data['pusat'] = '267 km BaratLaut TAHUNA-KEP.SANGIHE-SULUT'
        data['keterangan'] = 'tidak berpotensi TSUNAMI'

        return(data)
    else:
        return None


def menampilkan_data(result):
    if result is None:
        print('Tidak bisa menampilkan data Gempa Terkini')
        return


    print('Aplikasi Deteksi Gempa Terkini')
    print(f"Tanggal: {result['tanggal']}")
    print(f"Magnitude: {result['magnitude']}")
    print(f"Kedalaman: {result['kedalaman']}")
    print(f"Lokasi: LU: {result['lokasi']['lu']} BT: {result['lokasi']['bt']}")
    print(f"Pusat: {result['pusat']}")
    print(f"Keterangan: {result['keterangan']}")
