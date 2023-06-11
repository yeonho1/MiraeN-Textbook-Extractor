from crawler import getPageUrls
from crawler import downloadImages
from wrapper import makePDF

# BOOK_ID = 'kb2079'
BOOK_ID = 'kb2099'

pageUrls = getPageUrls(BOOK_ID)
pageCount = downloadImages(BOOK_ID, pageUrls)
pageCount = 440
makePDF(BOOK_ID, pageCount)
