import pandas as pd
import numpy as np

class Horario(object):
	def __init__(self):
		self.__NLINHAS = 16
		self.__LINHAS = ["7h30", "8h30", "9h30", "10h30", "11h30", "12h30", "13h30", "14h30", "15h30", "16h30", "17h30", "18h30", "19h30", "20h30", "21h30", "22h30"]
		self.__NCOLUNAS = 5
		self.__COLUNAS = ["Segunda", "Terca", "Quarta", "Quinta", "Sexta"]
		self.__LDIC = {"7h30":0, "8h30":1, "9h30":2, "10h30":3, "11h30":4, "12h30":5, "13h30":6, "14h30":7, "15h30":8, "16h30":9, "17h30":10, "18h30":11, "19h30":12, "20h30":13, "21h30":14, "22h30":15}
		self.__CDIC = {"segunda":0, "terca":1, "quarta":2, "quinta":3, "sexta":4}
		self.__horario ={}
		self.__tabela ={}
		self.__tabela = np.empty((self.__NLINHAS, self.__NCOLUNAS), dtype="U255")
		self.__tabela[:] = "-"

	@property
	def tabela(self):
		return self.__tabela

	@property
	def nlinhas(self):
		return self.__NLINHAS

	@property
	def linhas(self):
		return self.__LINHAS

	@property
	def ncolunas(self):
		return self.__NCOLUNAS

	@property
	def colunas(self):
		return self.__COLUNAS

	@tabela.setter
	def tabela(self, valor):
	# True - certo, False - erro
		if (valor.dtype == '<U255') and (valor.shape == (__NLINHAS, __NCOLUNAS)):
			self.__tabela = valor
			return True
		else:
			print ("ERRO: Horario.py - tabela")
			return False

	def elemento(self, linha, coluna, valor):
		# True - certo, False - erro
		if type(linha) is int:
			lin = linha
		else:
			try:
				lin = __LDIC[linha]
			except:
				print ("ERRO: Horario.py - elemento")
				return False

		if type(coluna) is int:
			col = coluna
		else:
			try:
				col = __CDIC[coluna.lower()]
			except:
				print ("ERRO: Horario.py - elemento")
				return False

		self.__tabela[lin, col] = valor
		return True

	def to_csv(self, path_or_buf):
		# True - certo, False - erro
		try:
			__df = pd.DataFrame(self.__tabela, index=self.__LINHAS, columns=self.__COLUNAS)
			__df.to_csv(path_or_buf)
		except:
			print ("ERRO: Horario.py - to_csv")
			return False
		return True