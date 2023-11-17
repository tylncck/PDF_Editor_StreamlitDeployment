from PyPDF2 import PdfReader, PdfWriter
from io import BytesIO
import os
from pathlib import Path
from typing import Union, Literal, List


def save_file(file_uploader):
    target_directory = 'files'
    os.makedirs(target_directory, exist_ok=True)
    target_path = os.path.join(target_directory, file_uploader.name)
    with open(target_path, "wb") as file:
        file.write(file_uploader.read())
    return target_path

def delete_pdf_files():
    target_directory = 'files'
    if os.path.exists(target_directory) and os.path.isdir(target_directory):
        files = os.listdir(target_directory)
        pdf_files = [file for file in files if file.lower().endswith(".pdf")]
        
        for pdf_file in pdf_files:
            pdf_path = os.path.join(target_directory, pdf_file)
            os.remove(pdf_path)

def pdf_merger(pdf_file_list):
    merger = PdfWriter()

    for pdf in pdf_file_list:
        merger.append(pdf)
    
    merged_pdf_stream = BytesIO()
    merger.write(merged_pdf_stream)
    merged_pdf_stream.seek(0)
    
    return merged_pdf_stream


def pdf_compress(input_file):
    reader = PdfReader(input_file)
    writer = PdfWriter()

    for page in reader.pages:
        page.compress_content_streams()
        writer.add_page(page)

    compressed_pdf_stream = BytesIO()
    writer.write(compressed_pdf_stream)
    compressed_pdf_stream.seek(0)
    return compressed_pdf_stream

def get_pdf_page_count(pdf_file_path):
    with open(pdf_file_path, 'rb') as file:
        pdf_reader = PdfReader(file)
        return len(pdf_reader.pages)

def pdf_inserter(pdf1, pagerange1, pdf2, pagerange2, position):
    merger = PdfWriter()

    file1 = open(pdf1, "rb")
    file2 = open(pdf2, "rb")

    # add pages from the first PDF file to output file as a whole
    merger.append(fileobj=file1, pages = pagerange1)

    # insert the pages  of input2 into the output beginning after the second page
    merger.merge(position=position, fileobj=file2, pages=pagerange2)

    inserted_pdf_stream = BytesIO()
    merger.write(inserted_pdf_stream)
    inserted_pdf_stream.seek(0)
    return inserted_pdf_stream

def pdf_split(pdf, pagerange):
    merger = PdfWriter()

    file1 = open(pdf, "rb")

    # add selected pages from the PDF file to output file as a whole
    merger.append(fileobj=file1, pages = pagerange)

    split_pdf_stream = BytesIO()
    merger.write(split_pdf_stream)
    split_pdf_stream.seek(0)
    return split_pdf_stream



def stamp(content_pdf, stamp_pdf):
    
    reader = PdfReader(stamp_pdf)
    image_page = reader.pages[0]

    writer = PdfWriter()
    reader = PdfReader(content_pdf)
    
    page_indices = list(range(0, len(reader.pages)))
    
    for index in page_indices:
        content_page = reader.pages[index]
        mediabox = content_page.mediabox
        content_page.merge_page(image_page)
        content_page.mediabox = mediabox
        writer.add_page(content_page)

    watermark_stream = BytesIO()
    writer.write(watermark_stream)
    watermark_stream.seek(0)
    return watermark_stream

def watermark(content_pdf, stamp_pdf):
    reader = PdfReader(content_pdf)
    
    page_indices = list(range(0, len(reader.pages)))

    writer = PdfWriter()
    for index in page_indices:
        content_page = reader.pages[index]
        mediabox = content_page.mediabox

        reader_stamp = PdfReader(stamp_pdf)
        image_page = reader_stamp.pages[0]

        image_page.merge_page(content_page)
        image_page.mediabox = mediabox
        writer.add_page(image_page)

    watermark_stream = BytesIO()
    writer.write(watermark_stream)
    watermark_stream.seek(0)
    return watermark_stream