def cifrar_caractere(char, chave):
    """
    Cifra um único caractere usando a Cifra de César.
    
    Args:
        char (str): Caractere a ser cifrado
        chave (int): Número de posições para deslocar
    
    Returns:
        str: Caractere cifrado
    """
    # Se não for uma letra, retorna o caractere inalterado
    if not char.isalpha():
        return char
    
    # Define o ponto de início do alfabeto (A ou a)
    inicio = ord('A') if char.isupper() else ord('a')
    
    # Calcula a nova posição com wrap around usando módulo 26
    posicao_atual = ord(char) - inicio
    nova_posicao = (posicao_atual + chave) % 26
    
    # Converte de volta para caractere
    return chr(inicio + nova_posicao)


def cifra_cesar(texto, chave):
    """
    Aplica a Cifra de César em um texto completo.
    
    Args:
        texto (str): Texto a ser cifrado
        chave (int): Chave de deslocamento
    
    Returns:
        str: Texto cifrado
    """
    resultado = ""
    
    # Processa cada caractere do texto
    for char in texto:
        resultado += cifrar_caractere(char, chave)
    
    return resultado


def obter_chave():
    """
    Solicita e valida a entrada da chave do usuário.
    
    Returns:
        int: Chave válida inserida pelo usuário
    """
    while True:
        try:
            chave = int(input("Digite a chave (número inteiro): "))
            return chave
        except ValueError:
            print("❌ Erro: Por favor, digite um número inteiro válido.")


def main():
    """
    Função principal que executa o programa da Cifra de César.
    """
    print("🔐 CIFRA DE CÉSAR")
    print("=" * 40)
    
    # Solicita o texto do usuário
    texto_original = input("Digite o texto que deseja cifrar: ")
    
    # Solicita e valida a chave
    chave = obter_chave()
    
    # Aplica a cifra
    texto_cifrado = cifra_cesar(texto_original, chave)
    
    # Exibe os resultados
    print("\n📝 RESULTADOS:")
    print("=" * 40)
    print(f"Texto original: {texto_original}")
    print(f"Chave utilizada: {chave}")
    print(f"Texto cifrado: {texto_cifrado}")
    
    # Opção para descriptografar
    print(f"\n💡 Para descriptografar, use a chave: {-chave}")
    
    # Pergunta se deseja descriptografar
    descriptografar = input("\nDeseja descriptografar o texto? (s/n): ").lower()
    if descriptografar in ['s', 'sim', 'y', 'yes']:
        texto_descriptografado = cifra_cesar(texto_cifrado, -chave)
        print(f"Texto descriptografado: {texto_descriptografado}")


def testar_exemplos():
    """
    Função para testar os exemplos fornecidos na descrição.
    """
    print("🧪 TESTANDO EXEMPLOS:")
    print("=" * 40)
    
    # Exemplos da descrição
    exemplos = [
        ("abc", 1, "bcd"),
        ("ABCDE", 2, "CDEFG"), 
        ("Cachorro", -1, "Bzbgnqqn"),
        ("Olá Mundo!", 3, "Roá Pxqgr!")
    ]
    
    for texto, chave, esperado in exemplos:
        resultado = cifra_cesar(texto, chave)
        status = "✅" if resultado == esperado else "❌"
        print(f'{status} "{texto}" + {chave} = "{resultado}" (esperado: "{esperado}")')


if __name__ == "__main__":
    # Executa os testes primeiro
    testar_exemplos()
    print("\n")
    
    # Executa o programa principal
    main()