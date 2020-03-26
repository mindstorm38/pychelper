@echo off
set /p version="Version: "
python -m twine upload dist/pychelper-%version%*