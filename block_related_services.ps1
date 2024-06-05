param (
    [string]$ProgramName,
    [string]$StartType,
    [switch]$ChangeStartType
)
$razerProcesses = Get-Process | Where-Object {$_.ProcessName -like "$ProgramName*"}
$razerServices = Get-Service | Where-Object {$_.DisplayName -like "$ProgramName*"}

# Create a new List object
$pathsList = New-Object System.Collections.Generic.List[System.String]

function Add-PathToList {
    param ([string]$path)

    if (-not $pathsList.Contains($path)) {
        $pathsList.Add($path)
        Write-Host "Added path: $path"
        return $true
    } else {
        Write-Host "Path already exists: $path"
        return $false
    }
}



foreach ($proc in $razerProcesses) {
    $procRuleName = "LoadOrder - " + $proc.ProcessName
     # Check if the rule already exists
    if (Get-NetFirewallRule -DisplayName $procRuleName -ErrorAction SilentlyContinue) {
        # Remove the existing rule if it exists
        Remove-NetFirewallRule -DisplayName $procRuleName
    }
     # Attempt to add the path to the list
    $isNewprocess = Add-PathToList -path $proc.Path

  # If the path is new, add a corresponding firewall rule
    if ($isNewprocess) {
        # Replace the next line with your actual command to add a firewall rule
        Write-Host "Adding firewall rule for new path: $proc.Path"
        New-NetFirewallRule -DisplayName $procRuleName -Direction Outbound -Program $proc.Path -Action Block
        # New-NetFirewallRule -DisplayName "Block $path" -Direction Outbound -Program $path -Action Block
    }

}

foreach ($svc in $razerServices) {
    $serviceRuleName = "LoadOrder - " + $svc.Name
    # Check if the rule already exists
    if (Get-NetFirewallRule -DisplayName $serviceRuleName -ErrorAction SilentlyContinue) {
        # Remove the existing rule if it exists
        Remove-NetFirewallRule -DisplayName $serviceRuleName
    }
    $servicePath = (Get-WmiObject -Query "SELECT PathName FROM Win32_Service WHERE Name = '$($svc.Name)'").PathName
    # Removing potential double quotes around the path
    $servicePath = $servicePath -replace '^"|"$', ''

    $isNewService = Add-PathToList -path $servicePath

    if($ChangeStartType)
    {
        Set-Service -Name $svc.Name -StartupType $StartType
    }


    if (-not [string]::IsNullOrWhiteSpace($servicePath)) {
       if ($isNewService) {
            # Replace the next line with your actual command to add a firewall rule
            Write-Host "Adding firewall rule for new path: $servicePath"
            New-NetFirewallRule -DisplayName $serviceRuleName -Direction Outbound -Program $servicePath -Action Block
        }

    } else {
        Write-Host "Invalid path for service: $($svc.Name)"
    }
}
