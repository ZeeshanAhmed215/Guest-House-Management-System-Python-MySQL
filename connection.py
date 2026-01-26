
database_data=["host name","user name","password","database name"]
      
def qrcode(data_encrypt):

    import qrcode
    qr = qrcode.QRCode(
        version=1,
        box_size=5,
        border=5
    )
    qr.add_data(data_encrypt)
    qr.make(fit=True)

    
    img = qr.make_image(fill="black", back_color="white")
    img.save("images/qrcode.png")



