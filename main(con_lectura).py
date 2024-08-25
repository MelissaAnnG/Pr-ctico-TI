import wave 
import struct 
import tkinter as tk 
from tkinter import filedialog, messagebox 

def validar_archivo_wav(filename):
    try:
        with open(filename, 'rb') as file: 
            header = file.read(12)
            
            # Verificar que los primeros 4 bytes son "RIFF"
            if header[:4].decode('ascii') != 'RIFF':
                return False

            # Verificar que los bytes 8 a 12 son "WAVE"
            if header[8:12].decode('ascii') != 'WAVE':
                return False
            
            return True  # Devuelve True si ambas condiciones se cumplen, de lo contrario, devuelve False
    
    except Exception as e:
        print(f"Error al verificar el archivo: {e}")
        return False

def mostrar_cabecera_wav(filename, text_widget):
    try:
        with open(filename, 'rb') as wav_file:
            # RIFF Header, lee los primeros 44 bytes de la cabecera del archivo WAV
            riff = wav_file.read(44)
            output = []
            output.append(f"Chunk ID (RIFF): {riff[:4].decode('ascii')}\n")
            chunk_size = struct.unpack('<I', riff[4:8])[0]  # Se utiliza struct.unpack para interpretar los bytes en diferentes formatos (por ejemplo, entero, corto).
            output.append(f"Chunk Size: {chunk_size}\n")
            format = riff[8:12].decode('ascii')
            output.append(f"Format: {format} (.wav)\n")

            # fmt Subchunk
            output.append(f"Subchunk1 ID (fmt): {riff[12:16].decode('ascii')}\n")
            subchunk1_size = struct.unpack('<I', riff[16:20])[0]
            output.append(f"Subchunk1 Size: {subchunk1_size}\n")
            audio_format = struct.unpack('<H', riff[20:22])[0]
            output.append(f"Audio Format: {audio_format}\n")
            num_channels = struct.unpack('<H', riff[22:24])[0]
            output.append(f"Num Channels: {num_channels}\n")
            sample_rate = struct.unpack('<I', riff[24:28])[0]
            output.append(f"Sample Rate: {sample_rate} Hz\n")
            byte_rate = struct.unpack('<I', riff[28:32])[0]
            output.append(f"Byte Rate: {byte_rate} bytes/second\n")
            block_align = struct.unpack('<H', riff[32:34])[0]
            output.append(f"Block Align: {block_align} bytes\n")
            bits_per_sample = struct.unpack('<H', riff[34:36])[0]
            output.append(f"Bits per Sample: {bits_per_sample} bits\n")

            # data Subchunk, Se imprimen detalles como el ID del chunk, el tamaño del chunk, la frecuencia de muestreo, el número de canales, etc.
            output.append(f"Subchunk2 ID (data): {riff[36:40].decode('ascii')}\n")
            subchunk2_size = struct.unpack('<I', riff[40:44])[0]
            output.append(f"Subchunk2 Size: {subchunk2_size} bytes\n")

            # Mostrar la salida en el widget de texto
            text_widget.delete(1.0, tk.END)  # Limpiar el cuadro de texto
            text_widget.insert(tk.END, ''.join(output))  # Insertar la nueva información en el cuadro de texto
                        
    except wave.Error as e:
        print(f"Error al procesar el archivo .wav: {e}")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

def abrir_archivo(text_widget):
    filename = filedialog.askopenfilename(
        title="Seleccionar archivo WAV",
        filetypes=(("Archivos WAV", "*.wav"), ("Todos los archivos", "*.*"))
    )

    if filename: 
        if validar_archivo_wav(filename):
            messagebox.showinfo("Validación", f"El archivo {filename} es un archivo .wav válido.")
            mostrar_cabecera_wav(filename, text_widget)
        else:
            messagebox.showerror("Error", f"El archivo {filename} no es un archivo .wav válido.")

def crear_ventana():
    ventana = tk.Tk()
    ventana.title("Validación de archivos WAV")

    # Configurar el tamaño de la ventana
    ventana.geometry("500x400")

    # Botón para abrir el archivo
    btn_abrir = tk.Button(ventana, text="Abrir archivo WAV", command=lambda: abrir_archivo(text_widget))
    btn_abrir.pack(pady=20)

    # Cuadro de texto para mostrar la cabecera
    global text_widget
    text_widget = tk.Text(ventana, wrap=tk.WORD, height=15, width=60)
    text_widget.pack(pady=10)

    # Ejecutar la ventana
    ventana.mainloop()

# Punto de entrada de la aplicación
if __name__ == "__main__":
    crear_ventana()
