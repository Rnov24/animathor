<#
.SYNOPSIS
    Animathor Skill Installer & Manager for Windows PowerShell (skill.ps1)
.DESCRIPTION
    Installs the Animathor agent skill into a target project or globally,
    runs health checks, and invokes the anti-slop linter.
#>

[CmdletBinding()]
param (
    [Parameter(Position = 0)]
    [ValidateSet("install", "check", "lint", "help")]
    [string]$Command = "install",

    [Parameter()]
    [string]$Project = ".",

    [Parameter()]
    [switch]$Global,

    [Parameter()]
    [ValidateSet("all", "agents", "claude")]
    [string]$Target = "all",

    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$RemainingArgs
)

$ErrorActionPreference = "Stop"
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path

function Write-Banner {
    Write-Host "=================================================================" -ForegroundColor Cyan
    Write-Host "    ANIMATHOR STUDIO - AGENT SKILL INSTALLER (skill.ps1)        " -ForegroundColor Cyan
    Write-Host "    Version: 1.0.0 | Mathematical & Technical Cinema            " -ForegroundColor Cyan
    Write-Host "=================================================================" -ForegroundColor Cyan
}

function Show-Help {
    Write-Banner
    Write-Host "Usage: .\skill.ps1 [command] [-Project <path>] [-Global] [-Target <all|agents|claude>]" -ForegroundColor Green
    Write-Host "`nCommands:"
    Write-Host "  install   Install Animathor skill into a project or globally (default)" -ForegroundColor Yellow
    Write-Host "  check     Run system health check (Python, Manim, ffmpeg, LaTeX)" -ForegroundColor Yellow
    Write-Host "  lint      Audit a storyboard or script for Anti-Slop & Accuracy" -ForegroundColor Yellow
    Write-Host "  help      Display this help message" -ForegroundColor Yellow
    Write-Host "`nExamples:"
    Write-Host "  .\skill.ps1 install                       # Install into current project" -ForegroundColor Green
    Write-Host "  .\skill.ps1 install -Project D:\MyProject # Install into specific project" -ForegroundColor Green
    Write-Host "  .\skill.ps1 install -Global               # Install globally for all projects" -ForegroundColor Green
    Write-Host "  .\skill.ps1 check                         # Run toolchain health check" -ForegroundColor Green
}

# Resolve source skill folder
$SourceSkill = Join-Path $ScriptDir "skills\animathor"
if (-not (Test-Path $SourceSkill)) {
    $SourceSkill = Join-Path $ScriptDir ".agents\skills\animathor"
}
if (-not (Test-Path $SourceSkill)) {
    Write-Host "[!] Error: Could not locate source 'animathor' skill directory." -ForegroundColor Red
    exit 1
}

switch ($Command) {
    "install" {
        Write-Banner
        if ($Global) {
            Write-Host "[*] Target: GLOBAL Agent Installation" -ForegroundColor Blue
            $HomeDir = [Environment]::GetFolderPath("UserProfile")
            
            # ~/.agents/skills/animathor
            $AgentsGlobal = Join-Path $HomeDir ".agents\skills\animathor"
            New-Item -ItemType Directory -Path (Split-Path $AgentsGlobal) -Force | Out-Null
            Copy-Item -Path $SourceSkill -Destination $AgentsGlobal -Recurse -Force
            Write-Host "  [+] Installed: $AgentsGlobal" -ForegroundColor Green

            # ~/.claude/skills/animathor
            $ClaudeGlobal = Join-Path $HomeDir ".claude\skills\animathor"
            New-Item -ItemType Directory -Path (Split-Path $ClaudeGlobal) -Force | Out-Null
            Copy-Item -Path $SourceSkill -Destination $ClaudeGlobal -Recurse -Force
            Write-Host "  [+] Installed: $ClaudeGlobal" -ForegroundColor Green

            Write-Host "`n[+] Animathor installed globally! Any agent session will now recognize @animathor." -ForegroundColor Green
            break
        }

        # Project-level installation
        $ResolvedProject = Resolve-Path $Project -ErrorAction SilentlyContinue
        if (-not $ResolvedProject) {
            New-Item -ItemType Directory -Path $Project -Force | Out-Null
            $ResolvedProject = Resolve-Path $Project
        }
        Write-Host "[*] Target Project: $ResolvedProject" -ForegroundColor Blue

        if ($Target -eq "agents" -or $Target -eq "all") {
            $AgentsDst = Join-Path $ResolvedProject ".agents\skills\animathor"
            New-Item -ItemType Directory -Path (Split-Path $AgentsDst) -Force | Out-Null
            Copy-Item -Path $SourceSkill -Destination $AgentsDst -Recurse -Force
            Write-Host "  [+] Installed: $AgentsDst" -ForegroundColor Green
        }

        if ($Target -eq "claude" -or $Target -eq "all") {
            $ClaudeDst = Join-Path $ResolvedProject ".claude\skills\animathor"
            New-Item -ItemType Directory -Path (Split-Path $ClaudeDst) -Force | Out-Null
            Copy-Item -Path $SourceSkill -Destination $ClaudeDst -Recurse -Force
            Write-Host "  [+] Installed: $ClaudeDst" -ForegroundColor Green
        }

        $TemplatesSrc = Join-Path $ScriptDir "templates"
        $TemplatesDst = Join-Path $ResolvedProject "templates"
        if (-not (Test-Path $TemplatesDst) -and (Test-Path $TemplatesSrc)) {
            Copy-Item -Path $TemplatesSrc -Destination $TemplatesDst -Recurse -Force
            Write-Host "  [+] Created: $TemplatesDst" -ForegroundColor Green
        }

        Write-Host "`n[+] Animathor skill successfully installed into project!" -ForegroundColor Green
        Write-Host "    You can now ask your AI agent:"
        Write-Host "    `"Plan a 9:16 vertical math short about Fourier Series in 3b1b style`"" -ForegroundColor Yellow
        break
    }

    "check" {
        Write-Banner
        Write-Host "[*] Running Animathor Toolchain Health Check...`n" -ForegroundColor Blue
        $HealthScript = Join-Path $ScriptDir "scripts\check_health.py"
        python $HealthScript
        break
    }

    "lint" {
        if (-not $RemainingArgs -or $RemainingArgs.Count -eq 0) {
            Write-Host "[!] Error: Please specify a file to lint. Example: .\skill.ps1 lint storyboard.md" -ForegroundColor Red
            exit 1
        }
        $CliScript = Join-Path $ScriptDir "scripts\animathor_cli.py"
        python $CliScript lint $RemainingArgs[0]
        break
    }

    "help" {
        Show-Help
        break
    }
}
