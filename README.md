# Laboratório de Ransomware Simulado em Python

Projeto educacional desenvolvido como prática de cibersegurança, inspirado em um desafio da DIO. O objetivo é compreender conceitos de criptografia de arquivos, recuperação de dados e verificação de integridade em um ambiente controlado.

## Objetivos

- Compreender a criptografia simétrica usando Fernet.
- Implementar criptografia e descriptografia de arquivos em Python.
- Verificar a integridade dos dados com SHA-256.
- Tratar falhas causadas por chaves incorretas.
- Praticar organização de código e tratamento de exceções.

## Tecnologias

- Python 3
- Kali Linux
- Biblioteca `cryptography`
- Fernet
- SHA-256

## Funcionamento

O programa oferece um menu interativo:

1. Criptografar uma cópia do arquivo de teste e exibir um aviso educativo.
2. Descriptografar a cópia para um novo arquivo.
0. Encerrar o programa.

A chave Fernet é armazenada localmente em `chave.key`. O arquivo original não é sobrescrito, e o programa evita substituir arquivos criptografados ou recuperados que já existam.

## Estrutura do projeto

```text
laboratorio-ransomware/
├── ransomware.py
├── README.md
├── .gitignore
├── chave.key
├── amostras/
│   ├── arquivo_teste.txt
│   └── AVISO_LABORATORIO.txt
└── .venv/
```

A chave, o ambiente virtual e os artefatos gerados durante os testes não devem ser publicados.

## Instalação

Crie e ative um ambiente virtual:

```bash
python -m venv .venv
source .venv/bin/activate
```

Instale a dependência:

```bash
python -m pip install cryptography
```

## Execução

```bash
python ransomware.py
```

Escolha uma das opções exibidas pelo menu.

## Testes realizados

- **Criptografia:** uma cópia do arquivo de teste foi criptografada, preservando o original.
- **Aviso educativo:** o programa exibiu a mensagem fictícia após criar a cópia criptografada.
- **Recuperação:** o conteúdo foi recuperado para um arquivo separado.
- **Integridade:** os hashes SHA-256 do original e do conteúdo recuperado coincidiram.
- **Chave incorreta:** a tentativa de recuperação com uma chave inválida foi rejeitada.
- **Proteção contra sobrescrita:** o programa recusou operações quando arquivos de saída já existiam.

Hash SHA-256 observado nos arquivos comparados:

```text
b83b0283a4febaab3ba77e0955de6cc14c6e07caed2d86a8f70ab3baeb8efa2e
```

A igualdade dos hashes confirma que os conteúdos comparados são idênticos.

## Segurança e limitações

Este projeto é uma simulação educacional, não um malware operacional. Ele utiliza arquivos de teste, não apaga o original, não possui mecanismos de propagação ou persistência e não solicita pagamentos reais.

A chave é necessária para recuperar os dados. Ela deve ser mantida em segurança e nunca publicada em um repositório público.

## Aprendizados

O laboratório permitiu praticar manipulação de arquivos com `pathlib`, criptografia com Fernet, tratamento de exceções, prevenção de sobrescrita e verificação de integridade com SHA-256.
