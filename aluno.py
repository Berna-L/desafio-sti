import gestor_csv as csv

class Aluno:

	def __init__(self, nome, matricula, telefone, email, uffmail, status):
		self.nome = nome
		self.matricula = matricula
		self.telefone = telefone
		self.email = email
		if ("@" not in uffmail):
			self.uffmail = None
		else:
			self.uffmail = uffmail
		if (status == "Ativo"):
			self.ativo = True
		else:
			self.ativo = False

	@staticmethod
	def matricula_para_aluno(matricula, nome_arquivo_csv="alunos.csv"):
		alunos_csv = csv.csv_para_lista(arquivo_csv)
		for linha in leitor:
			if (str(matricula) == linha["matricula"]):
				return Aluno(linha["nome"], linha["matricula"], linha["telefone"], linha["email"], linha["uffmail"], linha["status"])
		raise ValueError("Matrícula " + str(matricula) + " não encontrada")