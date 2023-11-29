@echo off
set /p name=Enter the Pokemon name: 

echo Is your Pokemon an Alternate Form?:
echo 1. Yes (Make sure the Pokemon is an alternate form and has a _ after it's name)
echo 2. No

choice /c 12 /n /m "Enter your choice:"

REM Run the Python command
if errorlevel 2 (
    python porymon.py %name%
) else (
    python poryform.py %name%
)

REM Ask the user if they want to add a new mon
set /p addNew=Do you want to add a new Pokémon? (y/n): 

if /i "%addNew%"=="y" (
    REM Reset the script
    call poryall.cmd
)