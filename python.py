#qr scanner project simple with python 
import pyqrcode 
import png

#taking input from user
s=input("enter your site here for qr")

#creating qr
link=pyqrcode.create(s)

#creating and svg file
link.svg("qrcode.svg",scale=8)

#and another png file 
link.png("qrcode.png",scale=6)

