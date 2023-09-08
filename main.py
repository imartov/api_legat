import os
import requests
from dotenv import load_dotenv


load_dotenv()
def get_api_data(url:str, unp:str) -> dict:
    ''' test function '''
    key = os.getenv("key")
    request_params = {"key": key, "unp": unp}
    response = requests.get(url=url, json=request_params)
    print(response)


def main():
    load_dotenv()
    url = os.getenv("URL_GET_BASIC_DATA")
    unp = "100128525"
    get_api_data(url=url, unp=unp)


if __name__ == "__main__":
    main()