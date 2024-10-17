import fitz

def replace_text_in_pdf(input_pdf, output_pdf):
    doc = fitz.open(input_pdf)

    for page_num in range(len(doc)):
        page = doc[page_num]

        print(page.get_fonts())
        
        text_instances = page.search_for('REPLACE_NAME')
        for inst in text_instances:
            page.add_redact_annot(inst, text=input('Enter your name: '), fill=(1, 1, 1))
            page.apply_redactions()

        text_instances = page.search_for('REPLACE_AGE')
        for inst in text_instances:
            page.add_redact_annot(inst, text=input('Enter your age: '), fill=(1,1,1))
            page.apply_redactions()

        
    
    doc.save(output_pdf)
    doc.close()


input_pdf = "replace.pdf"
output_pdf = "modified.pdf"

replace_text_in_pdf(input_pdf, output_pdf)