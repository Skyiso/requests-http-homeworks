import requests
import os

class YaUploader:
    base_host = 'https://cloud-api.yandex.net:443/'
    def __init__(self, token: str):
        self.token = token

    def authorization(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def upload(self, file_path: str):
        url = 'v1/disk/resources/upload/'
        request_url = self.base_host + url
        params = {
            "path": file_path,
            'overwrite': True
            }
        response = requests.get(request_url, headers=self.authorization(), params=params)
        url_for_upload = response.json().get('href', '')
        with open('', 'r') as file:
            response2 = requests.put(url_for_upload, files={"file": file})


if __name__ == '__main__':
    path_to_file = ""
    token = ""
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)