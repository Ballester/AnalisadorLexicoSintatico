from automato import Automato

class Lexico(object):

	#Delimitadores para transformar os varios em uma so transicao no automato
	def __init__(self, arq):
		self.reservadas = []
		self.delimitadores = []
		self.aut = Automato()
		self.arq = open(arq).readlines()
		self.linha_atual = 0
		self.col_atual = 0

	def insereEstado(self, est, final=False):
		self.aut.insereEstado(est, final)

	def insereTrans(self, est1, est2, simbolo):
		self.aut.insereTrans(est1, est2, simbolo)

	def setInicial(self, est):
		self.aut.setInicial(est)

	def insereDelimitador(self, dele):
		self.delimitadores.append(dele)

	def insereReservada(self, res):
		self.reservadas.append(res)

	#Retorna token se verdadeiro ou tupla com linha e coluna do erro, ex: ('ERRO', linha, coluna)
	def scanner(self):
		token = ''
		self.aut.resetInicial()
		for i in range(self.col_atual, len(self.arq[self.linha_atual])):
			aux = self.arq[self.linha_atual][self.col_atual]
			if aux in self.delimitadores and token != '':
				if self.aut.isFinal():
					return token
				else:
					return ('ERRO', self.linha_atual, self.col_atual)

			else:
				valid = True
				if aux not in self.delimitadores:
					token += aux
					valid = self.aut.doTrans(aux)
				if not valid:
					return ('ERRO', self.linha_atual, self.col_atual)

				self.col_atual += 1

			#Fim da linha
			if self.col_atual == len(self.arq[self.linha_atual])-1:
				self.linha_atual += 1
				self.col_atual = 0
				if self.linha_atual == len(self.arq):
					return 'EOF'

			
		return token


