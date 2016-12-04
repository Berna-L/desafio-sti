import unittest
import gestor_csv
import csv
import os

class TestGestorCsvMethods(unittest.TestCase):

	def setUp(self):
		with open("teste.csv", 'w', newline='') as arquivo_csv_escrita:
			escritor = csv.DictWriter(arquivo_csv_escrita, fieldnames=["cab1", "cab2", "cab3"])
			escritor.writeheader()
			escritor.writerow({"cab1": 1, "cab2": "1", "cab3": "bla"})
			escritor.writerow({"cab1": 2, "cab2": "2", "cab3": "ble"})
			escritor.writerow({"cab1": 3, "cab2": "3", "cab3": "bli"})


	def test_get_linha_existente(self):
		resultado = gestor_csv.get_linha(1, "cab1", "teste.csv")
		oraculo = {"cab1": "1", "cab2": "1", "cab3": "bla"}
		self.assertDictEqual(resultado, oraculo)

	def test_get_linha_inexistente(self):
		with self.assertRaises(ValueError):
			gestor_csv.get_linha("bla", "cab2", "teste.csv")


	def test_salvar_linha_existente(self):
		linha = {"cab1": 4, "cab2": "1", "cab3": "bla"}
		gestor_csv.salvar_linha(linha, "cab2", ["cab1", "cab2", "cab3"], "teste.csv")
		resultado = gestor_csv.get_linha(4, "cab1", "teste.csv")
		oraculo = {"cab1": "4", "cab2": "1", "cab3": "bla"}
		self.assertDictEqual(resultado, oraculo)

	def test_salvar_linha_inexistente(self):
		linha = {"cab1": "4", "cab2": "1", "cab3": "bla"}
		gestor_csv.salvar_linha(linha, "cab1", ["cab1", "cab2", "cab3"], "teste.csv")
		resultado = gestor_csv.get_linha(4, "cab1", "teste.csv")
		oraculo = {"cab1": "4", "cab2": "1", "cab3": "bla"}
		self.assertDictEqual(resultado, oraculo)

	def tearDown(self):
		os.remove("teste.csv")