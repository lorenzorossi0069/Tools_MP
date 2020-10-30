echo off

:--------------- step 33
echo Step 33: setup OpenofficePortable....
xcopy  "\\server01\Services\Utility&Tools\OpenOffice\Win10\OpenOfficePortable" "C:\Users\Test\Desktop\tmpSetup\OpenOfficePortable" /E/Y/I

echo ora copia su C.........
pause()
move /Y "C:\Users\Test\Desktop\tmpSetup\OpenOfficePortable" "C:\"

pause()

