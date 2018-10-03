
# coding: utf-8

# In[ ]:


import img2pdf
import os
from PyPDF2 import PdfFileWriter, PdfFileReader


from PyPDF2 import PdfFileMerger

pdfs = ['wo1/pdf/1160388_1.pdf', 'wo1/pdf/1160388_2.pdf']
imgs = ['wo1/1160388_1.jpg', 'wo1/1160388_2.jpg']

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("result.pdf")
with open("result2.pdf","wb") as f:
	f.write(img2pdf.convert(imgs))

# # Creating a routine that appends files to the output file
# def append_pdf(input,output):
#     [output.addPage(input.getPage(page_num)) for page_num in range(input.numPages)]

# # Creating an object where pdf pages are appended to
# output = PdfFileWriter()

# # Appending two pdf-pages from two different files
# for x in range(1,number_of_page):
# 	append_pdf(PdfFileReader(open(foldername+"/pdf/"+img_group+"_"+str(x)+".pdf","rb")),output)

# # Writing all the collected pages to a file
# output.write(open(foldername+"/"+foldername+".pdf","wb"))

# print("Done merge : "+foldername+" pdfs")
# print("PDF location : "+foldername+"/")

