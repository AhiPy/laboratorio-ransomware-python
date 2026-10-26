
from pathlib import Path
from cryptography.fernet import Fernet, InvalidToken

# ===== CONFIGURAÇÃO DO LABORATÓRIO =====
PASTA = Path(__file__).parent
PASTA_AMOSTRAS = PASTA / "amostras"

ARQUIVO_ORIGINAL = PASTA_AMOSTRAS / "arquivo_teste.txt"
ARQUIVO_CRIPTOGRAFADO = PASTA_AMOSTRAS / "arquivo_teste.txt.encrypted"
ARQUIVO_RECUPERADO = PASTA_AMOSTRAS / "arquivo_recuperado.txt"
ARQUIVO_CHAVE = PASTA / "chave.key"
ARQUIVO_AVISO = PASTA_AMOSTRAS / "AVISO_LABORATORIO.txt"


def gerar_chave():
    """Gera e salva uma chave Fernet para o laboratório."""
    chave = Fernet.generate_key()
    ARQUIVO_CHAVE.write_bytes(chave)
    return chave


def carregar_chave():
    """Carrega a chave existente ou cria uma nova."""
    if ARQUIVO_CHAVE.exists():
        return ARQUIVO_CHAVE.read_bytes()

    return gerar_chave()


def exibir_aviso():
    """Exibe a mensagem educativa da simulação."""
    if ARQUIVO_AVISO.is_file():
        print("\n=== AVISO DA SIMULAÇÃO ===")
        print(ARQUIVO_AVISO.read_text(encoding="utf-8"))
    else:
        print("Aviso da simulação não encontrado.")


def criptografar():
    """Criptografa uma cópia do arquivo original."""
    if not ARQUIVO_ORIGINAL.is_file():
        print("Arquivo original não encontrado.")
        return

    if ARQUIVO_CRIPTOGRAFADO.exists():
        print("O arquivo criptografado já existe. Nada foi alterado.")
        return

    try:
        chave = carregar_chave()
        fernet = Fernet(chave)

        conteudo = ARQUIVO_ORIGINAL.read_bytes()
        conteudo_criptografado = fernet.encrypt(conteudo)

        ARQUIVO_CRIPTOGRAFADO.write_bytes(conteudo_criptografado)

        print(f"Cópia criptografada criada: {ARQUIVO_CRIPTOGRAFADO.name}")
        exibir_aviso()

    except (ValueError, OSError) as erro:
        print(f"Não foi possível concluir a operação: {erro}")


def descriptografar():
    """Recupera o conteúdo para um novo arquivo."""
    if not ARQUIVO_CRIPTOGRAFADO.is_file():
        print("Arquivo criptografado não encontrado.")
        return

    if ARQUIVO_RECUPERADO.exists():
        print("O arquivo recuperado já existe. Nada foi alterado.")
        return

    if not ARQUIVO_CHAVE.is_file():
        print("Chave não encontrada. Recuperação cancelada.")
        return

    try:
        chave = ARQUIVO_CHAVE.read_bytes()
        fernet = Fernet(chave)

        conteudo_criptografado = ARQUIVO_CRIPTOGRAFADO.read_bytes()
        conteudo_original = fernet.decrypt(conteudo_criptografado)

        ARQUIVO_RECUPERADO.write_bytes(conteudo_original)

        print(f"Arquivo recuperado: {ARQUIVO_RECUPERADO.name}")
        print("A recuperação foi concluída.")

    except InvalidToken:
        print("Falha na recuperação: chave incorreta ou dados inválidos.")
    except (ValueError, OSError) as erro:
        print(f"Não foi possível concluir a recuperação: {erro}")


def menu():
    """Apresenta as opções do laboratório."""
    print("\n=== Laboratório DIO: Ransomware Simulado ===")
    print("1. Criptografar cópia e exibir aviso")
    print("2. Descriptografar para novo arquivo")
    print("0. Sair")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        criptografar()
    elif opcao == "2":
        descriptografar()
    elif opcao == "0":
        print("Encerrando o laboratório.")
    else:
        print("Opção inválida.")


if __name__ == "__main__":
    menu()
