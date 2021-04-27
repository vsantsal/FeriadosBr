from src.feriados.feriados import FeriadosBr
import pytest


@pytest.fixture
def base_case_feriados():
    ano_inicial = 2001
    ano_final = 2078
    return FeriadosBr(ano_inicial, ano_final)


@pytest.fixture
def nome_arquivo_feriados_anbima():
    return 'feriados_nacionais_anbima.txt'
