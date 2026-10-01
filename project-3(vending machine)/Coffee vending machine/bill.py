
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from datetime import datetime

def generate_bill(cart, total, amount, change):
    file_name = "coffee_bill.pdf"
    pdf = canvas.Canvas(file_name, pagesize=A4)
    width, height = A4

    dark_brown = colors.HexColor("#4B2E20")
    brown = colors.HexColor("#795548")
    light_brown = colors.HexColor("#F5E6D3")
    cream = colors.HexColor("#FFF8F0")
    gold = colors.HexColor("#C89B3C")
    text_brown = colors.HexColor("#5A4030")

    pdf.setFillColor(cream)
    pdf.rect( 0,0,width, height,  fill=1,stroke=0)
    pdf.setFillColor(dark_brown)
    pdf.roundRect(35, height - 125, width - 70, 90, 15, fill=1, stroke=0)
    pdf.setFillColor(colors.white)
    pdf.setFont(  "Helvetica-Bold", 22 )
    pdf.drawCentredString( width / 2, height - 75, "COFFEE VENDING MACHINE" )
    pdf.setFont( "Helvetica",10)
    pdf.drawCentredString(width / 2, height - 95, datetime.now().strftime( "%d-%m-%Y   %H:%M:%S" ))

    #*******bill tittle
    y = height - 165
    pdf.setFillColor(dark_brown)
    pdf.setFont( "Helvetica-Bold", 16 )
    pdf.drawCentredString( width / 2,y, "ORDER BILL" )


    # *******table header
    y -= 35
    pdf.setFillColor(light_brown)
    pdf.roundRect( 45,y - 10, width - 90,30,5,fill=1,stroke=0)
    pdf.setFillColor(dark_brown)
    pdf.setFont("Helvetica-Bold", 11 )
    pdf.drawString(60,y,"Coffee" )
    pdf.drawString( 260, y, "Qty")
    pdf.drawString( 340, y,"Price")
    pdf.drawString( 450, y, "Amount" )

#cofeee items****
    y -= 35
    pdf.setFont( "Helvetica",11  )
    for item in cart:
        item_total = ( item["price"] * item["quantity"] )
        pdf.setFillColor(text_brown)
        pdf.drawString(60, y,item["name"])
        pdf.drawString(260, y,str(item["quantity"]))
        pdf.drawString(340, y,"Rs. " + str(item["price"]))
        pdf.drawString(450,y,"Rs. " + str(item_total) )

    #below line after ech item
        y -= 25
        pdf.setStrokeColor(colors.HexColor("#D8C3AD")  )
        pdf.line( 50, y - 10, width - 50, y - 10)
        y -= 30

#payment****************
    y -= 20
    box_width = 300
    box_height = 115

#center box
    box_x = (  width - box_width ) / 2
    box_y = (  y - box_height + 15 )

#pay bg
    pdf.setFillColor(light_brown)
    pdf.roundRect(box_x, box_y, box_width, box_height,12,fill=1,stroke=0)

#pay title
    pdf.setFillColor(dark_brown)
    pdf.setFont(  "Helvetica-Bold", 13)

    pdf.drawCentredString( width / 2, y - 5,"PAYMENT SUMMARY" )

#total
    pdf.setFont("Helvetica-Bold", 11)
    pdf.drawString( box_x + 45, y - 35, "Total:")
    pdf.drawString( box_x + 160, y - 35, "Rs. " + str(total) )
#paid
    pdf.drawString( box_x + 45, y - 58, "Paid:" )
    pdf.drawString( box_x + 160, y - 58,"Rs. " + str(amount) )

    pdf.drawString( box_x + 45, y - 81, "Change:")
    pdf.drawString(  box_x + 160,y - 81,"Rs. " + str(change) )

    y = box_y - 55
    pdf.setFillColor(gold)
    pdf.roundRect( 150, y, width - 300, 40, 10, fill=1, stroke=0 )

    pdf.setFillColor(colors.white)
    pdf.setFont( "Helvetica-Bold", 13 )
    pdf.drawCentredString( width / 2, y + 14, "PAYMENT SUCCESSFUL")


    y -= 55
    pdf.setFillColor(dark_brown)
    pdf.setFont( "Helvetica-Bold", 15 )
    pdf.drawCentredString( width / 2, y, "Thank You! Enjoy Your Coffee")
    pdf.setFillColor(brown)
    pdf.setFont( "Helvetica", 9)
    pdf.drawCentredString( width / 2, 35, "Fresh Coffee • Happy Moments")

    pdf.save()
    return file_name
