from lexico import Lexico
#teste
class Sintatico(object):
	
	def __init__(self, file):
		self.lex = Lexico(file)
		self.tk = ''

	def insereEstado(self, est, final=False):
		self.lex.insereEstado(est, final)

	def insereTrans(self, est1, est2, simbolo):
		self.lex.insereTrans(est1, est2, simbolo)

	def setInicial(self, est):
		self.lex.setInicial(est)

	def insereDelimitador(self, dele):
		self.lex.delimitadores.append(dele)

	def insereReservada(self, res):
		self.lex.reservadas.append(res)

	def le_token(self):
		self.tk = self.lex.scanner()
		return self.tk


	def PROG(self):
		le_token()

		if LISTACMD():
			if self.tk == "EOF":
				return True

	def LISTACMD(self):
		if CMD():
			if self.tk == "ENDL":
				le_token()
				if LISTACMD():
					return True

		else:
			return True

	def CMD(self):
		if DEC():
			return True

		elif ATRIB():
			return True

		elif COND():
			return True

		elif ESC():
			return True

		elif LEI():
			return True

		else:
			return 'ERRO - Sintatico'


	def DEC(self):
		if DECl():
			le_token()
			if LVAR():
				return True
			else:
				return False
		else:
			return False

	def DECl(self):
		if self.tk == 'local':
			le_token()
			return True
		else:
			return True

	# def ID(self):
	# 	if self.tk == 'ari':
	# 		self.tk = le_token()
	# 		return True
	# 	elif self.tk == 'bool':
	# 		self.tk = le_token()
	# 		return True
	# 	else:
	# 		return False

	def LVAR(self):
		if self.tk == 'var':
			le_token()
			


	








	





