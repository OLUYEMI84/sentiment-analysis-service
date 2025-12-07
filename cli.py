import requests
import argparse

def send_request(url, text):
    response = requests.post(url + "/predict", json={"text": text})
    print(response.json())

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="Base URL of the service")
    parser.add_argument("text", help="Text to analyze")
    args = parser.parse_args()
    send_request(args.url, args.text)
