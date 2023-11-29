set /p name=Enter the Pokemon name (default is potato): 
if "%name%"=="" set "name=potato"

echo Is your Pokemon an Alternate Form?:
echo 1. No
echo 2. Yes (Make sure the Pokemon is an alternate form and has a _ after its name)

set /p choice=Enter your choice (default is 1): 
if "%choice%"=="" set choice=1

if "%choice%"=="2" (
    echo Adding Alternate Form
    py poryform.py %name%
) else (
    echo Adding New Species
    py porymon.py %name%
)

pause

REM Ask the user if they want to add a new mon
set /p addNew=Do you want to add a new Pokemon? (y/n): 

if /i "%addNew%"=="y" (
    REM Reset the script
    clear
    call porymon.cmd
)