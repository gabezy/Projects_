import qrcode


data = 'https://www.youtube.com/'
path = 'C:/Users/Gabriel/Desktop/myqrcode.png'

img = qrcode.make(data)

img.save(path)



