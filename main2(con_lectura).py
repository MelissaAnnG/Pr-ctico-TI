import struct
import tkinter as tk
from tkinter import filedialog, messagebox

def validar_archivo_bmp(file_bmp):
    try:
        with open(file_bmp, 'rb') as file:
            bmp = file.read(2)
            if bmp[:2].decode('ascii') != 'BM':
                return False
            return True
    except Exception as e:
        messagebox.showerror("Error", f"Error al verificar el archivo: {e}")
        return False

def mostrar_cabecera_bmp(file_bmp, text_widget):
    try:
        with open(file_bmp, 'rb') as file:
            # Mostramos los datos de los primeros 14 bytes
            cabecera = file.read(14)
            output = []
            output.append(f"Signature: {cabecera[:2].decode('ascii')}\n")
            file_size = struct.unpack('<I', cabecera[2:6])[0]
            output.append(f"File Size: {file_size} bytes\n")
            reserved = struct.unpack('<I', cabecera[6:10])[0]
            output.append(f"Reserved: {reserved}\n")
            data_offset = struct.unpack('<I', cabecera[10:14])[0]
            output.append(f"Data Offset: {data_offset}\n")

            # Propiedades de la imagen
            prop_img = file.read(40)
            size = struct.unpack('<I', prop_img[0:4])[0]
            output.append(f"Size: {size} bytes\n")
            width = struct.unpack('<I', prop_img[4:8])[0]
            output.append(f"Width: {width} px\n")
            height = struct.unpack('<I', prop_img[8:12])[0]
            output.append(f"Height: {height} px\n")
            planes = struct.unpack('<H', prop_img[12:14])[0]
            output.append(f"Planes: {planes}\n")
            bit_count = struct.unpack('<H', prop_img[14:16])[0]
            output.append(f"BitCount: {bit_count} px\n")
            compression = struct.unpack('<I', prop_img[16:20])[0]
            output.append(f"Compression: {compression}\n")
            image_size = struct.unpack('<I', prop_img[20:24])[0]
            output.append(f"ImageSize: {image_size}\n")
            XPixelsPerM = struct.unpack('<I', prop_img[24:28])[0]
            output.append(f"Resolución Horizontal: {XPixelsPerM} px/mts\n")
            YPixelsPerM = struct.unpack('<I', prop_img[28:32])[0]
            output.append(f"Resolución Vertical: {YPixelsPerM} px/mts\n")
            colour_used = struct.unpack('<I', prop_img[32:36])[0]
            output.append(f"Colores usados: {colour_used}\n")
            colour_imp = struct.unpack('<I', prop_img[36:40])[0]
            output.append(f"Colores importantes: {colour_imp}\n")

            # Mostrar la salida en el widget de texto
            text_widget.delete(1.0, tk.END)  # Limpiar el cuadro de texto
            text_widget.insert(tk.END, ''.join(output))  # Insertar la nueva información en el cuadro de texto

    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")

def abrir_archivo():
    filename = filedialog.askopenfilename(
        title="Seleccionar archivo BMP",
        filetypes=(("Archivos BMP", "*.bmp"), ("Todos los archivos", "*.*"))
    )

    if filename:
        if validar_archivo_bmp(filename):
            ventana_info = tk.Toplevel()
            ventana_info.title("Información del Archivo BMP")

            # Cuadro de texto para mostrar la cabecera
            text_widget = tk.Text(ventana_info, wrap=tk.WORD, height=15, width=60)
            text_widget.pack(pady=10)

            mostrar_cabecera_bmp(filename, text_widget)
        else:
            messagebox.showerror("Error", f"El archivo {filename} no es un archivo .bmp válido.")

def crear_ventana():
    ventana = tk.Tk()
    ventana.title("Validador de Archivos BMP")

    # Configurar el tamaño de la ventana
    ventana.geometry("400x200")

    # Botón para abrir el archivo
    btn_abrir = tk.Button(ventana, text="Abrir archivo BMP", command=abrir_archivo)
    btn_abrir.pack(pady=20)

    # Ejecutar la ventana
    ventana.mainloop()

if __name__ == '__main__':
    crear_ventana()