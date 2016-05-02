@ECHO OFF

set PWD=%~dp0
set COMMAND=%1
if X%COMMAND%==X set COMMAND=all
if X%COMMAND%==Xhelp goto Help
if X%COMMAND%==Xclean goto Clean
if X%COMMAND%==Xall goto Download
if X%COMMAND%==Xdownload goto Download
if X%COMMAND%==Xinstall goto Download
if X%COMMAND%==Xuninstall goto Uninstall
goto Help

:Help
echo.
echo "Invalid usage: call with args from ['clean', 'all', 'download', 'install', 'uninstall']"
echo "Make sure you bump the version in setup.py if necessary."
goto End

:Download
for  %%P in (python.exe) do SET PYTHON_PATH=%%~dp$PATH:P
IF NOT EXIST %PYTHON_PATH%\scripts\winros_wstool.py (
  echo.
  echo "Downloading using pip, then patching"
  echo.
  rem vcstools rosinstall wstool rospkg catkin_pkg empy
  pip install vcstools rosinstall wstool rospkg catkin_pkg empy
  copy %PYTHON_PATH%\scripts\wstool %PYTHON_PATH%\scripts\winros_wstool.py
  copy %PYTHON_PATH%\scripts\rosversion %PYTHON_PATH%\scripts\winros_rosversion.py
  copy %PYTHON_PATH%\scripts\catkin_create_pkg %PYTHON_PATH%\scripts\winros_catkin_create_pkg.py
  copy %PYTHON_PATH%\scripts\catkin_find_pkg %PYTHON_PATH%\scripts\catkin_find_pkg.py
) else (
  echo.
  echo "Already prepped"
)
if X%COMMAND%==Xall goto install
if X%COMMAND%==Xinstall goto install
goto End

:Install
python setup_by_pip.py install --record install.record
goto End

:Uninstall
echo "Uninstalling files."
for /f %%a in ('cat install.record') do rm -f %%a
goto End

:Clean
rm -f %cd%\install.record
goto End

:End
cd %PWD%
