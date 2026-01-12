import tabula
import pandas
import os
import pdf2docx
import docxtpl

# Read pdf into a list of DataFrame
'''def fromPDFToExcel(pdfName: str):
    pdfName = str(input("inserisci il file pdf: "))
    try:
        tabula.io.convert_into(pdfName, pdfName.replace(".pdf", ".csv"), output_format="csv")
    except Exception as error:
        print(str(error))

    df = pandas.read_csv(pdfName.replace(".pdf", ".csv"))
    try:
        df.to_excel(pdfName.replace(".pdf", ".xlsx"))
        print("Bene, il file pdf è stato convertito in un file xlsx")
    except Exception as error:
        print(str(error))
    else:
        print("Bo")

    os.system(f"ls -la /home/ale/Downloads | grep {pdfName.replace("/home/ale/Downloads", "")}")
'''
def fromPDFToWord(pdfName: str):
    Convert = pdf2docx.Converter(pdf_file=pdfName)
    Convert.convert(docx_filename=pdfName.replace(".pdf", ".docx"))

    os.system(f"ls -la /home/ale/Downloads | grep  {pdfName.replace("/home/ale/Downloads/", "")}")
#os.system("rm -rf /home/ale/.cache/.fr-L3ZH42/Jobs/cat.csv"

#fromPDFToWord("/home/ale/Downloads/MorelloAlessandroCV.pdf")
fromPDFToWord("/home/ale/Downloads/MorelloAlessandroCV-1.pdf")