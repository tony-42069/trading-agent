# PowerShell script to set up documentation structure
$projectPath = "D:\AI Projects\trading-agent"

# Create necessary directories
New-Item -ItemType Directory -Force -Path "$projectPath\docs"
New-Item -ItemType Directory -Force -Path "$projectPath\docs\archive"
New-Item -ItemType Directory -Force -Path "$projectPath\src"

# Function to create a file if it doesn't exist
function Create-FileIfNotExists {
    param (
        [string]$path,
        [string]$content
    )
    if (-not (Test-Path $path)) {
        Set-Content -Path $path -Value $content -Encoding UTF8
        Write-Host "Created $path"
    } else {
        Write-Host "$path already exists"
    }
}