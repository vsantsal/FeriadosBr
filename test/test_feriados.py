from datetime import date
from datetime import datetime
from decimal import Decimal
from src.feriados import FeriadosBr
from src.feriados import Pascoa
import pytest


##
# Testes da classe Pascoa
##
def test_data_pascoa_errada_algoritmo_gauss_original():
    pascoa = Pascoa(4200).data
    assert pascoa == date(4200, 4, 20)


@pytest.mark.parametrize("ano",
                         [
                             '2079',  # str só com dígitos
                             'abc',  # str só letras
                             {2079},  # conjunto
                             [2019, 2020],  # lista
                             2080.0,  # float
                             Decimal('3000'),  # decimal
                         ])
def test_pascoa_ano_not_int_raises_type_error(ano: int):
    with pytest.raises(TypeError):
        Pascoa(ano)


@pytest.mark.parametrize("ano, data_pascoa",
                         [
                             (2021, date(2021, 4, 4)),
                             (2022, date(2022, 4, 17)),
                             (2023, date(2023, 4, 9)),
                             (2024, date(2024, 3, 31)),
                             (2025, date(2025, 4, 20)),
                             (2026, date(2026, 4, 5)),
                             (2027, date(2027, 3, 28)),
                             (2028, date(2028, 4, 16)),
                             (2029, date(2029, 4, 1)),
                             (2030, date(2030, 4, 21)),
                             (2031, date(2031, 4, 13)),
                             (2032, date(2032, 3, 28)),
                             (2033, date(2033, 4, 17)),
                             (2034, date(2034, 4, 9)),
                             (2035, date(2035, 3, 25)),
                             (2036, date(2036, 4, 13)),
                             (2037, date(2037, 4, 5)),
                             (2038, date(2038, 4, 25)),
                             (2039, date(2039, 4, 10)),
                             (2040, date(2040, 4, 1)),
                             (2041, date(2041, 4, 21)),
                             (2042, date(2042, 4, 6)),
                             (2043, date(2043, 3, 29)),
                             (2044, date(2044, 4, 17)),
                             (2045, date(2045, 4, 9)),
                             (2046, date(2046, 3, 25)),
                             (2047, date(2047, 4, 14)),
                             (2048, date(2048, 4, 5)),
                             (2049, date(2049, 4, 18)),
                             (2050, date(2050, 4, 10)),
                             (2051, date(2051, 4, 2)),
                         ])
def test_datas_pascoa_proximos_anos(ano, data_pascoa):
    """Testes de datas de páscoa no calendário gregoriano para os próximos anos.
    Fonte: https://tlarsen2.tripod.com/thomaslarsen/easterdates.html
    """
    pascoa = Pascoa(ano).data
    assert pascoa == data_pascoa


@pytest.mark.parametrize("ano, resultado",
                         [(4200, 4200),
                          (2021, 2021),
                          (3000, 3000),
                          (1998, 1998)])
def test_pascoa_ano_getter(ano, resultado):
    pascoa = Pascoa(ano)
    assert pascoa.ano == resultado


def test_pascoa_ano_setter():
    pascoa = Pascoa(4200)
    assert pascoa.ano == 4200
    assert pascoa.data == date(4200, 4, 20)
    pascoa.ano = 2021
    assert pascoa.ano == 2021
    assert pascoa.data == date(2021, 4, 4)


##
# Testes da classe FeriadosBr
##
# referências para os cenários abaixo:
# https://www.anbima.com.br/feriados/feriados.asp
# caso base vai de 2018 a 2078
@pytest.mark.parametrize("data, resultado",
                         [
                             (date(2021, 1, 1), False),  # Ano novo
                             (date(2023, 1, 11), True),  # Dia útil de janeiro em 2023
                             (date(2078, 2, 14), False),  # segunda-feira de carnaval em 2078 (fev)
                             (date(2020, 2, 5), True),  # Dia útil de fevereiro de 2020
                             (date(2052, 3, 5), False),  # terça-feira de carnaval em 2052 (mar)
                             (date(2024, 3, 18), True),  # dia útil de março de 2024
                             (date(2021, 4, 21), False),  # Tiradentes 2021
                             (date(2019, 4, 23), True),  # Dia útil de abril de 2019 (Feriado local)
                             (date(2024, 3, 29), False),  # Paixão de Cristo em 2024 (março)
                             (date(2033, 4, 15), False),  # Paixão de Cristo em 2033 (abril)
                             (date(2022, 5, 1), False),  # Dia do trabalho em 2022
                             (date(2022, 5, 25), True),  # Dia útil de maio de 2022
                             (date(2024, 5, 30), False),  # Corpus christi em 2024 (maio)
                             (date(2031, 6, 12), False),  # Corpus christi em 2031 (junho)
                             (date(2021, 6, 21), True),  # Dia útil de junho de 2021
                             (date(2018, 7, 4), True),  # Dia útil de julho de 2018
                             (date(2021, 9, 7), False),  # Dia da independência de 2021
                             (date(2053, 10, 12), False),  # Dia de Nossa Senhora de 2053
                             (date(2020, 11, 15), False),  # Proclamação da República
                             (date(2022, 12, 25), False),  # Natal
                             (date(2021, 12, 31), True),  # último dia do ano - dia útil
                             (date(2022, 12, 31), False),  # último dia do ano - sábado
                         ])
def test_eh_dia_util_feriado_br(data: date, resultado: bool, base_case_feriados: FeriadosBr):
    flag = base_case_feriados.eh_dia_util(data)
    assert flag == resultado


@pytest.mark.parametrize("ano, resultado",
                         [
                             (2019, 2019),
                             (2020, 2020),
                             (2021, 2021),
                             (2022, 2022),
                             (2078, 2078),
                         ])
def test_altera_ano_inicial_menor_igual_ano_final_ok(ano: int,
                                                     resultado: int,
                                                     base_case_feriados: FeriadosBr):
    base_case_feriados.ano_inicial = ano
    assert base_case_feriados.ano_inicial == resultado


@pytest.mark.parametrize("ano, resultado",
                         [
                             (2077, 2077),
                             (2068, 2068),
                             (2055, 2055),
                             (2040, 2040),
                             (2001, 2001),
                         ])
def test_altera_ano_final_maior_igual_ano_inicial_ok(ano: int,
                                                     resultado: int,
                                                     base_case_feriados: FeriadosBr):
    base_case_feriados.ano_final = ano
    assert base_case_feriados.ano_final == resultado


@pytest.mark.parametrize("ano_inicial",
                         [
                             2079,
                             2080,
                             3000,
                         ])
def test_altera_ano_inicial_gt_ano_final_raises_value_error(ano_inicial: int,
                                                            base_case_feriados: FeriadosBr):
    with pytest.raises(ValueError):
        base_case_feriados.ano_inicial = ano_inicial


@pytest.mark.parametrize("ano_final",
                         [
                             2000,
                             1999,
                             1998,
                         ])
def test_altera_ano_final_lt_ano_inicial_raises_value_error(ano_final: int,
                                                            base_case_feriados: FeriadosBr):
    with pytest.raises(ValueError):
        base_case_feriados.ano_final = ano_final


@pytest.mark.parametrize("ano_inicial",
                         [
                             '2079',  # str só com dígitos
                             'abc',  # str só letras
                             {2079},  # conjunto
                             [2019, 2020],  # lista
                             2080.0,  # float
                             Decimal('3000'),  # decimal
                         ])
def test_altera_ano_inicial_not_int_raises_type_error(ano_inicial: int,
                                                      base_case_feriados: FeriadosBr):
    with pytest.raises(TypeError):
        base_case_feriados.ano_inicial = ano_inicial


@pytest.mark.parametrize("ano_final",
                         [
                             '2079',  # str só com dígitos
                             'abc',  # str só letras
                             {2079},  # conjunto
                             [2019, 2020],  # lista
                             float(2080.1),  # float
                             Decimal('3000.005'),  # decimal
                         ])
def test_altera_ano_final_not_int_raises_type_error(ano_final: int,
                                                    base_case_feriados: FeriadosBr):
    with pytest.raises(TypeError):
        base_case_feriados.ano_final = ano_final


@pytest.mark.parametrize("data",
                         [
                             '2079',  # str só com dígitos
                             'abc',  # str só letras
                             {2079},  # conjunto
                             [2019, 2020],  # lista
                             2080.0,  # float
                             Decimal('3000'),  # decimal
                         ])
def test_eh_dia_util_not_date_raises_type_error(data: date,
                                                base_case_feriados: FeriadosBr):
    with pytest.raises(TypeError):
        base_case_feriados.eh_dia_util(data)


@pytest.mark.parametrize("data",
                         [
                             date(2000, 12, 31),
                             date(1999, 5, 10),
                             date(1998, 3, 7),
                             date(2079, 1, 1),
                             date(2080, 4, 17),
                             date(2081, 6, 12),
                         ])
def test_eh_dia_util_out_of_range_raises_type_error(data: date,
                                                    base_case_feriados: FeriadosBr):
    with pytest.raises(ValueError):
        base_case_feriados.eh_dia_util(data)


def test_datas_planilha_anbima_sao_feriados(base_case_feriados: FeriadosBr,
                                            nome_arquivo_feriados_anbima: str):
    with open(nome_arquivo_feriados_anbima, 'r') as f:
        for line in f:
            try:
                data = datetime.strptime(line.strip('\n'), '%d/%m/%Y').date()
            except ValueError:
                assert 1 == 1
            else:
                assert not base_case_feriados.eh_dia_util(data)
