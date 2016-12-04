import unittest
import gerador_uffmail as gerador
from aluno import Aluno
from comunicador_email import Comunicador_email as cemail


class TestGestorCsvMethods(unittest.TestCase):

	def test_aluno_inativo(self):
		a = Aluno("abc", "abc", "abc", "abc", "", "Inativo")
		with self.assertRaisesRegex(ValueError, "inativo"):
			gerador.verifica_permissao(a)

	def test_aluno_com_uffmail(self):
		a = Aluno("abc", "abc", "abc", "abc", "hello@id.uff.br", "Ativo")
		with self.assertRaisesRegex(ValueError, "possui"):
			gerador.verifica_permissao(a)

	def test_opcoes_esperadas(self):
		a = Aluno("Aa Bb Cc", "abc", "abc", "abc", "", "Ativo")
		resultado = gerador.gerar_opcoes(a)
		sufixo="@id.uff.br"
		oraculo = ["aa_bb" + sufixo, "aabc" + sufixo, "aacc" + sufixo, "acc" + sufixo, "abbcc" + sufixo]
		self.assertListEqual(resultado, oraculo)

	def test_cadastro_ok(self):
		c = cemail("dsadasdsa@gmail.com")
		resultado = gerador.cadastrar_uffmail("1", "1", "o@id.uff.br", c)		
		self.assertEqual(resultado, True)

	def test_cadastro_uffmail_errado(self):
		c = cemail("dsadasdsa@gmail.com")
		with self.assertRaises(ValueError):
			gerador.cadastrar_uffmail("1", "1", "1", c)		

	def test_comunicador_errado(self):
		with self.assertRaises(TypeError):
			gerador.cadastrar_uffmail("1", "1", "1", None)