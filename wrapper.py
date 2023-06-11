from fpdf import FPDF

from core import getImageDirName
from core import getImageFileName
from core import getDestinationFileName

def makePDF(bookId, pageCount):
    print(f'Starting PDF conversion of book with id {bookId}')
    pdf = FPDF()
    imageDir = getImageDirName(bookId)
    for pageNum in range(1, pageCount + 1):
        pdf.add_page()
        pdf.image(f'{imageDir}/{getImageFileName(pageNum)}', 0, 0, 210, 297)
        print(f' - Processed page {pageNum}')
    dest = getDestinationFileName(bookId)
    print(f'Saving to {dest}')
    pdf.output(dest, "F")
    print(f'Completed PDF conversion of book with id {bookId}')
    print(f'Destination: {dest}')
