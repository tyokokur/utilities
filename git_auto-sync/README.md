# Git Auto Sync (Windows 10)

## Code (auto-sync.sh)
source: https://jakemccrary.com/blog/2020/02/25/auto-syncing-a-git-repository/
Modified for Windows 10 and recursive file search within parent

## inotify-win.exe
source: https://github.com/thekid/inotify-win
Needed for detection of changes
Manual installation from C: drive
Final .exe moved into C:\Program Files\Git\usr\bin

## Executable (RunAutoSync.bat)
Locate bash.exe and use it to run .bat executable

## Run on startup
Location: Task Scheduler/MyTasks/
Trigger: Run on startup
Action: "D:\(000) Git\RunAutoSync.bat"
