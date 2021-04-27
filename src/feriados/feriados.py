from datetime import date
from datetime import timedelta
from math import floor


class Pascoa:
    
    def __init__(self, ano: int):
        """Classe para calcular o dia da páscoa de determinado ano."""
        self._ano = ano
        self._valida_ano()

    @property
    def ano(self):
        return self._ano

    @ano.setter
    def ano(self, ano: int):
        if not isinstance(ano, int):
            raise TypeError('{} must be int!'.format(ano))
        self._ano = ano

    @property
    def data(self):
        return self._data_pascoa_pelo_algoritmo_gauss()

    def _valida_ano(self):

        if not isinstance(self._ano, int):
            raise TypeError('{} must be int!'.format(self._ano))

    def _data_pascoa_pelo_algoritmo_gauss(self) -> date:
        """
        𝑎=𝑦𝑒𝑎𝑟mod19
        𝑏=𝑦𝑒𝑎𝑟mod4
        𝑐=𝑦𝑒𝑎𝑟mod7
        𝑘=⌊𝑦𝑒𝑎𝑟/100⌋
        𝑝=⌊(13+8𝑘)/25⌋
        𝑞=⌊𝑘/4⌋
        𝑀=(15−𝑝+𝑘−𝑞)mod30
        𝑁=(4+𝑘−𝑞)mod7
        𝑑=(19𝑎+𝑀)mod30
        𝑒=(2𝑏+4𝑐+6𝑑+𝑁)mod7
        Gregorian Easter is 22+𝑑+𝑒 March or 𝑑+𝑒−9 April

        if 𝑑=29 and 𝑒=6, replace 26 April with 19 April

        if 𝑑=28, 𝑒=6, and (11𝑀+11)mod30<19, replace 25 April with 18 April
        :return:
            date: easter day.
        """
        # Algoritmo de Gauss
        a = self._ano % 19
        b = self._ano % 4
        c = self._ano % 7
        k = floor(self._ano/100)
        p = floor((13+8*k)/25)
        q = floor(k/4)
        m = (15 - p + k - q) % 30
        n = (4 + k - q) % 7
        d = (19*a + m) % 30
        e = (2*b+4*c+6*d+n) % 7
        if (d+e) > 9:
            dia = d + e - 9
            mes = 4
        else:
            dia = 22 + d + e
            mes = 3

        if d == 29 and e == 6:
            dia = 19

        if d == 28 and e == 6 and ((11*m + 11) % 30) < 19:
            dia = 18

        return date(self._ano, mes, dia)


class FeriadosBr:

    def __init__(self, ano_inicial: int, ano_final: int):
        self._ano_inicial = ano_inicial
        self._ano_final = ano_final
        self._check_anos()
        self._feriados = set()
        self._set_feriados()

    @property
    def feriados(self):
        return self._feriados

    @property
    def ano_inicial(self):
        return self._ano_inicial

    @ano_inicial.setter
    def ano_inicial(self, ano: int):
        self._ano_inicial = ano
        self._check_anos()

    @property
    def ano_final(self):
        return self._ano_final

    @ano_final.setter
    def ano_final(self, ano: int):
        self._ano_final = ano
        self._check_anos()

    def eh_dia_util(self, data: date) -> bool:

        self._check_data(data)

        self._set_feriados()

        return data.weekday() < 5 and data not in self._feriados

    def _set_feriados(self):

        ano_aux = self._ano_inicial

        while ano_aux <= self._ano_final:
            self._add_feriados_do_ano(ano_aux)
            ano_aux += 1

    def _add_feriados_do_ano(self, ano: int):
        # Páscoa do ano
        pascoa = Pascoa(ano).data
        # Ano novo (confraternização universal)
        self._feriados.add(date(ano, 1, 1))
        # Carnaval
        self._feriados.add(pascoa + timedelta(days=-48))
        self._feriados.add(pascoa + timedelta(days=-47))
        # Paixão de Cristo
        self._feriados.add(pascoa + timedelta(days=-2))
        # Tiradentes
        self._feriados.add(date(ano, 4, 21))
        # Corpus Christi
        self._feriados.add(pascoa + timedelta(days=60))
        # Dia do Trabalho
        self._feriados.add(date(ano, 5, 1))
        # Dia da Independência
        self._feriados.add(date(ano, 9, 7))
        # Nossa Senhora
        self._feriados.add(date(ano, 10, 12))
        # Dia de Finados
        self._feriados.add(date(ano, 11, 2))
        # Proclamação da República
        self._feriados.add(date(ano, 11, 15))
        # Natal
        self._feriados.add(date(ano, 12, 25))

    def _check_anos(self):
        if not (isinstance(self._ano_inicial, int) and isinstance(self._ano_final, int)):
            raise TypeError('{} and {} must both be int!'.format(self._ano_inicial,
                                                                 self._ano_final))
        if self._ano_inicial > self._ano_final:
            raise ValueError('{} must be less than or equal to {}'.format(self._ano_inicial,

                                                                          self._ano_final))

    def _check_data(self, data: date):

        if not isinstance(data, date):
            raise TypeError('{} must be date!'.format(data))

        if data.year < self._ano_inicial or data.year > self._ano_final:
            raise ValueError('{} must be between {} and {}'.
                             format(data,
                                    self._ano_inicial,
                                    self._ano_final))
