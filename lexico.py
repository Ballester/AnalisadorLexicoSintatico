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
		self.aut.resetInicial()
		token = ''
		if self.linha_atual == len(self.arq):
			return 'EOF'
		for i in range(self.col_atual, len(self.arq[self.linha_atual])):
			aux = self.arq[self.linha_atual][self.col_atual]
			if (aux in self.delimitadores and token != '') or (aux == '\n'):
				if self.aut.isFinal():
					if aux == '\n':
						self.linha_atual += 1
						self.col_atual = 0

					if token in self.reservadas:
						return (token, "reservada")
					else:						
						return (token, self.aut.returnAtual())

				else:
					return ('ERRO - Identificador Invalido', self.linha_atual, self.col_atual)

			else:
				valid = True
				if aux not in self.delimitadores:
					valid = self.aut.hasTrans(self.aut.returnAtual(), aux)
					if valid:
						token += aux
						self.aut.doTrans(aux)

					if not valid:
						if self.aut.isFinal():
							if token in self.reservadas:
								return (token, "reservada")
							else:
								return (token, self.aut.returnAtual())
						else:
							return ('ERRO - Transicao Invalida', self.linha_atual, self.col_atual)

				self.col_atual += 1

		#Entra somente no fim do arquivo
		self.linha_atual += 1
		if self.aut.isFinal():
			if token in self.reservadas:
				return (token, "reservada")
			else:
				return (token, self.aut.returnAtual())
		else:
			return ('ERRO - Identificador Invalido', self.linha_atual, self.col_atual)



