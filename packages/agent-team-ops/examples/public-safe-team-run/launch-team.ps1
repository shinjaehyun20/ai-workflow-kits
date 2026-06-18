#requires -version 5.1
<#
.SYNOPSIS
    Stand up a 4-pane Claude Code team in a Windows Terminal 2x2 grid.

.DESCRIPTION
    The Windows-native counterpart to launch-team.sh. Opens one Windows Terminal
    window split into a 2x2 grid and starts an interactive `claude` session in
    each pane, pre-briefed with its role from
    packages/agent-team-ops/claude/agents/ via --append-system-prompt.

    No tmux required. The repo root is resolved from this script's location, so
    you can run it from anywhere (no need to cd into the repo first).

.EXAMPLE
    pwsh -File packages\agent-team-ops\examples\public-safe-team-run\launch-team.ps1

.NOTES
    Requirements: Windows Terminal (wt.exe) and the claude CLI on PATH.
    Close the team by closing the Windows Terminal window.
#>

[CmdletBinding()]
param()

$ErrorActionPreference = 'Stop'

# Repo root = four levels up from examples/public-safe-team-run/.
$Root   = (Resolve-Path (Join-Path $PSScriptRoot '..\..\..\..')).Path
$Agents = Join-Path $Root 'packages\agent-team-ops\claude\agents'

# Pane title -> role agent file. Edit this list to change the team shape.
$Roles = [ordered]@{
    'team-lead' = Join-Path $Agents 'team-lead.agent.md'
    'builder'   = Join-Path $Agents 'builder.agent.md'
    'builder-2' = Join-Path $Agents 'builder.agent.md'
    'reviewer'  = Join-Path $Agents 'reviewer.agent.md'
}

if (-not (Get-Command wt.exe -ErrorAction SilentlyContinue)) {
    Write-Error 'Windows Terminal (wt.exe) not found. Install it from the Microsoft Store, or use launch-team.sh under WSL2. See docs/ko/tooling-setup.md.'
    return
}
if (-not (Get-Command claude -ErrorAction SilentlyContinue)) {
    Write-Error 'claude CLI not found on PATH.'
    return
}

# Build the per-pane command: cd to repo root, then launch claude with the role
# file injected as an appended system prompt. Each pane reads its own file so we
# never have to inline file contents on the command line.
function Get-PaneCommand([string]$file) {
    if (Test-Path $file) {
        return "Set-Location -LiteralPath '$Root'; claude --append-system-prompt (Get-Content -Raw -LiteralPath '$file')"
    }
    return "Set-Location -LiteralPath '$Root'; Write-Host 'Missing role file: $file'; claude"
}

$names = @($Roles.Keys)

# Assemble one wt invocation that builds a 2x2 grid:
#   pane0 (new tab) | pane1 (split right)
#   pane2 (split below 0) | pane3 (split below 1)
$wtArgs = @(
    'new-tab', '--title', $names[0], 'pwsh', '-NoExit', '-Command', (Get-PaneCommand $Roles[$names[0]]),
    ';', 'split-pane', '--vertical',   '--title', $names[1], 'pwsh', '-NoExit', '-Command', (Get-PaneCommand $Roles[$names[1]]),
    ';', 'move-focus', 'left',
    ';', 'split-pane', '--horizontal', '--title', $names[2], 'pwsh', '-NoExit', '-Command', (Get-PaneCommand $Roles[$names[2]]),
    ';', 'move-focus', 'right',
    ';', 'split-pane', '--horizontal', '--title', $names[3], 'pwsh', '-NoExit', '-Command', (Get-PaneCommand $Roles[$names[3]])
)

Write-Host ("Launching team '{0}' with {1} panes: {2}" -f 'team', $names.Count, ($names -join ', '))
& wt.exe @wtArgs
