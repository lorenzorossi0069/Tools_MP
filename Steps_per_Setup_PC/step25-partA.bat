echo off

:--------------- step 25 part A
echo step25: install PARSEQ
mkdir "C:\Users\Test\Desktop\tmpSetup\Volume"

echo copy N1: copying Parseq Installer(4.3)
xcopy  "\\server01\Software\ParSeq\W10\Parseq Installer(4.3)\Volume" "C:\Users\Test\Desktop\tmpSetup\Volume" /E

echo copy N2: copying Custom Installer(4.3)
xcopy  "\\server01\Software\ParSeq\W10\Custom Installer(4.3)" "C:\Users\Test\Desktop\tmpSetup\Custom Installer(4.3)" /E


echo run N1: Parseq Installer(4.3)
pause()
:qui cd non serve perchè non ho blanks...
C:\Users\Test\Desktop\tmpSetup\Volume\setup.exe

echo end of part 1: Parseq Installer(4.3), now reboot is required
============REBOOT 2 =======
pause()
