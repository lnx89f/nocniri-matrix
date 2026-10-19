#!/usr/bin/env python3
"""Captura ou restaura apenas os arquivos de configuração selecionados."""
import argparse
import datetime
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
HOME = Path.home()
FILES = [
    '.config/niri/config.kdl',
    '.config/alacritty/alacritty.toml',
    '.config/autostart/polkit-gnome-authentication-agent-1.desktop',
    '.local/state/noctalia/settings.toml',
    '.local/state/noctalia/community-palettes/GitHub%20Dark.json',
    'Imagens/Papeis-de-parede/via-lactea-matrix.png',
    'Imagens/wallpapers/colina-windows-xp-noite.png',
]
TOKEN = '@@HOME@@'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=['backup', 'restore'])
    parser.add_argument('--apply', action='store_true', help='Efetiva a restauração; sem isso, apenas lista os arquivos.')
    args = parser.parse_args()
    backup = HOME / '.local/share/nocniri-matrix/backups' / datetime.datetime.now().strftime('%Y%m%d-%H%M%S-%f')
    for relative in FILES:
        live = HOME / relative
        saved = ROOT / 'home' / relative
        source, target = (live, saved) if args.action == 'backup' else (saved, live)
        if not source.is_file():
            raise SystemExit(f'Arquivo ausente: {source}')
        print(f'{source} -> {target}')
        if args.action == 'restore' and not args.apply:
            continue
        if args.action == 'restore' and target.exists():
            previous = backup / relative
            previous.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(target, previous)
        target.parent.mkdir(parents=True, exist_ok=True)
        if source.suffix in ('.toml', '.kdl', '.desktop', '.json'):
            content = source.read_text()
            content = content.replace(str(HOME), TOKEN) if args.action == 'backup' else content.replace(TOKEN, str(HOME))
            target.write_text(content.rstrip() + '\n')
        else:
            shutil.copy2(source, target)
    if args.action == 'restore' and args.apply:
        print(f'Arquivos anteriores preservados em: {backup}')


if __name__ == '__main__':
    main()
