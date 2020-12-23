# Acessar Serviço

## Descrição

O usuário insere um texto numa caixa dedicada para busca, é retornado os resultados da pesquisa e o usuário acessa um serviço

## Atores

- visitante
  - Humano
  - Primário
  - Ativo
- cliente
  - Humano
  - Primário
  - Ativo

## Pré-condições

Não se aplica

## Pós-condições

- A página de detalhes do serviço é mostrada na tela

## Fluxo Principal

_Após o caso [CDU-BuscarEstabelecimentoServico]_

1. O usuário acessa a página de um serviço

__**Ponto de extensão:**_
[`CDU - Agendar horario`](./CDU-AgendarHorario.md)

## Fluxos Alternativos

Não se aplica

## Situações de Erro

### Texto Vazio Enviado

Consequência: O caso de uso é reiniciado.
