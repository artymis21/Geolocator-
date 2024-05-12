import requests

def get_ip_info(ip):
    url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url)
    data = response.json()
    return data

def generate_map_link(latitude, longitude):
    return f"https://www.google.com/maps/search/?api=1&query={latitude},{longitude}"

def main():
    ip = input("Enter the IP Address: ")
    ip_info = get_ip_info(ip)

    if ip_info['status'] == 'success':
        print("IP Address:", ip)
        print("Country:", ip_info['country'])
        print("City:", ip_info['city'])
        print("Latitude:", ip_info['lat'])
        print("Longitude:", ip_info['lon'])

        map_link = generate_map_link(ip_info['lat'], ip_info['lon'])
        print("Google Maps Link:", map_link)
    else:
        print("Failed to fetch IP information.")

if __name__ == "__main__":
    main()
