# 本程式執行時可以建立 C:\tmp\Python371
# 為了配合 Siemens NX1872 必須使用 Python 3.7.1
import urllib.request
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
# basic files for Python installation
# before 3.12.0
py_list = ["core", "dev", "exe", "lib", "tcltk", "tools"]
# after 3.12.1 no tools.msi
#py_list = ["core", "dev", "exe", "lib", "tcltk"]
# Python version
version = "3.7.1"
# Python msi download URL
ftp = "https://www.python.org/ftp/python/" + version + "/amd64/"
# location for Portable Python
path = "C:\\tmp\\Python371"
# create directory
try:
    os.mkdir(path)
except:
    # path exists
    pass
# get Python installation msi files and extract into target dir
for i in py_list:
    filename = i + ".msi"
    url = ftp + filename
    # download basic python msi file
    urllib.request.urlretrieve(url, filename)
    os.system("msiexec.exe /a " + i + ".msi targetdir=" + path)
    # delete msi file
    os.remove(dir_path + "\\" + i + ".msi")
    os.remove(path + "\\" + i + ".msi")