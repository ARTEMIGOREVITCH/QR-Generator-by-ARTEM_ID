import qrcode



def get_qrcode(url='https://www.instagram.com/amazingame.ru/', name ='default'):
    qr = qrcode.make(data=url)
    qr.save(stream=f'{name}.png')

    return f'QR code was created! Open the png {name}.png' 




def main(): 
    print(get_qrcode(url='https://www.instagram.com/amazingame.ru/', name='instagram'))
    print(get_qrcode(url='https://amazingame.ru/', name='amazingame')) 


if __name__ == '__main__':
   main() 