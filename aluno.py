import gestor_csv as csv
import shutil

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

	def salvar_em_csv(self, nome_arquivo_csv="alunos.csv"):
		if (self.ativo):
			status = "Ativo"
		else:
			status = "Inativo"
		if (self.uffmail is None):
			uffmail = ""
		else:
			uffmail = self.uffmail
		aluno = {"nome": self.nome, "matricula": self.matricula, "telefone": self.telefone, "email": self.email, "uffmail": uffmail, "status": status}
		campos = ["nome", "matricula", "telefone", "email", "uffmail", "status"]
		csv.salvar_linha(aluno, "matricula", campos, nome_arquivo_csv)

	@staticmethod
	def matricula_para_aluno(matricula, nome_arquivo_csv="alunos.csv"):
		try:
			aluno_dict = csv.get_linha(matricula, "matricula", nome_arquivo_csv)
			return Aluno(aluno_dict["nome"], aluno_dict["matricula"], aluno_dict["telefone"], aluno_dict["email"], aluno_dict["uffmail"], aluno_dict["status"])
		except ValueError:
			print("Matricula", matricula, "não encontrada.")