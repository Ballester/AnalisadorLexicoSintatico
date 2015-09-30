class Automato(object):

	def __init__(self):
		self.atual = ''
		self.estados = []
		self.finais  = []
		self.trans   = []

	#Retorna verdadeiro se conseguiu inserir
	def insereEstado(self, nome, final=False):
		self.estados.append(nome)
		if final == True:
			self.finais.append(nome)

		return True

	#Retorna verdadeiro se conseguiu inserir
	def insereTrans(self, est1, est2, simbolo):
		if est1 in self.estados and est2 in self.estados:
			self.trans.append((est1, est2, simbolo))
			return True

		return False

	#Coloca o automato no estado inicial, retorna falso se nao existe
	def setInicial(self, est):
		if est in self.estados:
			self.atual = est
			return True

		return False

	#Retorna o estado o estado de destino caso exista, falso caso contrario
	def hasTrans(self, est, simbolo):
		for trans in self.trans:
			if trans[0] == est and trans[2] == simbolo:
				return trans[1]

		return False

	#Modifica o estado atual do automato, retorna falso se transicao invalida
	def doTrans(self, simbolo):
		self.atual = self.hasTrans(self.atual, simbolo)
		return self.atual

	#Retorna verdadeiro se automato esta em um estado final
	def isFinal(self):
		return self.atual in self.finais

	def printEstados(self):
		print self.estados

	def printFinais(self):
		print self.finais

	def printTrans(self):
		print self.trans

	def printAtual(self):
		print self.atual
