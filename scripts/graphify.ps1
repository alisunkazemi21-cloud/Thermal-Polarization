# Project-local Graphify; no activation or global PATH change needed.
$graphifyRoot = Split-Path -Parent $PSScriptRoot
$graphifyExe = Join-Path $graphifyRoot '.venv\Scripts\graphify.exe'
if (-not (Test-Path -LiteralPath $graphifyExe)) {
    throw 'Graphify is missing. Install environment/requirements-graphify.txt into .venv first.'
}
Push-Location $graphifyRoot
try {
    & $graphifyExe @args
    $graphifyExitCode = $LASTEXITCODE
} finally {
    Pop-Location
}
exit $graphifyExitCode
