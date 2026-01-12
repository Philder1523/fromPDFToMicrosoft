from tabula.io import convert_into
from pandas import read_csv
import os
from pdf2docx import Converter
from psycopg2 import (
    connect, 
    DatabaseError
    )
from config import load_config

# Read pdf into a list of DataFrame
def fromPDFToExcel(pdfName: str):
    while True:
        pdfName = str(input("inserisci il file pdf: "))
        if pdfName != None and ".pdf" in pdfName:
            break

    try:
        convert_into(pdfName, pdfName.replace(".pdf", ".csv"), output_format="csv")
    except Exception as error:
            try:
                with connect(**config) as conn:
                    conn.autocommit = True
                    cursor = conn.cursor()
                    sql = '''INSERT INTO error_logs (id, timestamp, exception) VALUES ("%s"); ''', str(error)
                    cursor.execute(sql)
                    conn.commit()
                    conn.close()
            except (DatabaseError, Exception) as dbError:
                return dbError
            return str(error)

    df = read_csv(pdfName.replace(".pdf", ".csv"))
    try:
        df.to_excel(pdfName.replace(".pdf", ".xlsx"))
        print("Bene, il file pdf è stato convertito in un file xlsx")
    except Exception as error:
        return str(error)

    os.system("ls -la /link/to/pdf/ | grep %s", pdfName.replace("/link/to/pdf/", ""))

def fromPDFToWord(pdfName: str):
    Convert = Converter(pdf_file=pdfName)
    Convert.convert(docx_filename=pdfName.replace(".pdf", ".docx"))

    os.system(f"ls -la | grep  {pdfName.replace("/link/to/pdf/", "")}")

fromPDFToWord("")



if __name__ == "__main__":
    config = load_config()
    connect(config)
    