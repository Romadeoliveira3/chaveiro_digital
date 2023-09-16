import unittest
from func import *

class TestChaveiroDigital(unittest.TestCase):

    # Testes para HistoricoSenha
    def test_historico_senha(self):
        print("Executando teste para HistoricoSenha...")
        hs = HistoricoSenha()
        hs.adicionarHistorico("senha123", "01-01-2022")
        self.assertEqual(hs.buscarHistorico("01-01-2022"), "senha123")
        hs.removerHistorico("01-01-2022")
        self.assertIsNone(hs.buscarHistorico("01-01-2022"))

    # Testes para Acao
    def test_acao(self):
        print("Executando teste para Acao...")
        acao = Acao()
        acao.empilharAcao("adicionar", "senha123")
        self.assertEqual(acao.desempilharAcao(), ("adicionar", "senha123"))

    # Testes para HistoricoAcesso
    def test_historico_acesso(self):
        print("Executando teste para HistoricoAcesso...")
        ha = HistoricoAcesso()
        ha.registrarAcesso("senha123")
        self.assertEqual(ha.verificarUltimoAcesso(), "senha123")

    # Testes para Notificacao
    def test_notificacao(self):
        print("Executando teste para Notificacao...")
        notif = Notificacao()
        notif.adicionarNotificacao("Senha fraca!")
        self.assertEqual(notif.removerNotificacao(), "Senha fraca!")

    # Testes para SolicitacaoSuporte
    def test_solicitacao_suporte(self):
        print("Executando teste para SolicitacaoSuporte...")
        ss = SolicitacaoSuporte()
        ss.enviarSolicitacao("Erro ao adicionar senha!")
        self.assertEqual(ss.atenderSolicitacao(), "Erro ao adicionar senha!")

    # Testes para GerenciadorSenhas
    def test_gerenciador_senhas(self):
        print("Executando teste para GerenciadorSenhas...")
        gs = GerenciadorSenhas()
        gs.senhas = ["banana", "apple", "cherry"]
        gs.ordenarSenhas()
        self.assertEqual(gs.senhas, ["apple", "banana", "cherry"])
        self.assertEqual(gs.buscarSenha("banana"), "banana")
        self.assertIsNone(gs.buscarSenha("grape"))

if __name__ == "__main__":
    unittest.main()
