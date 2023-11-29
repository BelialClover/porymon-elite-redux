@echo off
echo Welcome to PoryMon UI!
echo What would you like to do?
echo 1. Add a new Pokemon
echo 2. Add a new Ability
echo 3. Add a new Move

set /p choice=Enter your choice (default is 1): 
if "%choice%"=="" set choice=1

if "%choice%"=="1" (
    call porymon.cmd
) else if "%choice%"=="2" (
    echo Coming soon! (TM)
    call poryall.cmd
) else if "%choice%"=="3" (
    echo Coming soon! (TM)
    call poryall.cmd
) else (
    call porymon.cmd
)