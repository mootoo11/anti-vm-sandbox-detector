
                #----------by_mootoo----------#

import os
import sys
import subprocess
import time
import psutil
import uuid
import platform
import socket
import threading
import requests
def check_vm_signatures():
    suspicious_keywords = ["VBOX", "VMWARE", "VIRTUALBOX", "QEMU", "XEN", "HYPER-V", "KVM", "SANDBOX"]
    try:
        output = subprocess.check_output("wmic baseboard get manufacturer,product", shell=True)
        output += subprocess.check_output("wmic computersystem get manufacturer,model", shell=True)
        decoded = output.decode(errors="ignore").upper()
        return any(word in decoded for word in suspicious_keywords)
    except:
        return False

def check_running_processes():
    suspicious_processes = [
        "vmsrvc.exe", "vmtoolsd.exe", "vboxservice.exe", "vboxtray.exe",
        "vmwaretrat.exe", "vmwareuser.exe", "prl_cc.exe", "prl_tools.exe",
        "xenservice.exe", "qemu-ga.exe", "wsnm.exe", "sbiectrl.exe", "pythonservice.exe",
        "wireshark.exe", "procmon.exe", "fiddler.exe", "ollydbg.exe"
    ]
    try:
        tasks = subprocess.check_output("tasklist", shell=True).decode(errors="ignore").lower()
        return any(proc.lower() in tasks for proc in suspicious_processes)
    except:
        return False

def check_sandbox_artifacts():
    paths = [
        "C:\\\\INTERNAL\\\\", "C:\\\\SAMPLE_ANALYSIS", "C:\\\\Windows\\\\SysWOW64\\\\sandbox"
    ]
    return any(os.path.exists(path) for path in paths)

def sleep_skip_check():
    start = time.time()
    time.sleep(5)
    return time.time() - start < 4.5

def check_ram(min_gb=4):
    return psutil.virtual_memory().total / (1024 ** 3) < min_gb

def check_cpu(min_cores=4):
    return psutil.cpu_count(logical=False) < min_cores

def check_disk(min_gb=60):
    return psutil.disk_usage('/').total / (1024 ** 3) < min_gb

def check_mac_address():
    mac = hex(uuid.getnode())[2:].upper()
    vm_mac_prefixes = ["080027", "000569", "005056", "001C42", "00163E", "001C14"]
    return any(mac.startswith(prefix) for prefix in vm_mac_prefixes)

def check_user_and_machine_name():
    suspicious_users = ["sandbox", "test", "analyst", "virus"]
    suspicious_hosts = ["WIN-VM", "DESKTOP-TEST", "MALWARELAB", "SANDBOX"]
    user = os.getenv("USERNAME", "").lower()
    host = platform.node().upper()
    return any(u in user for u in suspicious_users) or any(h in host for h in suspicious_hosts)

def check_uptime(max_minutes=15):
    uptime_seconds = time.time() - psutil.boot_time()
    return uptime_seconds < (max_minutes * 60)

def is_env_suspicious():
    score = 0
    checks = [
        check_vm_signatures,
        check_running_processes,
        check_sandbox_artifacts,
        sleep_skip_check,
        check_ram,
        check_cpu,
        check_disk,
        check_mac_address,
        check_user_and_machine_name,
        check_uptime
    ]
    for check in checks:
        try:
            if check():
                score += 1
        except:
            continue
    return score >= 2 

if __name__ == "__main__":
    if is_env_suspicious():
        sys.exit()
    else:
        print("✅ النظام حقيقي")
