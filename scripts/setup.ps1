
Set-Location $path/downloads
Invoke-WebRequest https://www.python.org/ftp/python/3.12.5/python-3.12.5-amd64.exe
python-3.9.0.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
Set-Location $path/desktop/Item-Calculator
