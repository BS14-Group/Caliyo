"""
 RAM auslesen unter Windows ohne Drittmodule wie psutil zu nutzen
 Quelle:
 https://stackoverflow.com/questions/38247958/incorrect-virtual-memory-report-using-ctypes-in-windows
 mit kleinen Änderungen
"""
import platform
import ctypes

class MEMORYSTATUS(ctypes.Structure):
    """  RAM auslesen mit ctypes """
    _fields_ = [
        ("dwLength", ctypes.c_ulong),
        ("dwMemoryLoad", ctypes.c_ulong),
        ("dwTotalPhys", ctypes.c_ulonglong),
        ("dwAvailPhys", ctypes.c_ulonglong),
        ("dwTotalPageFile", ctypes.c_ulonglong),
        ("dwAvailPageFile", ctypes.c_ulonglong),
        ("dwTotalVirtual", ctypes.c_ulonglong),
        ("dwAvailVirtual", ctypes.c_ulonglong),
        ("dwAvailExtendedVirtual", ctypes.c_ulonglong),
    ]

def get_memory():
    """ RAM auslesen """
    stat = MEMORYSTATUS(dwLength=ctypes.sizeof(MEMORYSTATUS)) #create the structure
    ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(stat))
    virtual_memory_dict = {
        'dwTotalPhys': stat.dwTotalPhys,
        'dwAvailPhys': stat.dwAvailPhys,
        'dwMemoryLoad': stat.dwMemoryLoad   # genutzter Speicher in Prozent
    }
    return virtual_memory_dict

if __name__ == '__main__':
    # This area is used for testing only
    if platform.system() == "Windows":
        memory = get_memory()
        print(memory)
