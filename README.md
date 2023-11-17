# PDF Editor Application

This repository is created for [streamlit.io](https://streamlit.io/) deployment. 

The main repository can be reached by [PDF_Editor](https://github.com/tylncck/PDF_Editor). The main repo contains the Docker image setup and it can be seamlessly deployed to any cloud platform. 

The application can be reached at [editpdfs.streamlit.app](https://editpdfs.streamlit.app/). 

## Application Pages

### Home Page
- Welcoming message and navigation instructions.

### PDF Merger Page
- Upload and merge multiple PDF files into one PDF file.

### PDF Compression Page
- Upload and compress a PDF file to reduce its size. Performance depends on the content of the uploaded file. 

### PDF Slicer Page
- Upload and slice a PDF file to only get some pages and use these pages to create a new PDF file.

### PDF Inserter Page
- Upload two PDF files and insert the second file after a specified page of the first file. Files can be used with all pages or you can decide which pages to use. 

### Watermarking Page
- Upload a PDF file and add a watermark with determined text, color, and position. (Currently *Confidential* and *Do Not Copy* version are available.)

## Credits
- The application utilizes the [PyPDF2](https://pypdf2.readthedocs.io/en/3.0.0/) library for PDF manipulation. 

- Ghostscript is used for PDF compression. Visit [Ghostscript](https://www.ghostscript.com/) for more information.

Credits to the PyPDF2 and Ghostscript developers for their contribution to open source habitat. 

## Conclusion
This PDF Editor Application provides a user-friendly interface for common PDF editing tasks. Feel free to explore and enhance your PDFs seamlessly!
I'll try my best to add new features to the application. 

by tylncck