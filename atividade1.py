import threading
import time
import random

def download_file(file_number):
    download_time = random.randint(1, 5)
    print(f"Iniciando o download do arquivo {file_number}... (tempo estimado: {download_time} segundos)")
    time.sleep(download_time)
    print(f"Arquivo {file_number} baixado com sucesso!")

def main():
    threads = []
    num_files = 5  # Número de arquivos para "baixar"

    for i in range(num_files):
        thread = threading.Thread(target=download_file, args=(i+1,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("Todos os downloads foram concluídos!")

if __name__ == "__main__":
    main()
