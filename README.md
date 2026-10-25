# GitLab CI/CD & Docker — Pipeline de Integração Contínua

![GitLab CI](https://img.shields.io/badge/GitLab_CI-Automacao-2ea44f?style=for-the-badge&logo=gitlab&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Containers-00875a?style=for-the-badge&logo=docker&logoColor=white)
![Python](https://img.shields.io/badge/Python-3-1b5e20?style=for-the-badge&logo=python&logoColor=white)
![Licença](https://img.shields.io/badge/Licenca-MIT-2e7d32?style=for-the-badge)

Laboratório acadêmico de Infraestrutura Ágil, desenvolvido por Weslley Ribeiro. Automatiza a construção e publicação de uma imagem Docker, a execução de um gráfico em caracteres com Python e a apresentação de uma notificação condicional no log.

Os badges acima identificam tecnologias e licença; não são verificações automáticas de execução.

## Resultado comprovado

O [pipeline 2983624730](https://gitlab.com/Weslley-Ribeiro/unopar_ci_cd/-/pipelines/2983624730), no projeto GitLab original, foi aprovado para o commit `c3373f58`. A imagem publicada foi `weslleyribeiro01/unopar-ci-cd:c3373f58`.

| Etapa | Job | Resultado |
| --- | --- | --- |
| pre-build | build-docker | Aprovado; 1 min 27 s |
| build | build-project | Aprovado; 23 s |
| notificacao | notificacao-sucesso | Aprovado; 19 s |
| notificacao | notificacao-falhas | Ignorado conforme on_failure |

As evidências se referem à execução no GitLab original. Publicar este espelho no GitHub não executa GitLab CI nem comprova uma nova execução.

## Arquitetura

```text
GitLab / main
    |
    v
pre-build: Docker build -> Docker Hub / tag do commit
    |
    v
build: imagem publicada -> programa Python -> gráfico no log
    |
    v
notificacao: horário + Sucesso (ou Falha, conforme resultado anterior)
```

## Estrutura

- `.gitlab-ci.yml`: pipeline com Docker-in-Docker e TLS.
- `Dockerfile`: base Ubuntu com Python 3 e pip, conforme laboratório.
- `plot_simples_grafico.py`: gráfico em caracteres, entrada [4, 3, 2, 2, 5].
- `relogio.py`: data e hora do ambiente.
- `notificacaoSucesso.sh` e `notificacaoFalha.sh`: mensagens no terminal.
- `requirements.txt`: informa a ausência de dependências externas.
- `LICENSE`: licença MIT para este repositório; preservar atribuições de materiais de terceiros.

O código do gráfico preserva a lógica apresentada no laboratório, com formatação compactada na inicialização da matriz.

## Execução local

Com Python 3 instalado:

```sh
python3 plot_simples_grafico.py
python3 relogio.py
sh notificacaoSucesso.sh
```

Com Docker instalado:

```sh
docker build -t unopar-ci-cd:local .
docker run --rm -v "$PWD:/workspace" -w /workspace unopar-ci-cd:local python3 plot_simples_grafico.py
```

O Dockerfile original instala o ambiente, mas não copia o programa nem define CMD; por isso o exemplo local monta o código e especifica o comando. Não confundir essa montagem local com o checkout realizado pelo GitLab Runner.

## Reprodução no GitLab

1. Disponibilize estes arquivos na raiz de um projeto GitLab.
2. Configure um runner compatível com Docker-in-Docker e certificados TLS.
3. Defina `DOCKERHUB_USERNAME` e `DOCKERHUB_TOKEN` nas variáveis de CI/CD; use token com permissão de publicação e proteja as variáveis conforme a política da conta.
4. Ajuste `APP_IMAGE` para um repositório Docker Hub sob seu controle.
5. Execute o pipeline e confira cada job e a publicação da tag.

Nunca versione credenciais. Exigências de identidade e permissões da plataforma devem ser resolvidas na própria conta.

## Evidências e documentação

Os quatro prints foram fornecidos e analisados, mas ainda não foram enviados como arquivos de imagem a este repositório. O conector utilizado para esta publicação aceita gravação textual, sem parâmetro de upload binário. Não foram criados links de imagens inexistentes.

Nomes previstos para os arquivos na raiz:

| Arquivo | Evidência |
| --- | --- |
| pipeline-execution.png | Visão geral do pipeline aprovado |
| docker-build.png | Construção e envio ao Docker Hub |
| python-execution.png | Gráfico e Job succeeded |
| success-notification.png | Horário, Sucesso e Job succeeded |

Converter os JPEGs para PNG antes de usar esses nomes. Após o upload, incorporar as imagens ao README e verificar sua exibição.

- [Memória técnica e inventário anteriores](https://github.com/Weslley-Ribeiro/Projetos-Faculdade/tree/main/Infraestrutura-Agil/UNOPAR-CI-CD)
- [Projeto original no GitLab](https://gitlab.com/Weslley-Ribeiro/unopar_ci_cd)
- [Build Docker](https://gitlab.com/Weslley-Ribeiro/unopar_ci_cd/-/jobs/17433017645)
- [Execução Python](https://gitlab.com/Weslley-Ribeiro/unopar_ci_cd/-/jobs/17433017646)
- [Notificação](https://gitlab.com/Weslley-Ribeiro/unopar_ci_cd/-/jobs/17433017647)

O relatório acadêmico final tem 13 páginas e sua entrega foi informada pelo autor. PDF e Word não estão publicados aqui para evitar exposição automática da identificação acadêmica.

## Limitações e adaptações do prompt

- Preservadas as três etapas originais; não substituídas por lint-and-test e build-and-push.
- Não adicionada aplicação app.py sem relação com as evidências.
- Não adicionados pytest e flake8 como se tivessem sido utilizados.
- Não houve teste controlado de falha nem validação de on_failure em execução.
- Não há deploy em produção ou testes automatizados comprovados; push para registro não é implantação da aplicação.
- Tag por hash de commit identifica revisão; não é versionamento semântico.
- Base Ubuntu não fixa versão e não foi configurado usuário não-root no laboratório. Melhorias futuras não são resultados já obtidos.
- Não foi comprovada publicação de tag latest; o resultado documentado usa c3373f58.

## Evoluções futuras

- [ ] Publicar e incorporar as quatro imagens.
- [ ] Testar falha controlada em branch separada.
- [ ] Adicionar testes reais e lint, com novas evidências.
- [ ] Avaliar fixação da imagem base e execução não-root em nova versão.

## Referências

- https://docs.gitlab.com/ci/
- https://docs.docker.com/get-started/docker-concepts/building-images/writing-a-dockerfile/
