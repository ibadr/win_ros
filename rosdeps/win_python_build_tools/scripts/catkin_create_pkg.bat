ECHO OFF

REM Used to help execute because windows is trivially fixated on extensions

set DIR=%~dp0
python %DIR%\catkin_create_pkg.py %*
