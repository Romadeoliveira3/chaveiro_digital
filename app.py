from func import *

def menu_principal():
    print("\nChaveiro Digital - Menu Principal")
    print("1. Adicionar senha ao histórico")
    print("2. Remover senha do histórico")
    print("3. Buscar senha no histórico")
    print("4. Registrar ação")
    print("5. Desfazer última ação")
    print("6. Registrar acesso a uma senha")
    print("7. Verificar último acesso")
    print("8. Adicionar notificação")
    print("9. Ler notificação")
    print("10. Enviar solicitação de suporte")
    print("11. Atender solicitação de suporte")
    print("12. Adicionar senha ao gerenciador")
    print("13. Ordenar senhas")
    print("14. Buscar senha")
    print("15. Sair")
    return int(input("Escolha uma opção: "))

def main():
    hs = HistoricoSenha()
    acao = Acao()
    ha = HistoricoAcesso()
    notif = Notificacao()
    ss = SolicitacaoSuporte()
    gs = GerenciadorSenhas()

    while True:
        escolha = menu_principal()

        if escolha == 1:
            senha = input("Digite a senha: ")
            data = input("Digite a data (dd-mm-aaaa): ")
            hs.adicionarHistorico(senha, data)
            print("Senha adicionada ao histórico.")

        elif escolha == 2:
            data = input("Digite a data da senha a ser removida (dd-mm-aaaa): ")
            hs.removerHistorico(data)
            print("Senha removida do histórico.")

        elif escolha == 3:
            data = input("Digite a data da senha a ser buscada (dd-mm-aaaa): ")
            senha = hs.buscarHistorico(data)
            if senha:
                print(f"Senha encontrada: {senha}")
            else:
                print("Senha não encontrada.")

        elif escolha == 4:
            tipo = input("Digite o tipo de ação (adicionar, modificar, excluir): ")
            senha = input("Digite a senha associada à ação: ")
            acao.empilharAcao(tipo, senha)
            print("Ação registrada.")

        elif escolha == 5:
            acao_desfeita = acao.desempilharAcao()
            if acao_desfeita:
                print(f"Ação desfeita: {acao_desfeita[0]} - {acao_desfeita[1]}")
            else:
                print("Nenhuma ação para desfazer.")

        elif escolha == 6:
            senha = input("Digite a senha acessada: ")
            ha.registrarAcesso(senha)
            print("Acesso registrado.")

        elif escolha == 7:
            ultimo_acesso = ha.verificarUltimoAcesso()
            if ultimo_acesso:
                print(f"Última senha acessada: {ultimo_acesso}")
            else:
                print("Nenhum acesso registrado.")

        elif escolha == 8:
            mensagem = input("Digite a mensagem da notificação: ")
            notif.adicionarNotificacao(mensagem)
            print("Notificação adicionada.")

        elif escolha == 9:
            notificacao = notif.removerNotificacao()
            if notificacao:
                print(f"Notificação: {notificacao}")
            else:
                print("Nenhuma notificação.")

        elif escolha == 10:
            mensagem = input("Digite a mensagem da solicitação de suporte: ")
            ss.enviarSolicitacao(mensagem)
            print("Solicitação enviada.")

        elif escolha == 11:
            solicitacao = ss.atenderSolicitacao()
            if solicitacao:
                print(f"Solicitação atendida: {solicitacao}")
            else:
                print("Nenhuma solicitação pendente.")

        elif escolha == 12:
            senha = input("Digite a senha a ser adicionada: ")
            gs.senhas.append(senha)
            print("Senha adicionada.")

        elif escolha == 13:
            gs.ordenarSenhas()
            print("Senhas ordenadas.")

        elif escolha == 14:
            chave = input("Digite a senha a ser buscada: ")
            senha = gs.buscarSenha(chave)
            if senha:
                print(f"Senha encontrada: {senha}")
            else:
                print("Senha não encontrada.")

        elif escolha == 15:
            print("Saindo do Chaveiro Digital...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
