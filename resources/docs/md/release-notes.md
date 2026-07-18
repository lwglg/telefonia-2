# Luxus.Connect | Release Notes

## TOC

<!-- TOC -->

- [Luxus.Connect | Release Notes](#luxusconnect--release-notes)
    - [TOC](#toc)
    - [Demandas priorizadas](#demandas-priorizadas)
    - [Demandas mapeadas e julgadas necessárias pelo responsável técnico](#demandas-mapeadas-e-julgadas-necess%C3%A1rias-pelo-respons%C3%A1vel-t%C3%A9cnico)
    - [Release notes](#release-notes)
        - [Dia 14/07/2026:](#dia-14072026)
        - [Dia 18/07/2026:](#dia-18072026)
    - [Prestadora de serviços](#prestadora-de-servi%C3%A7os)
        - [Identificação](#identifica%C3%A7%C3%A3o)
        - [Horas e custos](#horas-e-custos)
    - [O que deseja fazer?](#o-que-deseja-fazer)

<!-- /TOC -->

## Demandas priorizadas

- **Reestruturação do projeto**:
    - Camada de automação de exeucução do Docker Compose;
    - Análise da base de código Go do [backend] de modo a estabelecer o que é passível de ser testado;
    - Elaborar estratégia para implementação de testes automatizados, com no mínimo um teste de integração, e.g. geração de faturas via integração com Sicredi;
- **Deployment no provedor de cloud Railway (projeto [keen-generosity])**:
    - Preparação de stacks individuais para deployment específico de cada serviço no Railway
    - Adaptação de serviços no Docker Compose de desenvolvimento, de modo a construir manifesto de produção com limitação de consumo de recursos (RAM, volumes)

## Demandas mapeadas e julgadas necessárias pelo responsável técnico

- ***Docker Registry corporativo**:
    - Estudar uma forma de criar um registro de imagens customizadas da plataforma Docker para os diferentes serviços que compõem a plataforma em questão (`postgres`, `keycloak`, `rabbitmq`, `backend`, `frontend`, `seq`).
        - **Sugestão**: Haja vista que o Railway já possui uma integração com projetos (repositórios) do Github, existem também uma maneira de integrar a criação de instância de serviços de cloud com um Docker Registry do próprio Github. Basta:
            - Realizar o upgrade (ou criação) da organização da empresa no Github e.g. (`github.com/luxus`);
            - Transferir este repositório, possivelmente com um nome atualizado, e.g. `github.com/luxus/luxus-connect`;
            - Realizar a criação de um [**Github Container Registry (GHCR)**](https://docs.github.com/pt/packages/working-with-a-github-packages-registry/working-with-the-container-registry) associado à organização;
            - Implementar pipelines de CD para fazer build e registro automatizado das imagens do repositório de modo a serem consumidas pelo Raiway;
            - Integrar GHCR com o Railway corporativo. Documentação pode ser conferida [aqui](https://docs.railway.com/builds/private-registries) 

## Release notes

### Dia 14/07/2026:
- Intervalos de tempo dedicados:
    - **09:27 às 12:31**:
        - Expansão da camada inicial de scripts de automação do projeto;
        - Descontinuação do elementos associados à estrutura inicial do projeto, 
        - Descontinuação da estrutura inicial de dockerização de serviços via Docker Compose;
    - **13:25 às 18:00**:
        - Reagrupamento do antigo serviço de back-end em Go (`api`) em nova pasta (`backend`), com transferência de declarações de imagens para camada de infra dedicada (`ìnfra/docker/develop/backend`);
        - Reagrupamento do antigo serviço de front-end em Vue.js (`src`) em nova pasta (`frontend`), com transferência de declarações de imagens para camada de infra dedicada (`ìnfra/docker/develop/frontend`);
        - Testes exploratórios iniciais dos mecanismos de building dos novos serviços em `ìnfra/docker/develop/docker-compose.yml`;
- Commits do período na branch `refactor/project-reorganization`: Listagem no fork do [projeto](https://github.com/lwglg/telefonia-2/commits/refactor/project-reorganization/?author=lwglg&since=2026-07-01&until=2026-07-14).

### Dia 18/07/2026:
- Intervalos de tempo dedicaddos:
    - **08:30 às 12:00**:
        - Correção da sequência de aplicação de scripts de migração SQL na inicialização do serviço `postgresql`;
        - Implementação da estrutura customizada de entrypoint para o serviço `keycloak`;
        - Implementação de estágio inicial de buiding na imagem Docker do serviço `keycloak` de modo a possibilitar execução de scripts SQL internamente ao container, em conexão com o serviço `postgres`;
        - Redação da seção de documentação de release notes;
        - Correção do script de prunning de serviços em execução e ociosos do Docker;
- Commits do período na branch `refactor/project-reorganization` Listagem no fork do [projeto](https://github.com/lwglg/telefonia-2/commits/refactor/project-reorganization/?author=lwglg&since=2026-07-18&until=2026-07-18).

## Prestadora de serviços

### Identificação
- **Guilherme L. Gonçalves Desenvolvimento de Sistemas Ltda. (44.867.072/0001-06)**
- Contato:
    - E-mail: [lwglguilherme@gmail.com](mailto:lwglguilherme@gmail.com);
    - Telefone: [+55 (51) 98199 9952](https://wa.me/55519981999952).

### Horas e custos
- Planilha de apontamento de horas com os custos de desenvolvimento já calculados pode ser acessada [aqui](https://docs.google.com/spreadsheets/d/1tTr04UYyuMSEAELLE6anzc5VU5NdvgoQauqQKjzVzTk/edit?usp=sharing).

---
## O que deseja fazer?

- [Voltar ao topo](#toc)
- [Voltar à raíz](../../../README.md)
