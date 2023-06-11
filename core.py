def getImageDirName(bookId):
    return f'{bookId}_images'

def getImageFileName(pageNum):
    return f'page_{pageNum}.jpg'

def getDestinationFileName(bookId):
    return f'{bookId}.pdf'
