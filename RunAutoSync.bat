@ECHO OFF
mode con: cols = 160 lines = 78
cd /d "D:\(000) Git"
dir
cmd /c ""C:\Program Files\Git\bin\bash.exe" utilities\auto_sync.sh"
PAUSE