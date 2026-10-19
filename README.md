# nocniri-matrix

Backup das configurações pessoais do Niri e Noctalia, com visual Matrix.

## Conteúdo

- Niri: layout, janelas, atalhos, inicialização do Noctalia e teclado `br` / `thinkpad`.
- Overview: **Super + '**. Terminal: **Super + Enter**. Launcher: **Super + Espaço**.
- Noctalia: barra, dock, tela de bloqueio, preferências e paleta personalizada local `Matrix-Verde-Medio`.
- Wallpaper ativo `via-lactea-matrix.png` e alternativa `colina-windows-xp-noite.png`.
- Alacritty e configuração de autostart do agente Polkit.
- `system-reference/`: configuração de console e idioma para consulta; não é aplicada pelo script.

A paleta do Noctalia usa destaque verde `#009926`, alertas verde claro `#99FFB3`, texto comum `#F2F2F2` e texto destacado `#FFFFFF`. Bordas e elementos secundários usam o cinza `#505A60` do Niri, mantendo os fundos escuros. A paleta fica em `~/.config/noctalia/palettes/` e usa a origem `custom`, evitando que atualizações da paleta online sobrescrevam as cores.

Ambiente de origem: openSUSE Tumbleweed, Niri 26.04, Noctalia v5.3.0.
Dependências: Python 3.11+, Niri, Noctalia, Alacritty, Nautilus, xkeyboard-config e os serviços de áudio/rede/Bluetooth usados pelo desktop. Os pacotes não são instalados por este projeto.

## Atualizar o backup

Na raiz do repositório:

```sh
python3 scripts/configs.py backup
git diff
git add .
git commit -m "Atualiza configurações do desktop"
git push
```

O backup inclui somente os arquivos explicitamente listados em `scripts/configs.py`.
Ao adicionar outra configuração ou mudar o wallpaper/paleta, atualize essa lista.
Caminhos da pasta pessoal são salvos como `@@HOME@@` e ajustados na restauração.
Não copie os arquivos com esse marcador diretamente para sua configuração.
Históricos, clipboard, notificações, credenciais, caches e backups antigos não fazem parte da captura.
Revise o diff antes de publicar novas alterações.

## Restaurar

Feche o Noctalia antes de restaurar para evitar que ele sobrescreva as preferências.
Primeiro veja os arquivos que serão copiados:

```sh
python3 scripts/configs.py restore
```

Para aplicar:

```sh
python3 scripts/configs.py restore --apply
niri validate
```

Arquivos existentes são preservados em `~/.local/share/nocniri-matrix/backups/`.
Depois, reinicie o Noctalia. O Niri recarrega sua configuração automaticamente.
As preferências da tela de bloqueio referenciam `eDP-1`; ajuste para seu monitor se necessário.
O teclado gráfico usa a variante ThinkPad, enquanto o console salvo em `system-reference/` usa `KEYMAP=br` e mantém os valores originais do sistema.
