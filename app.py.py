class ChaveiroDigital:
    def __init__(self):
        self.cadastros = []
        self.notificacao = None
        self.ultima_acao = None

    def adicionar_cadastro(self):
        descricao = input("Descrição do cadastro: ")
        login = input("Login do cadastro: ")
        senha = input("Senha do cadastro: ")
        data = input("Data do cadastro (dd-mm-aaaa): ")
        prioridade = int(input("Prioridade (0-10): "))
        nome = input("Nome do usuário: ")
        cadastro = {
            "descricao": descricao,
            "login": login,
            "senha": senha,
            "data": data,
            "prioridade": prioridade,
            "nome": nome
        }
        self.cadastros.append(cadastro)
        self.ultima_acao = ("adicionar", cadastro)

    def mostrar_todas_senhas(self):
        for cadastro in self.cadastros:
            print(cadastro)

    def mostrar_senhas_por_usuario(self, nome):
        for cadastro in self.cadastros:
            if cadastro["nome"] == nome:
                print(cadastro)

    def mostrar_senhas_por_prioridade(self, prioridade):
        for cadastro in self.cadastros:
            if cadastro["prioridade"] == prioridade:
                print(cadastro)

    def mostrar_senhas_por_data(self, data):
        for cadastro in self.cadastros:
            if cadastro["data"] == data:
                print(cadastro)

    def mostrar_senhas_por_descricao(self, descricao):
        for cadastro in self.cadastros:
            if cadastro["descricao"] == descricao:
                print(cadastro)

    def excluir_cadastro(self, descricao):
        for cadastro in self.cadastros:
            if cadastro["descricao"] == descricao:
                self.cadastros.remove(cadastro)
                self.ultima_acao = ("excluir", cadastro)
                return
        print("Descrição não encontrada.")

    def modificar_cadastro(self, descricao):
        for cadastro in self.cadastros:
            if cadastro["descricao"] == descricao:
                self.adicionar_cadastro()
                self.cadastros.remove(cadastro)
                return
        print("Descrição não encontrada.")

    def buscar_senha(self, senha):
        for cadastro in self.cadastros:
            if cadastro["senha"] == senha:
                print(cadastro)
                return
        print("Senha não encontrada.")

    def mostrar_ultimo_acesso(self):
        if self.cadastros:
            print(self.cadastros[-1]["data"])
        else:
            print("Nenhuma atividade registrada.")

    def criar_notificacao(self, mensagem):
        self.notificacao = mensagem

    def exibir_notificacao(self):
        if self.notificacao:
            print(self.notificacao)
        else:
            print("Nenhuma notificação.")

    def desfazer_acao(self):
        if self.ultima_acao:
            acao, cadastro = self.ultima_acao
            if acao == "adicionar":
                self.cadastros.remove(cadastro)
            elif acao == "excluir":
                self.cadastros.append(cadastro)
            print(f"Ação {acao} desfeita.")
        else:
            print("Nenhuma ação para desfazer.")

def menu():
    print("\nChaveiro Digital")
    print("1. Adicionar Cadastro")
    print("2. Mostrar todas senhas")
    print("3. Mostrar senhas por usuário")
    print("4. Mostrar senhas por prioridade")
    print("5. Mostrar senhas por data")
    print("6. Mostrar senhas por descrição")
    print("7. Excluir Cadastro")
    print("8. Modificar Cadastro")
    print("9. Buscar senha")
    print("10. Mostrar último acesso")
    print("11. Criar notificação")
    print("12. Exibir notificação")
    print("13. Desfazer ação")
    print("0. Sair do sistema")
    return int(input("Escolha uma opção: "))

def main():
    chaveiro = ChaveiroDigital()
    while True:
        opcao = menu()
        if opcao == 1:
            chaveiro.adicionar_cadastro()
        elif opcao == 2:
            chaveiro.mostrar_todas_senhas()
        elif opcao == 3:
            nome = input("Nome do usuário: ")
            chaveiro.mostrar_senhas_por_usuario(nome)
        elif opcao == 4:
            prioridade = int(input("Prioridade (0-10): "))
            chaveiro.mostrar_senhas_por_prioridade(prioridade)
        elif opcao == 5:
            data = input("Data (dd-mm-aaaa): ")
            chaveiro.mostrar_senhas_por_data(data)
        elif opcao == 6:
            descricao = input("Descrição: ")
            chaveiro.mostrar_senhas_por_descricao(descricao)
        elif opcao == 7:
            descricao = input("Descrição do cadastro a ser excluído: ")
            chaveiro.excluir_cadastro(descricao)
        elif opcao == 8:
            descricao = input("Descrição do cadastro a ser modificado: ")
            chaveiro.modificar_cadastro(descricao)
        elif opcao == 9:
            senha = input("Senha: ")
            chaveiro.buscar_senha(senha)
        elif opcao == 10:
            chaveiro.mostrar_ultimo_acesso()
        elif opcao == 11:
            mensagem = input("Mensagem da notificação: ")
            chaveiro.criar_notificacao(mensagem)
        elif opcao == 12:
            chaveiro.exibir_notificacao()
        elif opcao == 13:
            chaveiro.desfazer_acao()
        elif opcao == 0:
            print("Saindo do Chaveiro Digital...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
