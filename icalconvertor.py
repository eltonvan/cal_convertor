import PyPDF2
from icalendar import Calendar, Event

def pdf_to_ics(pdf_file, ics_file):
    pdf = PyPDF2.PdfFileReader(pdf_file)
    num_pages = pdf.getNumPages()

    cal = Calendar()

    for page_num in range(num_pages):
        print(page_num)
        page = pdf.getPage(page_num)
        content = page.extract_text()

        # Assuming the table has two columns separated by a tab character
        rows = content.strip().split('\n')

        for row in rows:
            data = row.split('\t')

            # Assuming the table has at least two columns: date and description
            if len(data) >= 2:
                date = data[0].strip()
                description = data[1].strip()

                event = Event()
                event.add('summary', description)
                event.add('dtstart', date)
                event.add('dtend', date)
                cal.add_component(event)

    with open(ics_file, 'wb') as f:
        f.write(cal.to_ical())


pdf_file_path = 'kinder.pdf'
ics_file_path = 'kinder.ics'
pdf_to_ics(pdf_file_path, ics_file_path)
