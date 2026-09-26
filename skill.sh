#!/usr/bin/env bash
# ==============================================================================
# Animathor Skill Installer & Manager (skill.sh)
# Compatible with Linux, macOS, and Windows (Git Bash / WSL / MSYS2)
# ==============================================================================

set -e

ANIMATHOR_VERSION="1.0.0"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

print_banner() {
    echo -e "${CYAN}=================================================================${NC}"
    echo -e "${CYAN}    ANIMATHOR STUDIO - AGENT SKILL INSTALLER (skill.sh)         ${NC}"
    echo -e "${CYAN}    Version: ${ANIMATHOR_VERSION} | Mathematical & Technical Cinema    ${NC}"
    echo -e "${CYAN}=================================================================${NC}"
}

print_help() {
    print_banner
    echo -e "Usage: ${GREEN}bash skill.sh [command] [options]${NC}\n"
    echo -e "Commands:"
    echo -e "  ${YELLOW}install${NC}       Install Animathor skill into a project or globally (default)"
    echo -e "  ${YELLOW}check${NC}         Run system health check (Python, Manim, ffmpeg, LaTeX)"
    echo -e "  ${YELLOW}lint${NC}          Audit a storyboard or script for Anti-Slop & Accuracy"
    echo -e "  ${YELLOW}help${NC}          Display this help message\n"
    echo -e "Options for install:"
    echo -e "  ${BLUE}--project <path>${NC}    Target project directory (default: current directory .)"
    echo -e "  ${BLUE}--global${NC}            Install to user's global agent configuration (~/.agents, ~/.claude)"
    echo -e "  ${BLUE}--target <type>${NC}     Target folder: 'agents', 'claude', or 'all' (default: all)"
    echo -e "\nExamples:"
    echo -e "  ${GREEN}bash skill.sh install${NC}                     # Install into current project"
    echo -e "  ${GREEN}bash skill.sh install --project /path/to/app${NC} # Install into specific project"
    echo -e "  ${GREEN}bash skill.sh install --global${NC}              # Install globally for all projects"
    echo -e "  ${GREEN}bash skill.sh check${NC}                         # Check system toolchain"
}

resolve_source_skill() {
    # Detect where the skill source lives
    if [ -d "$SCRIPT_DIR/skills/animathor" ]; then
        SOURCE_SKILL="$SCRIPT_DIR/skills/animathor"
    elif [ -d "$SCRIPT_DIR/.agents/skills/animathor" ]; then
        SOURCE_SKILL="$SCRIPT_DIR/.agents/skills/animathor"
    else
        echo -e "${RED}[!] Error: Could not locate source 'animathor' skill directory.${NC}"
        exit 1
    fi
}

install_skill() {
    local target_dir="."
    local is_global=false
    local target_type="all"

    while [[ "$#" -gt 0 ]]; do
        case $1 in
            --project) target_dir="$2"; shift ;;
            --global) is_global=true ;;
            --target) target_type="$2"; shift ;;
            *) ;;
        esac
        shift
    done

    resolve_source_skill
    print_banner

    if [ "$is_global" = true ]; then
        echo -e "${BLUE}[*] Target: GLOBAL Agent Installation${NC}"
        
        # 1. ~/.agents/skills/animathor
        mkdir -p "$HOME/.agents/skills"
        cp -r "$SOURCE_SKILL" "$HOME/.agents/skills/animathor"
        echo -e "  ${GREEN}[+] Installed:${NC} $HOME/.agents/skills/animathor"

        # 2. ~/.claude/skills/animathor
        mkdir -p "$HOME/.claude/skills"
        cp -r "$SOURCE_SKILL" "$HOME/.claude/skills/animathor"
        echo -e "  ${GREEN}[+] Installed:${NC} $HOME/.claude/skills/animathor"

        # 3. ~/.gemini/antigravity/skills/animathor (if exists)
        if [ -d "$HOME/.gemini" ]; then
            mkdir -p "$HOME/.gemini/antigravity/skills"
            cp -r "$SOURCE_SKILL" "$HOME/.gemini/antigravity/skills/animathor"
            echo -e "  ${GREEN}[+] Installed:${NC} $HOME/.gemini/antigravity/skills/animathor"
        fi

        echo -e "\n${GREEN}[✓] Animathor installed globally! Any agent session will now recognize @animathor.${NC}"
        return 0
    fi

    # Project-level installation
    echo -e "${BLUE}[*] Target Project: ${target_dir}${NC}"
    mkdir -p "$target_dir"

    if [ "$target_type" = "agents" ] || [ "$target_type" = "all" ]; then
        mkdir -p "$target_dir/.agents/skills"
        cp -r "$SOURCE_SKILL" "$target_dir/.agents/skills/animathor"
        echo -e "  ${GREEN}[+] Installed:${NC} $target_dir/.agents/skills/animathor"
    fi

    if [ "$target_type" = "claude" ] || [ "$target_type" = "all" ]; then
        mkdir -p "$target_dir/.claude/skills"
        cp -r "$SOURCE_SKILL" "$target_dir/.claude/skills/animathor"
        echo -e "  ${GREEN}[+] Installed:${NC} $target_dir/.claude/skills/animathor"
    fi

    # Copy templates directory if not present
    if [ ! -d "$target_dir/templates" ] && [ -d "$SCRIPT_DIR/templates" ]; then
        cp -r "$SCRIPT_DIR/templates" "$target_dir/templates"
        echo -e "  ${GREEN}[+] Created:${NC} $target_dir/templates"
    fi

    echo -e "\n${GREEN}[✓] Animathor skill successfully installed into project!${NC}"
    echo -e "    You can now ask your AI agent:"
    echo -e "    ${YELLOW}\"Plan a 9:16 vertical math short about Fourier Series in 3b1b style\"${NC}"
}

run_health_check() {
    print_banner
    echo -e "${BLUE}[*] Running Animathor Toolchain Health Check...${NC}\n"
    if command -v python3 &>/dev/null; then
        python3 "$SCRIPT_DIR/scripts/check_health.py"
    elif command -v python &>/dev/null; then
        python "$SCRIPT_DIR/scripts/check_health.py"
    else
        echo -e "${RED}[!] Error: Python is not installed or not in PATH.${NC}"
        exit 1
    fi
}

run_linter() {
    local target_file="$1"
    if [ -z "$target_file" ]; then
        echo -e "${RED}[!] Error: Please specify a file to lint. Example: bash skill.sh lint storyboard.md${NC}"
        exit 1
    fi
    if command -v python3 &>/dev/null; then
        python3 "$SCRIPT_DIR/scripts/animathor_cli.py" lint "$target_file"
    else
        python "$SCRIPT_DIR/scripts/animathor_cli.py" lint "$target_file"
    fi
}

# Main routing
CMD="${1:-install}"
shift || true

case "$CMD" in
    install)
        install_skill "$@"
        ;;
    check)
        run_health_check
        ;;
    lint)
        run_linter "$@"
        ;;
    help|--help|-h)
        print_help
        ;;
    *)
        echo -e "${RED}[!] Unknown command: $CMD${NC}"
        print_help
        exit 1
        ;;
esac
