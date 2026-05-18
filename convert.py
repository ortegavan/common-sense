from docling.document_converter import DocumentConverter

source = "file.pdf"
converter = DocumentConverter()
doc = converter.convert(source).document

with open("file.md", "w", encoding="utf-8") as f:
    f.write(doc.export_to_markdown())