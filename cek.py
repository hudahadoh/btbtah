import requests

def check_proxy(proxy):
    urls = [
        "https://www.google.com",
        # Tambahkan daftar URL yang ingin Anda coba akses di sini
    ]
    for url in urls:
        try:
            response = requests.get(url, proxies={"https": proxy}, timeout=5)
            if response.status_code == 200:
                print(f"Proxy {proxy} is working for URL: {url}")
                return True
        except requests.exceptions.ProxyError as pe:
            print(f"Proxy {proxy} is not working for URL: {url}. Proxy Error: {pe}")
        except Exception as e:
            print(f"Error occurred while checking proxy {proxy} for URL: {url}. Error: {e}")
    return False

def main():
    proxy_url = "https://raw.githubusercontent.com/ALIILAPRO/Proxy/main/http.txt"
    try:
        response = requests.get(proxy_url)
        if response.status_code == 200:
            proxies = response.text.splitlines()
            with open("good.txt", "w") as good_file:
                for proxy in proxies:
                    if check_proxy(proxy):
                        good_file.write(proxy + "\n")
    except Exception as e:
        print(f"Failed to fetch proxies from {proxy_url}. Error: {e}")

if __name__ == "__main__":
    main()
