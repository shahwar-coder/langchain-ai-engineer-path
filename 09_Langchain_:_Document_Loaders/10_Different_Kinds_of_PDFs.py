# | Use Case                                         | Recommended Loader                                       | Why                                                                                             |
# | ------------------------------------------------ | -------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
# | Simple, clean PDFs (text-based)                  | **PyPDFLoader**                                          | Fast and simple extraction; good when PDF contains straightforward text without complex layout. |
# | PDFs with tables / multi-column layouts          | **PDFPlumberLoader**                                     | Better at preserving table structures and column layouts.                                       |
# | Scanned / image-based PDFs                       | **UnstructuredPDFLoader** or **AmazonTextractPDFLoader** | Uses OCR to extract text from images; Textract is more accurate but requires AWS.               |
# | Need layout, images, or bounding box info        | **PyMuPDFLoader**                                        | Extracts detailed page structure, images, and layout metadata.                                  |
# | Best overall structure extraction (complex docs) | **UnstructuredPDFLoader**                                | Handles headings, sections, lists, tables, and complex formats better than basic loaders.       |


# https://docs.langchain.com/oss/python/integrations/document_loaders