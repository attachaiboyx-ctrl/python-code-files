import qrcode

my_link = "https://www.tiktok.com/@pythonbegin.s"  # ใส่ลิงก์ที่ต้องการ
img = qrcode.make(my_link)
img.save("free_qr.png")