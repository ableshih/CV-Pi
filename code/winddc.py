# https://gist.github.com/ThiefMaster/7063105
# https://msdn.microsoft.com/en-us/library/windows/desktop/dd692979(v=vs.85).aspx
# https://msdn.microsoft.com/en-us/library/windows/desktop/dd692982(v=vs.85).aspx
# http://docs.activestate.com/activepython/2.6/pywin32/win32api__EnumDisplayMonitors_meth.html
# http://nullege.com/codes/search/win32api.EnumDisplayMonitors

from ctypes import windll, byref, Structure, WinError, POINTER, WINFUNCTYPE
from ctypes.wintypes import BOOL, HMONITOR, HDC, RECT, LPARAM, DWORD, BYTE, WCHAR, HANDLE
import sys


_MONITORENUMPROC = WINFUNCTYPE(BOOL, HMONITOR, HDC, POINTER(RECT), LPARAM)


class _PHYSICAL_MONITOR(Structure):
    _fields_ = [('handle', HANDLE),
                ('description', WCHAR * 128)]


def _iter_physical_monitors(close_handles=True):
    """Iterates physical monitors.

    The handles are closed automatically whenever the iterator is advanced.
    This means that the iterator should always be fully exhausted!

    If you want to keep handles e.g. because you need to store all of them and
    use them later, set `close_handles` to False and close them manually."""

    def callback(hmonitor, hdc, lprect, lparam):
        monitors.append(hmonitor)
        return True

    monitors = []
    if not windll.user32.EnumDisplayMonitors(None, None, _MONITORENUMPROC(callback), None):
        raise WinError('EnumDisplayMonitors failed')

    for monitor in monitors:
        # Get physical monitor count
        count = DWORD()
        if not windll.dxva2.GetNumberOfPhysicalMonitorsFromHMONITOR(monitor, byref(count)):
            raise WinError()
        # Get physical monitor handles
        physical_array = (_PHYSICAL_MONITOR * count.value)()
        if not windll.dxva2.GetPhysicalMonitorsFromHMONITOR(monitor, count.value, physical_array):
            raise WinError()
        for physical in physical_array:
            yield physical.handle
            if close_handles:
                if not windll.dxva2.DestroyPhysicalMonitor(physical.handle):
                    raise WinError()


def set_vcp_feature(monitor, code, value):
    """Sends a DDC command to the specified monitor.

    See this link for a list of commands:
    ftp://ftp.cis.nctu.edu.tw/pub/csie/Software/X11/private/VeSaSpEcS/VESA_Document_Center_Monitor_Interface/mccsV3.pdf
    """
    if not windll.dxva2.SetVCPFeature(HANDLE(monitor), BYTE(code), DWORD(value)):
        raise WinError()


turn_on = len(sys.argv) > 1 and sys.argv[1] == 'on'
for handle in _iter_physical_monitors():
    # 0x04 is SOFT-OFF, 0x01 is ON
    set_vcp_feature(handle, 0x10, 0x01 if turn_on else 0x64)
