@ECHO OFF
mode con:cols=75 lines=15
cd /d "D:\(000) Git"
dir
cmd /c ""C:\Program Files\Git\bin\bash.exe" auto-sync.sh"
PAUSE