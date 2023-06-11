import json
import requests
import re
import os

from core import getImageDirName
from core import getImageFileName

def getPageUrls(bookId):
    # 책의 각 페이지의 이미지 URL을 가져옴
    response = requests.get(f'https://ebook.mirae-n.com/@{bookId}/buk.json')
    parsed = json.loads(response.content)
    items = parsed['items']
    result = []
    for item in items:
        url = item['url']
        reSearch = re.search(r'html/(.*).xhtml', url)
        imageId = reSearch.group(1)
        result.append(imageId)
    return result

def downloadImages(bookId, imageIds):
    # 책의 각 페이지 이미지를 다운로드함
    print(f'Starting download of book with id {bookId}')
    dirName = getImageDirName(bookId)
    if not os.path.exists(dirName):
        os.makedirs(dirName)
    count = 0
    for i, imageId in enumerate(imageIds):
        image = requests.get(
            f'https://ebookmirae-ncom.contents.buk.io/@{bookId}'
            f'/static/images/{imageId}.jpg'
        ).content
        with open(f'{dirName}/{getImageFileName(i+1)}', 'wb') as f:
            f.write(image)
            count += 1
            print(f' - Downloaded page {count}')
    print(f'Completed download of book with id {bookId}')
    print(f'Page count: {count}')
    return count
