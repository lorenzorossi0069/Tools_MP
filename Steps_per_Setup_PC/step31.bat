echo off

:--------------- step 31
:tbc remov unused apps (Office revove etc)
echo Step 31: uninstall (preinstalled) Office, games, etc..
xcopy  "\\server01\lorenzo.rossi\TOOLS_setup_PC_2020_public\office_removal2020\o15-ctrremove.diagcab" "C:\Users\Test\Desktop\tmpSetup"

pause()
:start 
C:\Users\Test\Desktop\tmpSetup\15-ctrremove.diagcab

pause()