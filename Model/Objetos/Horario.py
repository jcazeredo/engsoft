import pandas as pd
import numpy as np

class Horario(object):
	__NLINHAS = 16
	__LINHAS = ["7h30", "8h30", "9h30", "10h30", "11h30", "12h30", "13h30", "14h30", "15h30", "16h30", "17h30", "18h30", "19h30", "20h30", "21h30", "22h30"]
	__NCOLUNAS = 5
	__COLUNAS = ["Segunda", "Terca", "Quarta", "Quinta", "Sexta"]
	__LDIC = {"7h30":0, "8h30":1, "9h30":2, "10h30":3, "11h30":4, "12h30":5, "13h30":6, "14h30":7, "15h30":8, "16h30":9, "17h30":10, "18h30":11, "19h30":12, "20h30":13, "21h30":14, "22h30":15}
	__CDIC = {"segunda":0, "terca":1, "quarta":2, "quinta":3, "sexta":4}
	__horario ={}
	__tabela ={}

	def __init__(self):
		self.__tabela = np.empty((__NLINHAS, __NCOLUNAS), dtype="U255")
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
			return False

	#@elemento.setter
	def elemento(self, linha, coluna, valor):
		# True - certo, False - erro
		if type(linha) is int:
			lin = linha
		else:
			try:
				lin = __LDIC[linha]
			except:
				return False

		if type(coluna) is int:
			col = coluna
		else:
			try:
				col = __CDIC[coluna.lower()]
			except:
				return False

		self.__tabela[lin, col] = valor
		return True

	@staticmethod
	def to_csv(path_or_buf):
		# True - certo, False - erro
		try:
			__df = pd.DataFrame(__tabela, index=__LINHAS, columns=__COLUNAS)
			__df.to_csv(path_or_buf)
		except:
			return False
		return True