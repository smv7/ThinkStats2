'''2022/03/18 by PianisT
This Python script reaches the codebook of the
specified column in the pdf codebook.'''


#import re  # The pdf reader don't shows the header or numeration at footer.

import PyPDF2 as pypdf


def main():
    path = './Cycle6Codebook-Pregnancy.pdf'
    pdf_file = pypdf.PdfFileReader(path)
    col_name = input('Column name: ').lower()
    #regex = f'.*{col_name}.+[0-9] of [0-9].*'

    for i in range(pdf_file.numPages):
        current_page = pdf_file.getPage(i)
        text = current_page.extractText().lower()
        if col_name in text:#re.search(regex, text) is not None:
            print(f'Page founded!\nYour result is in page {i+1}\n')
            return i+1
    return None


if __name__ == '__main__':
    main()
