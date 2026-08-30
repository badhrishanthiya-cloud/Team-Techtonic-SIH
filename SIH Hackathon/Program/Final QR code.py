import qrcode
name=input("Enter your name: ")
contact_info=input("Enter your contact info: ")
hostel_name=input("Enter your hostel name: ")
details={"name":f"{name}","contact_info":f"{contact_info}","hostel_name":f"{hostel_name}"}
qr_name=input("Enter your qr code name: ")
file_path=f"C:\\Users\\trija\\PycharmProjects\\PythonProject\\{qr_name}.png"
qr=qrcode.QRCode()
for k,v in details.items():
    k=k+': '
    v=v+'\n'
    qr.add_data(k)
    qr.add_data(v)
img = qr.make_image()
img.save(file_path)
