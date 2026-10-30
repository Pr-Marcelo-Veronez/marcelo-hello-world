# marcelo-hello-world
Desafio AWS EC2 com deploy automático via GitHub Actions
 
# Server 1 — Ambiente de Desenvolvimento

## Objetivo do projeto

Este servidor foi criado para hospedar a primeira versão da aplicação **Marcelo Hello World**, utilizando os serviços da AWS e integração com o GitHub.

O objetivo é demonstrar, na prática, como funciona a publicação automática de uma aplicação em um servidor Linux na nuvem.

## Como funciona

O código-fonte da aplicação fica armazenado neste repositório GitHub, na branch `main`.

Sempre que uma alteração é realizada e enviada para essa branch, o GitHub Actions inicia automaticamente um processo de atualização do servidor.

Esse processo funciona da seguinte maneira:

1. O desenvolvedor altera o código da aplicação.
2. As alterações são enviadas para a branch `main` do GitHub.
3. O GitHub Actions identifica a atualização e inicia o processo de publicação.
4. O GitHub autentica-se na AWS por meio de uma integração segura chamada OIDC, utilizando uma função IAM.
5. O AWS Systems Manager (SSM) recebe o comando de atualização e executa as operações no servidor EC2.
6. O servidor atualiza os arquivos da aplicação e reinicia o serviço.
7. Ao final, o processo verifica se a aplicação está funcionando corretamente.

## Estrutura do servidor

- **Plataforma:** Amazon Web Services (AWS).
- **Serviço:** Amazon EC2.
- **Sistema operacional:** Ubuntu Server.
- **Servidor web:** Nginx.
- **Aplicação:** Python.
- **Serviço da aplicação:** Systemd.
- **Automação:** GitHub Actions.
- **Comunicação com a AWS:** IAM, OIDC e Systems Manager (SSM).

O Nginx recebe as requisições dos usuários pela porta HTTP 80 e encaminha essas solicitações para a aplicação Python, que funciona internamente na porta 8000.

## Resultado

O ambiente de desenvolvimento permite que cada alteração enviada para a branch `main` seja publicada automaticamente no primeiro servidor EC2, sem a necessidade de acessar o servidor manualmente por SSH.

Esse processo facilita os testes, agiliza as atualizações e demonstra o funcionamento de uma integração CI/CD entre GitHub e AWS.

**Importante:** Este servidor representa o ambiente de desenvolvimento do projeto. As alterações são publicadas automaticamente, permitindo validar as modificações antes da atualização do ambiente de produção.
