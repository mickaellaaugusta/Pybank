from pybank_ref import caixa_eletronico, valida_saque

def test_valida_saque_invalido():
	assert valida_saque(-1) is False

def test_valida_saque_valido():
	assert valida_saque(80) is True
