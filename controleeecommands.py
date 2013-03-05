import os, time

class ControlEeeCommands():
    """Webcam commands"""
    def webcam_on(self):
        os.system('modprobe uvcvideo')
        os.system('echo 1 > /proc/acpi/asus/camera')
        
    def webcam_off(self):
        os.system('rmmod uvcvideo')
        os.system('echo 0 > /proc/acpi/asus/camera')
        
    def webcam_status(self):
        val = os.popen('cat /proc/acpi/asus/camera').read()
        if val=="1\n":
                return 1
        elif val=="0\n":
                return 0
        else:
                return -1

    """Bluetooth Commands"""
    def bluetooth_on(self):
        os.system('echo 1 > /proc/acpi/asus/bt')
        
    def bluetooth_off(self):
        os.system('echo 0 > /proc/acpi/asus/bt')
        
    def bluetooth_status(self):
        val = os.popen('cat /proc/acpi/asus/bt').read()
        if val=="1\n":
                return 1
        elif val=="0\n":
                return 0
        else:
                return -1
    
    """Wifi Commands"""
    def wifi_on(self):
        # Force PCI Express Hotplug to reinit
        os.system('modprobe -r -q pciehp')
        time.sleep(1)
        # pciehp_force may be unnecessary; Xandros did it.
        os.system('modprobe pciehp pciehp_force=1')
        time.sleep(1)
        # Switch on the hardware
        os.system('echo 1 > /proc/acpi/asus/wlan')
        time.sleep(1)
        # load_modules
        os.system('modprobe ath_pci')
        time.sleep(1)
        os.system('/etc/init.d/networking restart')
        
    def wifi_off(self):
        os.system('modprobe -r -q ath_pci')
        os.system('modprobe -r -q ath_rate_sample')
        os.system('modprobe -r -q ath_hal')
        os.system('modprobe -r -q wlan_ccmp')
        os.system('modprobe -r -q wlan_tkip')
        os.system('modprobe -r -q wlan_wep')
        os.system('modprobe -r -q wlan_acl')
        os.system('modprobe -r -q wlan_scan_sta')
        os.system('modprobe -r -q wlan')
        os.system('echo 0 > /proc/acpi/asus/wlan')
        
    def wifi_status(self):
        val = os.popen('cat /proc/acpi/asus/wlan').read()
        if val=="1\n":
                return 1
        elif val=="0\n":
                return 0
        else:
                return -1
