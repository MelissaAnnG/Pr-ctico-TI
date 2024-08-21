"""
Escribir un programa en lenguaje a elección, que permita:
    1) Ingresar el nombre de un archivo con extensión .bmp
    2) Valide que el archivo sea con el formato adecuado.
    3) Muestre los datos de la cabecera del archivo .bmp

Un archivo gráfico en formato BMP (bitmap) tiene la estructura que se ilustra en la siguiente figura:
                            Cabecera (14 bytes)
                    Propiedades de la imagen (40 bytes)
            Paleta de color (opcional - su tamaño puede variar)
                            Datos de la imagen
"""
import struct 

def validar_archivo_bmp (file_bmp):
    try:
        with open(file_bmp, 'rb') as file:
            bmp = file.read(2)
            if bmp[:2].decode('ascii') != 'BM':
                return False
            return True
    except Exception as e:
        print(f"Error al verificar el archivo {e}")

def mostrar_cabecera_bmp (file_bmp):
    try:
        with open(file_bmp, 'rb') as file:
            #Mostramos los datos de los primeros 14 bytes
            cabecera = file.read(14)
            print(f"Signature: {cabecera[:2].decode('ascii')}")
            file_size = struct.unpack('<I', cabecera[2:6])[0]
            print(f"File Size: {file_size} bytes")
            reserved = struct.unpack('<I', cabecera[6:10])[0]
            print(f"Reserved: {reserved}")
            data_offset = struct.unpack('<I', cabecera[10:14])[0]
            print(f"Data Offset: {data_offset}")

            #Propiedades de la imagen

            prop_img = file.read(40)
            size = struct.unpack('<I', prop_img[0:4])[0]
            print(f"Size: {size} bytes")
            width = struct.unpack('<I', prop_img[4:8])[0]
            print(f"Width: {width} px")
            height = struct.unpack('<I', prop_img[8:12])[0]
            print(f"Height: {height} px")
            planes = struct.unpack('<H', prop_img[12:14])[0]
            print(f"Planes: {planes}")
            bit_count = struct.unpack('<H', prop_img[14:16])[0]
            print(f"BitCount: {bit_count} px")
            compression = struct.unpack('<I', prop_img[16:20])[0]
            print(f"Compression: {compression}")
            image_size = struct.unpack('<I', prop_img[20:24])[0]
            print(f"ImageSize: {image_size}")
            XPixelsPerM = struct.unpack('<I', prop_img[24:28])[0]
            print(f"Resolución Horizontal: {XPixelsPerM} px/mts")
            YPixelsPerM = struct.unpack('<I', prop_img[28:32])[0]
            print(f"Resolución Vertical: {YPixelsPerM} px/mts")
            colour_used = struct.unpack('<I', prop_img[32:36])[0]
            print(f"Colores usados: {colour_used}")
            colour_imp = struct.unpack('<I', prop_img[36:40])[0]
            print(f"Colores importantes: {colour_imp}")
            
    except Exception as e:
        print(f"Ocurrió un error: {e}")

def main2 ():
    file_bmp = r'C:\Users\lucia\OneDrive\Escritorio\PracticoTeoria de la información\file\example.bmp'
    if validar_archivo_bmp(file_bmp):
        print(f"El archivo {file_bmp} es un archivo .bmp valido")
        mostrar_cabecera_bmp(file_bmp)
    else:
        print(f"El archivo {file_bmp} no es un archivo .bmp valido")

if __name__ == '__main__':
    main2()