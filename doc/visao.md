# Documento de visão

## 1 - Resumo

O Buscabelo é uma solução web que visa promover uma maior integração entre estabelecimentos de beleza e o cliente interessado em seus serviços.

## 2 - Clientes

Os estabelecimentos de beleza serão os clientes da Buscabelo, uma vez que o acesso a algumas funcionalidades para eles só serão disponibilizadas mediante pagamento.

## 3 - Problema

### 3.1 Consumidor

#### 3.1.1 Dificuldade em encontrar serviços de beleza especializados

Devido a grande quantidade de estabelecimentos de beleza, diferentes serviços e a busca por como cuidar melhor de sua aparência e de como tratar de forma saudável seus cabelos e barbas; os públicos, tanto feminino quanto masculino, têm tido certas dificuldades para encontrar um serviço de beleza ideal, de qualidade e confiável.

### 3.1.2 Dificuldade em comparar preços de serviços de beleza em uma região

Como em alguns bairros há uma grande quantidade de estabelecimentos de beleza e na cidade em geral há vários estabelecimentos de beleza que oferecem o mesmo serviço, o consumidor pode ficar em dúvida de onde ir e de qual é melhor. A ideia de comparar os preços de serviços é dar a opção ao consumidor de escolher um lugar em que ele se sinta confortável em pagar o preço que ele acha justo pelo serviço e qualidade do estabelecimento de beleza.

### 3.1.3 Dificuldade em agendar serviços e perda de tempo.

Alguns estabelecimentos de beleza possuem formas de agendamento de serviços de beleza, porém eles são lentos ou possuem dificuldade de usabilidade e trás uma experiência de usuário negativa. Outros estabelecimentos de beleza não fazem agendamentos e trabalham por ordem de chegada dos seus clientes e fazem-os desperdiçar tempo para ser atendido.

## 4 - Escopo

### 4.1. O Buscabelo é

- Uma plataforma web para busca e agendamento de serviços de beleza.

### 4.2. O Buscabelo não é

- Uma plataforma para comprar perucas.
- Uma plataforma de compra.
- Uma plataforma de blog.

### 4.3. O Buscabelo faz

- Realiza a busca de serviços de beleza.
- Possibilita a filtragem da busca de serviços de beleza por região.
- Realiza o agendamento de serviços em estabelecimentos de beleza.
- Permite a avaliação de estabelecimentos de beleza ao qual o consumidor agendou o serviço.
- Permite ao consumidor o acesso ao histórico de serviços de beleza contratados.
- Permite ao estabelecimento de beleza o acesso ao histórico de clientes que contrataram seus serviços.

### 4.4. O Buscabelo não faz

- Realizar pagamentos pela plataforma.
- Acompanhar a rota até o estabelecimento de beleza contratado pelo cliente na plataforma.
- Permitir avaliação pública.

## 5 - Usuários

### 5.1 Consumidor
- Utilizam a plataforma para encontrar estabelecimentos de beleza com serviços de beleza.
- Utilizam a plataforma para marcar horário em estabelecimento(s) de beleza.

#### 5.2 Estabelecimento de beleza
- Utilizam a plataforma para anunciar seus serviços de beleza.
- Utilizam a plataforma para exibir no perfil um quadro de horários para agendamento.


## 6 - Requisitos

### 6.2.1 Requisitos Funcionais

| Cód. | Nome | Descrição | Categoria |
| -------- | -------- | -------- | -------- |
| RF01 | Catalogar serviços e produtos | Possibilitar a catalogação dos serviços e produtos ofertados pelo estabelecimentos de beleza | |
| RF02 | Agendar serviços de beleza | Possibilita que usuário consiga marcar um horário em comum com o estabelecimento para que o usuário tenha acesso ao serviço| |
| RF03 | Avaliar estabelecimentos de beleza | Permitir que os usuários possam avaliar os serviços de beleza que utilizarem | | 


### 6.2.2 Requisitos não funcionais

| Cód. | Nome | Descrição | Categoria |
| -------- | -------- | -------- | -------- |
| NF01 | Python (Django)| O sistema deve ser desenvolvido com a linguagem Python, usando o framework Django | Obrigatório |
| NF02 |  Sistema web| O sistema deve ser um sistema web | Obrigatório |


## 7 - Regras de Negócios

- O agendamento estará disposto em faixas de horários personalizáveis pelo estabelecimento de beleza conforme a duração do serviço e a necessidade.
- Um estabelecimento de beleza oferta ao menos um serviço.
- Os serviços são listados de acordo com a pesquisa feita.

## 8 - Glossário

- Estabelecimentos de beleza: Salões de beleza e/ou barbearias.
- Serviços de beleza: Serviços para cabelo e barba.
- Região: Bairro ou cidade.
