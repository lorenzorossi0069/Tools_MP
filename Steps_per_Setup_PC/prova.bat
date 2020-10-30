echo off
CHOICE /M "Do yo really want to quit"
IF ERRORLEVEL 1 echo pressed Y
IF ERRORLEVEL 2 echo pressed N
pause()