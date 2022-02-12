def ekstrasi_data():
    """
    Tanggal: 11 Februari 2022, 21:25:16 WIB
    Magnitude: 5.2
    Kedalaman: 10 km
    Lokasi: 5.77 LU - 124.43 BT
    Pusat: 267 km BaratLaut TAHUNA-KEP.SANGIHE-SULUT
    Keterangan: tidak berpotensi TSUNAMI
    """

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


def menampilkan_data(result):
    print('Aplikasi Deteksi Gempa Terkini')
    print(f"Tanggal: {result['tanggal']}")
    print(f"Magnitude: {result['magnitude']}")
    print(f"Kedalaman: {result['kedalaman']}")
    print(f"Lokasi: LU: {result['lokasi']['lu']} BT: {result['lokasi']['bt']}")
    print(f"Pusat: {result['pusat']}")
    print(f"Keterangan: {result['keterangan']}")
