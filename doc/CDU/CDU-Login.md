# Login

## Descrição

O usuário acessa um formulario para autenticar no sistema.

## Atores

- Usuário
  - Humano
  - Primário
  - Ativo
- Estabelecimento
  - Humano
  - Secundário
  - Passivo

## Gatilhos

Não se aplica

## Pré-condições

Não se aplica

## Pós-condições

- O usuário está autenticado ao sistema

## Fluxo Principal

_Após o caso [CDU-AcessarSistema]_

1. O usuário tem acesso a um formulario de autenticação
1. O usuário preenche o formulario e envia fazendo a autenticação

_**ponto de extensão:**_
[`CDU - Acesso Dashboard Estabelecimento`]()

_**ponto de extensão:**_
[`CDU - Acessar Sistema`](./CDU-AcessarSistema.md)
## Fluxos Alternativos

Não se aplica

## Situações de Erro

Preencher credenciais erradas

## Regras de Negócio

