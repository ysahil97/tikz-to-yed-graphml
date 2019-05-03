# Pip3 Installation in Windows
(Tested on Windows 10)

### Prerequisites:
* Python should be installed and callable from command

### Procedure
* Download [get-pip.py](https://bootstrap.pypa.io/get-pip.py)
* Open a command prompt and navigate to the folder containing get-pip.py
* Run `python get-pip.py`
* Pip is now installed corresponding to the version of python
* *Important* To ensure that pip3 is added to path variable, follow these steps
    * Open Control Panel->Systems->Advanced system settings.A pop-up window will appear
    * Click on Environment Variables Button which will list out all the current environment variables.
    * Check whether in `PATH` environment variable, C:\Users\{UserName}\AppData\Local\Programs\Python\Python37-32\Scripts\ is present. If not, add it to `PATH` variable.