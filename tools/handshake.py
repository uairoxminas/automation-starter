"""
Handshake — verifica que toda credencial e todo serviço externo respondem.

Rode ISTO antes de construir qualquer lógica. Um "link" quebrado descoberto no
início custa minutos; descoberto depois de três dias de código construído em
cima, custa os três dias.

Uso:
    python tools/handshake.py

Adicione um check por integração. Cada check devolve (ok, detalhe).
"""

from __future__ import annotations

import os
import sys
from typing import Callable

from dotenv import load_dotenv

load_dotenv()

Check = Callable[[], tuple[bool, str]]


def check_env(*names: str) -> tuple[bool, str]:
    """Confere apenas que as variáveis existem e não estão vazias."""
    faltando = [n for n in names if not os.getenv(n)]
    if faltando:
        return False, f"faltando no .env: {', '.join(faltando)}"
    return True, "presentes"


# ─────────────────────────────────────────────────────────────
# Registre um check por integração.
#
# Um check de verdade CHAMA o serviço — não basta a chave existir, ela precisa
# ser aceita. Chave presente mas revogada é o modo de falha que mais engana.
#
# Exemplo:
#
# def check_slack() -> tuple[bool, str]:
#     import requests
#     token = os.getenv("SLACK_BOT_TOKEN")
#     if not token:
#         return False, "SLACK_BOT_TOKEN ausente"
#     r = requests.post(
#         "https://slack.com/api/auth.test",
#         headers={"Authorization": f"Bearer {token}"},
#         timeout=10,
#     )
#     data = r.json()
#     if not data.get("ok"):
#         return False, f"token rejeitado: {data.get('error')}"
#     return True, f"autenticado como {data.get('user')}"
# ─────────────────────────────────────────────────────────────

CHECKS: dict[str, Check] = {
    # "Slack": check_slack,
}


def main() -> int:
    if not CHECKS:
        print("Nenhum check registrado ainda.")
        print("Defina as integrações no CLAUDE.md e adicione um check por serviço aqui.")
        return 0

    falhou = False
    for nome, check in CHECKS.items():
        try:
            ok, detalhe = check()
        except Exception as e:  # noqa: BLE001 — queremos ver qualquer falha aqui
            ok, detalhe = False, f"{type(e).__name__}: {e}"

        print(f"[{'OK ' if ok else 'FALHA'}] {nome}: {detalhe}")
        if not ok:
            falhou = True

    if falhou:
        print("\nLink quebrado. NÃO construa lógica por cima — corrija primeiro.")
        return 1

    print("\nTodas as conexões respondendo.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
