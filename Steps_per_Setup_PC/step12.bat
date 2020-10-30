echo off

:--------------- step 12
echo step 12: Power profile
:RIF DIR = "C:\Users\Test\Desktop\tmpSetup"
copy "\\server01\services\Win10 settings\Power settings\MicroplanPowerSettings.pow" "C:\Users\Test\Desktop\tmpSetup"

:pbm: serve essere admin 
copy /Y "C:\Users\Test\Desktop\tmpSetup\MicroplanPowerSettings.pow" "C:\"

echo if C:\MicroplanPowerSettings.pow not found, copy by hand
echo DO MANUAL STEPS AND PROCEED...
pause()
powercfg.exe -import C:\MicroplanPowerSettings.pow
del C:\MicroplanPowerSettings.pow
echo manually set Microplan profile (todo: open Energy manager)
pause()

