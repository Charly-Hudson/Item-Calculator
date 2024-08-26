# Item-Calculator
An item calculator for Factory Based Games (Coming Soon) 
For any issues with any of the items not calculating please let me know Via Discord 

Discord Username: d1sc0rdcharly



To get this setup ensure you have Git installed (If you are on MacOS things are a little more complicated see Solution 2)

Git Install:

Install git and run the file and go through a simple setup.

```
https://gitforwindows.org/
```
Open VScode press Windows/CMD+' (Opening a terminal) Then paste the following script commands into A PowerShell Terminal

Solution 1: 
Windows; (With Python installed)

```
$path = Get-Location
cd desktop
git clone https://github.com/Charly-Hudson/Item-Calculator.git --branch V1.1.1
cd Item-Calculator
python ItemCalculator.py
```

Solution 1.2: 
Windows; (No Python installed)

```
$path = Get-Location
cd desktop
git clone https://github.com/Charly-Hudson/Item-Calculator.git --branch V1.1.1
cd Item-Calculator
.\scripts\setup.py
python ItemCalculator.py
```

Solution 2.1:
Mac; (No Homebrew)

Open your Mac terminal and run the following

```
https://brew.sh/
brew install powershell --cask
```

Solution 2.2;
Mac; (No Python)

Open a Powershell Terminal in VS code and Run the Following

```
cd desktop
git clone https://github.com/Charly-Hudson/Item-Calculator.git --branch V1.1.1
cd Item-Calculator
.\scripts\setup.py
python ItemCalculator.py
```

Solution 2.3
Mac; (Just get the Item Calc)

Open a Powershell Terminal in VS code and Run the Following

```
cd desktop
git clone https://github.com/Charly-Hudson/Item-Calculator.git --branch V1.1.1
cd Item-Calculator
python ItemCalculator.py
```
