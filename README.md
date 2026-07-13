# Automation Starter

Template para projetos de **automação**: scrapers, pipelines de dados, bots,
integrações, agentes disparados por cron ou webhook.

Não é para produtos web com login e assinatura — para isso use o
[saas-supabase-starter](https://github.com/uairoxminas/saas-supabase-starter).

## A ideia

Um LLM é probabilístico. Regra de negócio precisa ser determinística. Este
template separa as duas coisas em camadas, para que a parte crítica nunca dependa
de um palpite:

```
CLAUDE.md       A lei — schemas, regras, invariantes. Lido em toda sessão.
architecture/   SOPs em Markdown. O "como funciona" de cada peça.
tools/          Scripts Python determinísticos. Atômicos e testáveis.
.tmp/           Bancada de trabalho. Efêmero, fora do git.
.env            Credenciais. Fora do git.
```

O agente é a camada de decisão: ele roteia dados entre os SOPs e as tools,
chamando-as na ordem certa. Ele não executa a lógica de negócio por conta própria.

## O método

Cinco fases, em ordem. Pular uma é o que gera retrabalho.

1. **Blueprint** — descobrir o objetivo e **definir o schema dos dados**.
   Nenhum código antes disso.
2. **Link** — verificar que toda credencial funciona (`python tools/handshake.py`).
   Link quebrado? Pare. Não construa por cima.
3. **Architect** — escrever o SOP em `architecture/`, depois a tool em `tools/`.
   Nessa ordem.
4. **Stylize** — formatar o payload para entrega profissional.
5. **Trigger** — subir para a nuvem e configurar o disparo (cron, webhook).

As skills em `.claude/skills/` (`blueprint`, `self-anneal`, `project-memory`)
carregam essas disciplinas automaticamente no Claude Code.

## Começar

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
pip install -r requirements.txt

cp .env.example .env          # preencha as credenciais
python tools/handshake.py     # verifique as conexões ANTES de tudo
```

Depois abra o `CLAUDE.md` e preencha o Norte e o Schema. É daí que tudo sai.

## Definição de pronto

O projeto está pronto quando o **payload chegou ao destino final** — a planilha
atualizada, a mensagem entregue, a linha no banco. Não quando o script rodou sem
erro.
