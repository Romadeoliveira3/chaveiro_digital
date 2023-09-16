# 1. Listas Encadeadas:

class NodoHistorico:
    def __init__(self, senha, dataAlteracao):
        self.senha = senha
        self.dataAlteracao = dataAlteracao
        self.proximo = None

class HistoricoSenha:
    def __init__(self):
        self.cabeca = None

    def adicionarHistorico(self, senha, dataAlteracao):
        novo_nodo = NodoHistorico(senha, dataAlteracao)
        novo_nodo.proximo = self.cabeca
        self.cabeca = novo_nodo

    def removerHistorico(self, data):
        atual = self.cabeca
        anterior = None
        while atual:
            if atual.dataAlteracao == data:
                if anterior:
                    anterior.proximo = atual.proximo
                else:
                    self.cabeca = atual.proximo
                return True
            anterior = atual
            atual = atual.proximo
        return False

    def buscarHistorico(self, data):
        atual = self.cabeca
        while atual:
            if atual.dataAlteracao == data:
                return atual.senha
            atual = atual.proximo
        return None

# 2. Pilhas:

class Acao:
    def __init__(self):
        self.pilha = []

    def empilharAcao(self, tipo, senha):
        self.pilha.append((tipo, senha))

    def desempilharAcao(self):
        if not self.pilha:
            return None
        return self.pilha.pop()

class HistoricoAcesso:
    def __init__(self):
        self.pilha = []

    def registrarAcesso(self, senha):
        self.pilha.append(senha)

    def verificarUltimoAcesso(self):
        if not self.pilha:
            return None
        return self.pilha[-1]

# 3. Filas:

class Notificacao:
    def __init__(self):
        self.fila = []

    def adicionarNotificacao(self, mensagem):
        self.fila.append(mensagem)

    def removerNotificacao(self):
        if not self.fila:
            return None
        return self.fila.pop(0)

class SolicitacaoSuporte:
    def __init__(self):
        self.fila = []

    def enviarSolicitacao(self, mensagem):
        self.fila.append(mensagem)

    def atenderSolicitacao(self):
        if not self.fila:
            return None
        return self.fila.pop(0)

# 4. Algoritmos de Ordenação e Busca:

class GerenciadorSenhas:
    def __init__(self):
        self.senhas = []

    def _particao(self, low, high):
        i = low - 1
        pivot = self.senhas[high]

        for j in range(low, high):
            if self.senhas[j] <= pivot:
                i += 1
                self.senhas[i], self.senhas[j] = self.senhas[j], self.senhas[i]

        self.senhas[i+1], self.senhas[high] = self.senhas[high], self.senhas[i+1]
        return i + 1

    def _quickSort(self, low, high):
        if low < high:
            pi = self._particao(low, high)
            self._quickSort(low, pi-1)
            self._quickSort(pi+1, high)

    def ordenarSenhas(self):
        n = len(self.senhas)
        self._quickSort(0, n-1)

    def buscarSenha(self, chave):
        # Usando busca linear como exemplo
        for senha in self.senhas:
            if senha == chave:
                return senha
        return None