# # # from reportlab.platypus import SimpleDocTemplate, Paragraph
# # # from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
# # # from reportlab.lib.units import inch
# # # from reportlab.lib.pagesizes import letter
# # #
# # # import io
# # #
# # # buf = io.BytesIO()
# # #
# # # # Setup the document with paper size and margins
# # # doc = SimpleDocTemplate(
# # #     buf,
# # #     rightMargin=inch / 2,
# # #     leftMargin=inch / 2,
# # #     topMargin=inch / 2,
# # #     bottomMargin=inch / 2,
# # #     pagesize=(100,50),
# # # )
# # #
# # # Styling paragraphs
# # styles = getSampleStyleSheet()
# #
# # # Write things on the document
# # paragraphs = []
# # paragraphs.append(
# #     Paragraph('This is a paragraph', styles['Normal']))
# # paragraphs.append(
# #     Paragraph('This is another paragraph', styles['Normal']))
# # doc.build(paragraphs)
# #
# # # Write the PDF to a file
# # with open('test.pdf', 'wb') as fd:
# #     fd.write(buf.getvalue())
# from reportlab.pdfgen import canvas
# from reportlab.platypus import Image
# from reportlab.lib.units import inch
# # from PIL import Image
# c = canvas.Canvas("hello.pdf",pagesize=(1500,500))
# logo = "images/1.png"
# logo_width,logo_height = 1043,445
# image = Image(logo,logo_width,logo_height)
# # image = Image.open("images/1.png").save('lalala.png')
# c.drawImage(image,0,0)
# # hello(c)
#
# c.showPage()
# c.save()
#
#
# # from PyPDF2 import PdfFileWriter, PdfFileReader
# # output = PdfFileWriter()
# #
# # input_file = PdfFileReader(open('result.pdf', 'rb'))
# # page = input_file.getPage(0)
# # context = input_file.getObject(page.indirectRef)
# # print("ha")
import time
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import BaseDocTemplate,SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

doc = SimpleDocTemplate("form_letter.pdf", pagesize=(1045,459),
                        rightMargin=0, leftMargin=0,
                        topMargin=0, bottomMargin=0)
Story = []
logo = "images/1.png"
logo_width,logo_height = 522,445
magName = "Pythonista"
issueNum = 12
subPrice = "99.00"
limitedDate = "03/05/2010"
freeGift = "tin foil hat"

formatted_time = time.ctime()
full_name = "Mike Driscoll"
address_parts = ["411 State St.", "Marshalltown, IA 50158"]

im = Image(logo,logo_width,logo_height)
Story.append(im)
Story.append(im)

# styles = getSampleStyleSheet()
# styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
# ptext = '<font size=12>%s</font>' % formatted_time
#
# Story.append(Paragraph(ptext, styles["Normal"]))
# Story.append(Spacer(1, 12))
#
# # Create return address
# ptext = '<font size=12>%s</font>' % full_name
# Story.append(Paragraph(ptext, styles["Normal"]))
# for part in address_parts:
#     ptext = '<font size=12>%s</font>' % part.strip()
#     Story.append(Paragraph(ptext, styles["Normal"]))
#
# Story.append(Spacer(1, 12))
# ptext = '<font size=12>Dear %s:</font>' % full_name.split()[0].strip()
# Story.append(Paragraph(ptext, styles["Normal"]))
# Story.append(Spacer(1, 12))
#
# ptext = '<font size=12>We would like to welcome you to our subscriber base for %s Magazine! \
#         You will receive %s issues at the excellent introductory price of $%s. Please respond by\
#         %s to start receiving your subscription and get the following free gift: %s.</font>' % (magName,
#                                                                                                 issueNum,
#                                                                                                 subPrice,
#                                                                                                 limitedDate,
#                                                                                                 freeGift)
# Story.append(Paragraph(ptext, styles["Justify"]))
# Story.append(Spacer(1, 12))
#
# ptext = '<font size=12>Thank you very much and we look forward to serving you.</font>'
# Story.append(Paragraph(ptext, styles["Justify"]))
# Story.append(Spacer(1, 12))
# ptext = '<font size=12>Sincerely,</font>'
# Story.append(Paragraph(ptext, styles["Normal"]))
# Story.append(Spacer(1, 48))
# ptext = '<font size=12>Ima Sucker</font>'
# Story.append(Paragraph(ptext, styles["Normal"]))
# Story.append(Spacer(1, 12))
doc.build(Story)