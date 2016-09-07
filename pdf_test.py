# # # # from reportlab.platypus import SimpleDocTemplate, Paragraph
# # # # from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
# # # # from reportlab.lib.units import inch
# # # # from reportlab.lib.pagesizes import letter
# # # #
# # # # import io
# # # #
# # # # buf = io.BytesIO()
# # # #
# # # # # Setup the document with paper size and margins
# # # # doc = SimpleDocTemplate(
# # # #     buf,
# # # #     rightMargin=inch / 2,
# # # #     leftMargin=inch / 2,
# # # #     topMargin=inch / 2,
# # # #     bottomMargin=inch / 2,
# # # #     pagesize=(100,50),
# # # # )
# # # #
# # # # Styling paragraphs
# # # styles = getSampleStyleSheet()
# # #
# # # # Write things on the document
# # # paragraphs = []
# # # paragraphs.append(
# # #     Paragraph('This is a paragraph', styles['Normal']))
# # # paragraphs.append(
# # #     Paragraph('This is another paragraph', styles['Normal']))
# # # doc.build(paragraphs)
# # #
# # # # Write the PDF to a file
# # # with open('test.pdf', 'wb') as fd:
# # #     fd.write(buf.getvalue())
from reportlab.pdfgen import canvas
from reportlab.platypus import Image
from reportlab.lib.units import inch, mm
from PIL import Image as IMG,ImageChops,ImageDraw,ImagePath,ImageFont
import numpy
import matplotlib.pyplot as plt
# c = canvas.Canvas("hello.pdf", pagesize=(1562, 221 * mm))
# logo = "images/1.png"
# logo_width,logo_height = 1043,445
# image = Image(logo,logo_width,logo_height)
# image = Image.open("images/1.png").save('lalala.png')
# c.drawImage(image,0,0)
# hello(c)

from reportlab.platypus import SimpleDocTemplate, Image
doc = SimpleDocTemplate("image.pdf", pagesize=(1562,221*mm))
parts = []
page = IMG.open("images/4.png")
page.convert('CMYK')
parts.append(Image('images/4.png'))
parts.append(Image('images/ab_skin_1.png'))
parts.append(page)
doc.build(parts)


# ############################################
#
#
# c.drawString(226, 110, "Hello")
# hair = Image.open("images/ab_thumb_male_hair_straight.png")
# page = Image.open("images/4.png")
# page.convert('CMYK')
# c.drawImage(page,x=0,y=0)
# c.showPage()
# white_back = Image.open("lalala.png")
# txt = Image.new('RGBA', (700,200), (100,100,100,0))
#
# d = ImageDraw.Draw(txt)
# font = ImageFont.truetype("arial.ttf",size=100)
# d.text((20,100),"Hello WORLD!",fill=(0,0,0,255),font=font)
#
# d.point((28,119),fill=(255,0,0,255))
# d.point((672,119),fill=(255,0,0,255))
# d.point((672,190),fill=(255,0,0,255))
# d.point((28,190),fill=(255,0,0,255))
# # d.text((20,100),"Hello WORLD2!",fill=(0,0,0,255))
# white_back.paste(hair,(700,20),hair)
# txt.save('text_original.jpeg')
# # TEXT TRANSFORMATION
# def find_coeffs(pa, pb):
#     matrix = []
#     for p1, p2 in zip(pa, pb):
#         matrix.append([p1[0], p1[1], 1, 0, 0, 0, -p2[0]*p1[0], -p2[0]*p1[1]])
#         matrix.append([0, 0, 0, p1[0], p1[1], 1, -p2[1]*p1[0], -p2[1]*p1[1]])
#     A = numpy.matrix(matrix, dtype=numpy.float)
#     B = numpy.array(pb).reshape(8)
#     res = numpy.dot(numpy.linalg.inv(A.T * A) * A.T, B)
#     return numpy.array(res).reshape(8)
#
# coeffs = find_coeffs(
#     [(28,119),(672,119),(672,190),(28,190)],
#     [(0,0),(700,0),(700,200),(0,200)],
# )
# # txt = txt.transform((new_width, height), Image.AFFINE,
# #         coeffs, Image.BICUBIC)
# # # img.save(sys.argv[2])
# txt = txt.transform((700, 200), Image.AFFINE,
#         coeffs, Image.NEAREST)
# # img.save(sys.argv[2])
# plt.imshow(txt)
# txt.save('text.png')
# coeffs = find_coeffs(
#     [(0,0),(680,0),(660,100),(0,100)],
#     [(0,0),(680,0),(680,50),(0,100)],
#
# )
# # txt = txt.transform((new_width, height), Image.AFFINE,
# #         coeffs, Image.BICUBIC)
# # # img.save(sys.argv[2])
# txt = txt.transform((700, 200), Image.AFFINE,
#         coeffs, Image.BICUBIC)
# txt.save('text1.png')
# white_back.paste(txt,(100,0),txt)
# white_back.save('LOL.png')
# c.showPage()
# c.drawImage("LOL.png", 0, 0)
# c.showPage()
# # c.drawImage("images/ab_skin_1.png", 700, 300)
# # c.showPage()
# # ##################
# # ##################
# c.save()
#
# # #############################################
# #
# # # from PyPDF2 import PdfFileWriter, PdfFileReader
# # # output = PdfFileWriter()
# # #
# # # input_file = PdfFileReader(open('result.pdf', 'rb'))
# # # page = input_file.getPage(0)
# # # context = input_file.getObject(page.indirectRef)
# # # print("ha")
# # import time
# # from reportlab.lib.enums import TA_JUSTIFY
# # from reportlab.lib.pagesizes import letter
# # from reportlab.platypus import BaseDocTemplate,SimpleDocTemplate, Paragraph, Spacer, Image
# # from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
# # from reportlab.lib.units import inch
# # from reportlab.pdfgen import canvas
# #
# # from reportlab.lib.pagesizes import letter, A4
# # myCanvas = canvas.Canvas('myfile.pdf', pagesize=letter)
# # width, height = letter #keep for later
# #
# # doc = SimpleDocTemplate("form_letter.pdf", pagesize=(1045,459),
# #                         rightMargin=0, leftMargin=0,
# #                         topMargin=0, bottomMargin=0)
# # Story = []
# # logo = "images/1.png"
# # logo_width,logo_height = 522,445
# # magName = "Pythonista"
# # issueNum = 12
# # subPrice = "99.00"
# # limitedDate = "03/05/2010"
# # freeGift = "tin foil hat"
# #
# # formatted_time = time.ctime()
# # full_name = "Mike Driscoll"
# # address_parts = ["411 State St.", "Marshalltown, IA 50158"]
# #
# # im = Image(logo,logo_width,logo_height)
# # Story.append(im)
# # Story.append(im)
# #
# # # styles = getSampleStyleSheet()
# # # styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
# # # ptext = '<font size=12>%s</font>' % formatted_time
# # #
# # # Story.append(Paragraph(ptext, styles["Normal"]))
# # # Story.append(Spacer(1, 12))
# # #
# # # # Create return address
# # # ptext = '<font size=12>%s</font>' % full_name
# # # Story.append(Paragraph(ptext, styles["Normal"]))
# # # for part in address_parts:
# # #     ptext = '<font size=12>%s</font>' % part.strip()
# # #     Story.append(Paragraph(ptext, styles["Normal"]))
# # #
# # # Story.append(Spacer(1, 12))
# # # ptext = '<font size=12>Dear %s:</font>' % full_name.split()[0].strip()
# # # Story.append(Paragraph(ptext, styles["Normal"]))
# # # Story.append(Spacer(1, 12))
# # #
# # # ptext = '<font size=12>We would like to welcome you to our subscriber base for %s Magazine! \
# # #         You will receive %s issues at the excellent introductory price of $%s. Please respond by\
# # #         %s to start receiving your subscription and get the following free gift: %s.</font>' % (magName,
# # #                                                                                                 issueNum,
# # #                                                                                                 subPrice,
# # #                                                                                                 limitedDate,
# # #                                                                                                 freeGift)
# # # Story.append(Paragraph(ptext, styles["Justify"]))
# # # Story.append(Spacer(1, 12))
# # #
# # # ptext = '<font size=12>Thank you very much and we look forward to serving you.</font>'
# # # Story.append(Paragraph(ptext, styles["Justify"]))
# # # Story.append(Spacer(1, 12))
# # # ptext = '<font size=12>Sincerely,</font>'
# # # Story.append(Paragraph(ptext, styles["Normal"]))
# # # Story.append(Spacer(1, 48))
# # # ptext = '<font size=12>Ima Sucker</font>'
# # # Story.append(Paragraph(ptext, styles["Normal"]))
# # # Story.append(Spacer(1, 12))
# # doc.build(Story)
# from pyPdf2 import PdfFileWriter, PdfFileReader
# from reportlab.pdfgen import canvas
# from StringIO import StringIO
#
#
# # Using ReportLab to insert image into PDF
# imgTemp = StringIO()
# imgDoc = canvas.Canvas(imgTemp)
#
# # Draw image on Canvas and save PDF in buffer
# imgPath = "path/to/img.png"
# imgDoc.drawImage(imgPath, 399, 760, 160, 160)    ## at (399,760) with size 160x160
# imgDoc.save()
#
# # Use PyPDF to merge the image-PDF into the template
# page = PdfFileReader(open("document.pdf","rb")).getPage(0)
# overlay = PdfFileReader(StringIO(imgTemp.getvalue())).getPage(0)
# page.mergePage(overlay)
#
# #Save the result
# output = PdfFileWriter()
# output.addPage(page)
# output.write(file("output.pdf","w"))
