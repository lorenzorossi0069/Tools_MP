echo off

:login as lorenzo.rossi
net use \\server01 /USER:microplan\lorenzo.rossi Microplan999++
echo logged to \\server01



:RIF DIR = "C:\Users\Test\Desktop\tmpSetup"
mkdir "C:\Users\Test\Desktop\tmpSetup"

:--------------- step 1
:--------------- step 2
:--------------- step 3
:--------------- step 4
:--------------- step 5
:--------------- step 6
echo step 6: set autologin with cmd control userpasswords2
netplwiz
pause()
echo

:--------------- step 7
echo step 7: computer: C0XX and workgroup: MICROPLAN 
systempropertiescomputername
pause()
echo

=========REBOOT====
:--------------- step 8
:--------------- step 9
:--------------- step 10
echo step 10: set No screensaver
:tbd
pause()

:--------------- step 11
echo step 11: set wallpaper Microplan
.\wallpapers\Nero-16-9.png
:tbc
:pbm: come impostare cmd as admin in local prompt?
pause()

:--------------- step 12
echo step 12: Power profile
:RIF DIR = "C:\Users\Test\Desktop\tmpSetup"
copy "\\server01\services\Win10 settings\Power settings\MicroplanPowerSettings.pow" 
"C:\Users\Test\Desktop\tmpSetup\MicroplanPowerSettings.pow"
:pbm: serve essere admin 


"C:\Users\Test\Desktop\MicroplanPowerSettings.pow"

copy /Y "C:\Users\microplan\Desktop\MicroplanPowerSettings.pow" "C:\"
echo if C:\MicroplanPowerSettings.pow not found, copy by hand
echo DO MANUAL STEPS AND PROCEED...
pause()
powercfg.exe -import C:\MicroplanPowerSettings.pow
del C:\MicroplanPowerSettings.pow
echo manually set Microplan profile (todo: open Energy manager)
pause()

:--------------- step 13
echo step 13: Set "System shutdown" on the action of power button pressing
:tbd
echo do manually and press enter
pause()

:--------------- step 14
echo step 14: Folders Options, make visible extensions for files, hidden files 
:tbd
echo do manually and press enter
pause()

:--------------- step 15
echo step 15: auto hide task bar
:tbd
echo do manually and press enter
pause()

:--------------- step 16
echo step 16: Install Acrobat reader (https://get.adobe.com/reader/)
start /MIN /B  microsoft-edge:https://get.adobe.com/reader/

:--------------- step 17
echo step 17: start/home page a blank page (about:blank)
:tbd
echo do manually and press enter
pause()

:--------------- step 18
:--------------- step 19
:--------------- step 20
echo step 20: select 2nd eth for wago (or other ethernet devices)
ncpa.cpl

:--------------- step 21
:--------------- step 22
:--------------- step 23
echo step 23: install Teamviewer
\\server01\Services\Teamviewer\TeamViewer_Host_Setup.exe
pause()

:=============================

:--------------- step 24
:--------------- step 25
echo step25: install PARSEQ
:mkdir "C:\Users\Test\Desktop\tmpSetup\Volume"

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

echo run Custom Installer(4.3)
pause()
:qui cd serve perchè  ho blanks...
cd "C:\Users\Test\Desktop\tmpSetup\Custom Installer(4.3)"
setup.exe"

echo end of Custom Installer(4.3)
pause()

::following if for LABSOFT
::skipped
:echo step24: install LV2018sp1
:xcopy  "\\server01\Services\National Instruments\LabSoft 2.0 - Drivers\W10\LabVIEW RunTime & Device Driver Installer 2018sp1\Volume" "C:\Users\Test\Desktop\tmpSetup\LABSOFTsetup" /E
:C:\Users\Test\Desktop\tmpSetup\LABSOFTsetup\setup.exe
:pause()
:echo verify NI is OK (before deleting)

:--------------- step 26
:--------------- step 27
:tbd shell:startup

:--------------- step 28
:tbd extra language packs
:--------------- step 29
:--------------- step 30
:--------------- step 31
:tbc remov unused apps (Office revove etc)
echo Step 31: uninstall (preinstalled) Office, games, etc..
xcopy  "\\server01\lorenzo.rossi\TOOLS_setup_PC_2020_public\office_removal2020\o15-ctrremove.diagcab" "C:\Users\Test\Desktop\tmpSetup"
start o15-ctrremove.diagcab.exe

:--------------- step 32
:tbd check updates

:--------------- step 33
echo Step 33: setup OpenofficePortable....
:xcopy  "\\server01\Services\Utility&Tools\OpenOffice\Win10\OpenOfficePortable" "C:\Users\Test\Desktop\tmpSetup\OpenOfficePortable" /E/Y
move /-Y "C:\Users\Test\Desktop\tmpSetup\OpenOfficePortable" "C:\"

:--------------- step 34 RAM >8GB
:--------------- step 35
:tbd disable autoaupdate


::=============================

echo continue to delete setup folder (clean up)
:rmdir "C:\Users\Test\Desktop\tmpSetup" /S/Q
echo fine
pause()

