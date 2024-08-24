import fitz

def extract_text_from_pdf(pdf_path,txt_path):
    document = fitz.open(pdf_path)

    ##create or overwrite txt file
    with open(txt_path,'w') as txt_file:
        #iterate over each page
        for page_num in range(len(document)):
            page = document.load_page(page_num)

            ##extract the text in pdf
            text = page.get_text()

            #write the text to txt file

            txt_file.write(text)
            



if __name__ == "__main__":
    pdf_path = "Shikar_Tscripts.pdf"

    txt_path = "result.txt"

    extract_text_from_pdf(pdf_path,txt_path)


    print("extract text from pdf")







