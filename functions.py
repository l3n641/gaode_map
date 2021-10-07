def get_lat_lon_from_gaode(key, address):
    import requests
    url = f'https://restapi.amap.com/v3/geocode/geo?key={key}&address={address}&batch=false'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data['geocodes']:
                return data['geocodes'][0]['location']
        return ''
    except Exception:
        return None
