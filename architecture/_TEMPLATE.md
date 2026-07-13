# SOP: <nome da peça>

> Um arquivo destes por peça do sistema. É o "como funciona" — a fonte da verdade
> da lógica. **Se a lógica mudar, este arquivo muda ANTES do código.** Se o SOP e
> o código discordarem, o SOP está certo e o código é o bug.

## Objetivo

<!-- O que esta peça faz. Uma frase. -->

## Input

<!-- O que ela recebe. Formato + exemplo real. De onde vem. -->

```json
{}
```

## Lógica

<!-- Os passos, em ordem. Determinísticos. Sem "o agente decide" — se algo depende
     de julgamento, isso é um input, não um passo. -->

1.
2.
3.

## Output

<!-- O que ela devolve. Formato + exemplo real. Para onde vai. -->

```json
{}
```

## Edge cases

<!-- O que acontece quando o dado vem torto. Cada linha aqui é um bug que não
     vai existir. -->

| Situação | Comportamento esperado |
|---|---|
| Input vazio | |
| Serviço externo fora do ar | |
| Dado duplicado | |

## Tools envolvidas

- `tools/<script>.py`
