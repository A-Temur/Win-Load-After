Get-Process | Where-Object {$_.ProcessName -like "Razer*"} | Stop-Process -Force
Get-Process | Where-Object {$_.ProcessName -like "CefSharp*"} | Stop-Process -Force
Get-Process | Where-Object {$_.ProcessName -like "EABackgroundService*"} | Stop-Process -Force
Get-Process | Where-Object {$_.ProcessName -like "GameManagerService*"} | Stop-Process -Force