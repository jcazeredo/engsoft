import pandas as pd
import numpy as np

class Horario(object):
	def __init__(self):
		self.__NLINHAS = 7
		self.__LINHAS = ["8h", "10h", "13h", "15h", "17h", "19h", "21h"]
		self.__NCOLUNAS = 5
		self.__COLUNAS = ["Segunda", "Terca", "Quarta", "Quinta", "Sexta"]
		self.__LDIC = {"8":0, "10":1, "13":2, "15":3, "17":4, "19":5, "21":6}
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
		if (valor.dtype == '<U255') and (valor.shape == (self.__NLINHAS, self.__NCOLUNAS)):
			self.__tabela = valor
			return True
		else:
			print ("ERRO: Horario.py - tabela")
			return False

	def elemento(self, linha, coluna, valor):
		# True - certo, False - erro
		lin = self.__LDIC[str(linha)]

		if type(coluna) is int:
			col = coluna
		else:
			try:
				col = self.__CDIC[coluna.lower()]
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