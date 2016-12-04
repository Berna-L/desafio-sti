import abc

class Comunicador(object):

	__metaclass__ = abc.ABCMeta

	@abc.abstractmethod
	def enviar_mensagem(self, nome, uffmail, senha):
		"""Envia a mensagem ao usuário."""
		return