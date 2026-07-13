# CLAUDE.md — Constituição do projeto

> **Este arquivo é lei.** É o único que o Claude Code carrega automaticamente em
> toda sessão. Regras que precisam valer sempre moram aqui — e só aqui.
>
> Histórico do que foi feito vai em `progress.md`. Pesquisa que ainda não virou
> regra vai em `findings.md`. Não misture: encher este arquivo de narrativa afoga
> as regras que importam.

---

## 1. Norte

<!-- O ÚNICO resultado que este projeto entrega. Uma frase. Se houver dois
     resultados, provavelmente são dois projetos. -->

_(preencher no Blueprint)_

## 2. Schema de dados

**Regra inegociável: nenhum código de produção antes desta seção estar preenchida.**
Use exemplos reais, não descrições.

### Input (dado cru que entra)

```json
{}
```

**De onde vem:** _(fonte da verdade — API, planilha, banco, scraping)_

### Output (payload que sai)

```json
{}
```

**Para onde vai:** _(destino final — Slack, Sheets, banco, e-mail)_

### Invariantes

<!-- O que é SEMPRE verdade sobre esse dado. Campos obrigatórios, unicidade,
     faixas válidas. Ex: "email é único e sempre lowercase" -->

- _(preencher)_

## 3. Regras de comportamento

<!-- O que o sistema NUNCA pode fazer. Tom, limites, restrições de negócio. -->

- Nunca escrever no destino de produção durante testes — use `DRY_RUN=true`.
- _(preencher)_

## 4. Integrações

| Serviço | Para quê | Credencial (`.env`) | Verificada? |
|---|---|---|---|
| _(ex: Slack)_ | _(postar o payload)_ | `SLACK_BOT_TOKEN` | ☐ |

Toda credencial é verificada com um script de handshake em `tools/` **antes** de
qualquer lógica ser construída. Link quebrado = pare, não construa por cima.

## 5. Restrições descobertas

<!-- Alimentado pelo loop de auto-reparo (skill self-anneal). Toda vez que algo
     quebra e você descobre o porquê, o fato vai para cá — para o erro não voltar.
     Registre o FATO, não a narrativa do conserto. -->

- _(ex: "A API X exige header `Accept: application/json`, senão devolve HTML.")_
- _(ex: "Rate limit: 5 req/s. Acima disso, 429 sem `Retry-After`.")_

---

## Arquitetura

Três camadas, com uma razão: **LLM é probabilístico, regra de negócio precisa ser
determinística.** A separação impede que a lógica crítica dependa de um palpite.

```
architecture/   Camada 1 — SOPs em Markdown. O "como funciona" de cada peça.
                Se a lógica muda, o SOP muda ANTES do código.
tools/          Camada 3 — scripts determinísticos, atômicos, testáveis.
.tmp/           Bancada de trabalho. Efêmero, fora do git.
```

A camada 2 (navegação/decisão) é o agente: ele roteia dados entre os SOPs e as
tools, chamando-as na ordem certa. Ele **não** executa a lógica de negócio por
conta própria.

## Definição de pronto

Um projeto está pronto quando o **payload chegou ao destino final** — a planilha
atualizada, a mensagem entregue, a linha no banco. Não quando o script rodou sem
erro.

## Como rodar

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
pip install -r requirements.txt
cp .env.example .env          # preencha as credenciais
python tools/handshake.py     # verifica as conexões ANTES de tudo
```
