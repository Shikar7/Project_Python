import fitz

pdf = fitz.open('Option_Trading_Strategies.pdf')
#print(pdf.page_count)
#print(pdf.metadata)
#print(pdf.metadata['author'])
print(pdf.get_ocgs())


pdf.close()