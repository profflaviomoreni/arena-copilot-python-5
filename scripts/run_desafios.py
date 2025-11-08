#!/usr/bin/env python3
"""Pequeno utilitário para testar as funções em src/desafios.py individualmente.

Uso:
  python scripts/run_desafios.py palindromo "À sogra má e amargosa"
  python scripts/run_desafios.py intersecao "1,2,2,3" "2,2,4"
  python scripts/run_desafios.py soma "1:5,3:7,10:11"
"""
import argparse
import os
import sys

# Garantir que o diretório raiz do repositório esteja no sys.path para permitir
# importações como `from src.desafios import ...` quando o script for executado
# diretamente (ex: `python scripts/run_desafios.py ...`).
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from src.desafios import eh_palindromo, intersecao_unica, soma_intervalos
from typing import List, Tuple


def parse_list(s: str) -> List[int]:
    if not s:
        return []
    return [int(x) for x in s.split(',') if x.strip()]


def parse_intervals(s: str) -> List[Tuple[int, int]]:
    if not s:
        return []
    out = []
    for part in s.split(','):
        part = part.strip()
        if not part:
            continue
        if ':' not in part:
            raise ValueError(f"Intervalo inválido: {part}. Use inicio:fim")
        a, b = part.split(':', 1)
        out.append((int(a), int(b)))
    return out


def main() -> None:
    parser = argparse.ArgumentParser(description="Demo das funções em src/desafios.py")
    sub = parser.add_subparsers(dest='cmd', required=True)

    p1 = sub.add_parser('palindromo', help='Verifica se o texto é palíndromo')
    p1.add_argument('texto', nargs='+', help='Texto a avaliar (coloque entre aspas se houver espaços)')

    p2 = sub.add_parser('intersecao', help='Mostra intersecao única e ordenada entre duas listas')
    p2.add_argument('l1', help='Lista 1, elementos separados por vírgula (ex: 1,2,3)')
    p2.add_argument('l2', help='Lista 2, elementos separados por vírgula (ex: 2,3,4)')

    p3 = sub.add_parser('soma', help='Soma comprimentos dos intervalos unidos')
    p3.add_argument('intervalos', help='Intervalos no formato inicio:fim separados por vírgula (ex: 1:5,3:7)')

    args = parser.parse_args()

    if args.cmd == 'palindromo':
        texto = ' '.join(args.texto)
        print(eh_palindromo(texto))
    elif args.cmd == 'intersecao':
        l1 = parse_list(args.l1)
        l2 = parse_list(args.l2)
        print(intersecao_unica(l1, l2))
    elif args.cmd == 'soma':
        iv = parse_intervals(args.intervalos)
        print(soma_intervalos(iv))


if __name__ == '__main__':
    main()
