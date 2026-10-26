# 🛡️ Python Ransomware Simulation Lab

<p align="center">
  <em>Simulação educacional de ransomware em Python com criptografia e recuperação controlada de arquivos</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Cryptography-6D597A?style=for-the-badge&logo=letsencrypt&logoColor=white" alt="Cryptography">
  <img src="https://img.shields.io/badge/Kali_Linux-557C94?style=for-the-badge&logo=kalilinux&logoColor=white" alt="Kali Linux">
  <img src="https://img.shields.io/badge/DIO-Laboratório-00C86F?style=for-the-badge" alt="DIO">
  <img src="https://img.shields.io/badge/Finalidade-Educacional-2E8B57?style=for-the-badge" alt="Finalidade educacional">
</p>

```console
┌──(kali㉿kali)-[~/laboratorio-ransomware]
└─$ cat objetivo.txt
  [+] linguagem ..: Python
  [+] objetivo ...: estudar criptografia e ransomware
  [+] ambiente ...: laboratorio controlado
  [+] validacao ..: recuperacao + hash SHA-256
  [+] seguranca ..: original preservado
```

Projeto prático de cibersegurança desenvolvido como laboratório educacional em Python. O objetivo é compreender o fluxo básico de criptografia de arquivos, recuperação dos dados e validação de integridade, observando como essas etapas se relacionam com o funcionamento de um ransomware.

> [!CAUTION]
> **Uso exclusivamente educacional.** A simulação foi projetada para trabalhar com arquivos de teste, mantendo o original preservado. Não há exclusão de arquivos nem propagação. Execute somente em um ambiente controlado e autorizado. Este projeto não deve ser utilizado contra dados ou sistemas de terceiros.

## 📑 Índice

- [Objetivos](#-objetivos)
- [Tecnologias utilizadas](#-tecnologias-utilizadas)
- [Estrutura do projeto](#-estrutura-do-projeto)
- [Funcionamento](#-funcionamento)
- [Instalação e execução](#-instalação-e-execução)
- [Testes e validações](#-testes-e-validações)
- [Segurança e limitações](#-segurança-e-limitações)
- [Aprendizados](#-aprendizados)

## 🎯 Objetivos

- Compreender o uso de criptografia simétrica em Python.
- Utilizar a biblioteca `cryptography` para proteger e recuperar um arquivo de teste.
- Separar as etapas de geração, armazenamento e carregamento da chave.
- Implementar um fluxo controlado de criptografia e descriptografia.
- Validar a integridade do arquivo recuperado por meio do SHA-256.
- Documentar os limites de segurança de uma simulação educacional.

## 🧰 Tecnologias utilizadas

| Tecnologia | Finalidade |
|---|---|
| Python | Implementação da lógica da simulação |
| `cryptography` | Operações criptográficas |
| Kali Linux | Ambiente de desenvolvimento e testes |
| `venv` | Isolamento das dependências Python |
| SHA-256 | Comparação da integridade dos arquivos |
| Git e GitHub | Versionamento e documentação do projeto |

## 📂 Estrutura do projeto

```text
laboratorio-ransomware/
├── amostras/
│   ├── arquivo_teste.txt
│   └── AVISO_LABORATORIO.txt
├── ransomware.py
├── .gitignore
└── README.md
```

**Observação:** a chave criptográfica e os arquivos gerados durante os testes são artefatos locais e não devem ser publicados no repositório. O `.gitignore` foi configurado para evitar que esses arquivos sejam enviados acidentalmente.

## ⚙️ Funcionamento

O programa organiza o processo em funções responsáveis por etapas específicas:

| Função | Responsabilidade |
|---|---|
| `gerar_chave()` | Gera a chave criptográfica |
| `carregar_chave()` | Carrega a chave utilizada na operação |
| `exibir_aviso()` | Exibe o aviso educativo da simulação |
| `criptografar()` | Executa a criptografia do arquivo de teste |
| `descriptografar()` | Recupera o conteúdo para um arquivo separado |
| `menu()` | Organiza a interação com o usuário |

### 🔄 Fluxo da simulação

```text
Arquivo de teste
       │
       ▼
Geração/carregamento da chave
       │
       ▼
Criptografia da cópia de teste
       │
       ▼
Arquivo criptografado
       │
       ▼
Descriptografia controlada
       │
       ▼
Arquivo recuperado separado
       │
       ▼
Comparação dos hashes SHA-256
```

O fluxo foi pensado para permitir a observação das operações sem destruir o arquivo original.

## 🚀 Instalação e execução

### 1. Clonar o repositório

```bash
git clone https://github.com/AhiPy/laboratorio-ransomware-python.git
cd laboratorio-ransomware-python
```

### 2. Criar e ativar o ambiente virtual

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalar a dependência

```bash
python -m pip install cryptography
```

### 4. Preparar e executar

Confira se o arquivo de teste `amostras/arquivo_teste.txt` existe e contém somente dados fictícios.

```bash
python ransomware.py
```

Siga as opções apresentadas pelo programa para executar a simulação e a recuperação.

### 5. Verificar a sintaxe

```bash
python -m py_compile ransomware.py
```

Resultado observado durante o desenvolvimento:

```text
Sintaxe válida.
```

## 🧪 Testes e validações

Os seguintes resultados foram verificados durante o desenvolvimento do laboratório:

| Teste | Resultado |
|---|---|
| Compilação da sintaxe Python | ✅ Aprovada |
| Criptografia do arquivo de teste | ✅ Funcionou |
| Preservação do arquivo original | ✅ Confirmada |
| Recuperação com a chave correta | ✅ Funcionou |
| Tentativa com chave incorreta | ✅ Rejeitada |
| Comparação de hashes SHA-256 | ✅ Hashes coincidentes |
| Proteção de artefatos com `.gitignore` | ✅ Regras verificadas |

### 🔐 Validação de integridade

O hash SHA-256 obtido para o arquivo original e para o arquivo recuperado foi:

```text
b83b0283a4febaab3ba77e0955de6cc14c6e07caed2d86a8f70ab3baeb8efa2e
```

A coincidência dos hashes confirma que o conteúdo do arquivo recuperado corresponde ao original usado no teste.

> A validação demonstra a integridade do arquivo recuperado neste cenário específico. Ela não representa, por si só, uma avaliação completa da segurança do programa.

## 🔒 Segurança e limitações

Este projeto é uma simulação didática, não um ransomware pronto para uso real.

- Trabalha com um arquivo de teste controlado.
- Mantém o arquivo original preservado.
- Salva a recuperação em um arquivo separado.
- Não implementa propagação ou exclusão de arquivos.
- Utiliza uma chave local, que precisa ser protegida e não deve ser publicada.
- Não inclui mecanismos de persistência, evasão ou controle remoto.

A segurança de uma implementação criptográfica real depende também do gerenciamento de chaves, do tratamento de erros, do armazenamento dos dados e de outros requisitos que estão além do escopo deste laboratório.

## 📚 Aprendizados

Durante o desenvolvimento, foram praticados conceitos importantes:

- Organização de código Python em funções.
- Uso de uma biblioteca criptográfica.
- Separação entre criptografia e recuperação de dados.
- Tratamento de uma tentativa de recuperação com chave incorreta.
- Verificação de integridade usando SHA-256.
- Isolamento de dependências com ambiente virtual.
- Uso do Git, `.gitignore` e GitHub para versionamento.
- Documentação técnica de um exercício de cibersegurança.

---

<p align="center">
  <sub>Projeto educacional de cibersegurança desenvolvido em Python. Implementação, testes e validações executados por mim; documentação organizada e revisada com apoio de I.A.</sub>
</p>
