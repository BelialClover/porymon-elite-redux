@echo off
echo Welcome to PoryMon UI!
echo What would you like to do?
echo 1. Add a new Pokemon
echo 2. Download Pokemon Assets
echo 3. Add a new Ability
echo 4. Add a new Move

set /p choice=Enter your choice (default is 1): 
if "%choice%"=="" set choice=1

if "%choice%"=="1" (
    call porymon.cmd
) else if "%choice%"=="2" (
    clear
    py assets_downloader.py
    pause
    call poryall.cmd
) else (
    echo Coming soon! (TM)
    call poryall.cmd
)