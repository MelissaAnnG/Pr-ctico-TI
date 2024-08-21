import wave
import struct

def validar_archivo_wav(filename):
    try:
        with open(filename, 'rb') as file:
            # Leer los primeros 12 bytes
            header = file.read(12)
            
            # Verificar que los primeros 4 bytes son "RIFF"
            if header[:4].decode('ascii') != 'RIFF':
                return False

            # Verificar que los bytes 8 a 12 son "WAVE"
            if header[8:12].decode('ascii') != 'WAVE':
                return False
            
            return True
    
    except Exception as e:
        print(f"Error al verificar el archivo: {e}")
        return False

def mostrar_cabecera_wav(filename):
    try:
        with open(filename, 'rb') as wav_file:
            # RIFF Header
            riff = wav_file.read(44)
            print(f"Chunk ID (RIFF): {riff[:4].decode('ascii')}")
            chunk_size = struct.unpack('<I', riff[4:8])[0]
            print(f"Chunk Size: {chunk_size}")
            format = riff[8:12].decode('ascii')
            print(f"Format: {format} (.wav)")

            # fmt Subchunk
            fmt_subchunk = riff
            print(f"Subchunk1 ID (fmt): {fmt_subchunk[12:16].decode('ascii')}")
            subchunk1_size = struct.unpack('<I', fmt_subchunk[16:20])[0]
            print(f"Subchunk1 Size: {subchunk1_size}")
            audio_format = struct.unpack('<H', fmt_subchunk[20:22])[0]
            print(f"Audio Format: {audio_format}")
            num_channels = struct.unpack('<H', fmt_subchunk[22:24])[0]
            print(f"Num Channels: {num_channels}")
            sample_rate = struct.unpack('<I', fmt_subchunk[24:28])[0]
            print(f"Sample Rate: {sample_rate} Hz")
            byte_rate = struct.unpack('<I', fmt_subchunk[28:32])[0]
            print(f"Byte Rate: {byte_rate} bytes/second")
            block_align = struct.unpack('<H', fmt_subchunk[32:34])[0]
            print(f"Block Align: {block_align} bytes")
            bits_per_sample = struct.unpack('<H', fmt_subchunk[34:36])[0]
            print(f"Bits per Sample: {bits_per_sample} bits")

            # data Subchunk
            data_subchunk = riff
            print(f"Subchunk2 ID (data): {data_subchunk[36:40].decode('ascii')}")
            subchunk2_size = struct.unpack('<I', data_subchunk[40:44])[0]
            print(f"Subchunk2 Size: {subchunk2_size} bytes")
            #print(f"Data (first 10 bytes): {data_subchunk[8:18]}")
            
            
    except wave.Error as e:
        print(f"Error al procesar el archivo .wav: {e}")
    except Exception as e:
        print(f"Ocurrió un error: {e}")


def main():
    # Ingresar el nombre del archivo .wav
    filename = r"C:\Users\lucia\OneDrive\Escritorio\PracticoTeoria de la información\file\395244__hoshi_hana__happy.wav"
    
    # Validar el archivo
    if validar_archivo_wav(filename):
        print(f"El archivo {filename} es un archivo .wav válido.")
        # Mostrar los datos de la cabecera
        mostrar_cabecera_wav(filename)
    else:
        print(f"El archivo {filename} no es un archivo .wav válido.")

if __name__ == "__main__":
    main()
