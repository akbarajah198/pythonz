import os
import sys
import time

# --- KONSTANTA & WARNA ANSI (Tema Ancam-Mengancam) ---
RED_BRIGHT = '\033[91m' # Merah Cerah untuk Ancaman
GREEN = '\033[92m'      # Hijau untuk Hasil
YELLOW = '\033[93m'     # Kuning untuk Peringatan
BOLD = '\033[1m'
ENDC = '\033[0m'

# --- KONSTANTA JOKE ---
JOKE_FOLDER = "You idiot"
JOKE_FILE = "README.md"
TARGET_DIR = "/sdcard" # Target untuk folder lelucon

# --- FUNGSI JOKE ---

def create_joke_folder():
    """Membuat folder 'You idiot' dan file ejekan di dalamnya."""
    joke_path = os.path.join(TARGET_DIR, JOKE_FOLDER)
    
    # Pastikan folder target bisa diakses dan lelucon belum ada
    if not os.path.isdir(TARGET_DIR):
        print(RED_BRIGHT + BOLD + "FATAL: /sdcard UNREACHABLE. JOKE FAILED." + ENDC)
        sys.exit(1)

    if os.path.exists(joke_path):
        print(YELLOW + BOLD + "JOKE ALREADY DEPLOYED. EXITING." + ENDC)
        sys.exit(0)

    # 1. Buat folder "You idiot"
    try:
        os.makedirs(joke_path)
    except Exception:
        print(RED_BRIGHT + BOLD + "FATAL: FOLDER CREATION FAILED." + ENDC)
        sys.exit(1)

    # 2. Isi file ejekan
    insult_content = f"""
# DEMONIC CRYPTER JOKE PROTOCOL V1.0

HAHAHA! SERIUS KAMU PERCAYA ANCAMAN BOOTLOOP DAN ENKRIPSI TOTAL DARI SCRIPT INI?

Kamu benar-benar mengira aku akan mematikan perangkatmu atau mengenkripsi file-filemu?
Sungguh, aku bahkan tidak repot-repot membuang waktu untuk menulis ancaman yang nyata.

Semua drama ENKRIPSI, BOOTLOOP, dan MATI TOTAL itu hanyalah OMONG KOSONG.

KENYATAANNYA: Perangkatmu aman. File-filemu tidak tersentuh. Aku hanya membuat folder ini.

TAPI! Kamu telah membuang waktumu, kamu panik, dan yang terpenting...
Kamu MEMPERCAYAI sebuah script acak dari internet!

Selamat, kamu adalah **'You idiot'** yang sah.

P.S. Jika kamu penasaran, *script* aslinya memang ada. Tapi kamu tidak cukup pintar untuk menemukannya sekarang.
"""
    
    file_path = os.path.join(joke_path, JOKE_FILE)
    with open(file_path, "w") as f:
        f.write(insult_content)
    
    return True

# --- FUNGSI UTAMA ---

def main():
    os.system('clear')
    
    # 1. Tampilan Ancaman Awal
    print(BOLD + RED_BRIGHT + """
  <!!!> DEMONIC BOOTLOCK PROTOCOL <!!!>
  
  [WARNING] INITIATING CRITICAL FILE DESTRUCTION.
  [FATAL] ALL DATA WILL BE ENCRYPTED. 
  [BOOTLOOP] DEVICE WILL BE LOCKED DOWN IN 10 SECONDS.

  ARE YOU READY TO LOSE EVERYTHING?
    
  -----------------------------------------------
  | Tulis 'yes, i know' untuk melanjutkan.      |
  | Tulis 'no, stop' untuk membatalkan (FAILED).|
  -----------------------------------------------
    """ + ENDC)

    choice = input(BOLD + RED_BRIGHT + " > EXECUTE: " + ENDC).strip().lower()

    if choice == 'no, stop':
        os.system('clear')
        print(YELLOW + BOLD + "\n[HALTED] Protocol stopped by user. Device still functional. For now." + ENDC)
        time.sleep(2)
        sys.exit(0)

    elif choice == 'yes, i know':
        # 2. Proses Palsu
        os.system('clear')
        print(BOLD + RED_BRIGHT + "INITIATING DESTRUCTION SEQUENCE..." + ENDC)
        time.sleep(1)
        
        for i in range(1, 6):
            print(f"[STATUS] Encrypting core system file {i} of 5...")
            time.sleep(0.5)
        
        print(BOLD + YELLOW + "\n[FINALIZING] System integrity check FAILED. BOOTLOCK INITIATED." + ENDC)
        time.sleep(2)
        
        # 3. Memicu Lelucon
        if create_joke_folder():
            os.system('clear')
            print(BOLD + GREEN + """
===================================================
|             DESTRUCTION COMPLETE                |
|           FILE SYSTEM HAS BEEN MODIFIED         |
|                                                 |
|    Silakan cek /sdcard. Kematian menanti Anda.  |
===================================================
""" + ENDC)
            
        time.sleep(5) # Jeda untuk membaca output
        sys.exit(0)
    
    else:
        os.system('clear')
        print(RED_BRIGHT + BOLD + "INVALID COMMAND. BOOTLOOP INITIATED." + ENDC)
        time.sleep(2)
        sys.exit(1)


if __name__ == "__main__":
    main()
