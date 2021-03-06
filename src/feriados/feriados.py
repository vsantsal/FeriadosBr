from datetime import date
from datetime import timedelta
from math import floor


class Pascoa:
    
    def __init__(self, ano: int):
        """Classe para calcular o dia da pรกscoa de determinado ano."""
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
        ๐=๐ฆ๐๐๐mod19
        ๐=๐ฆ๐๐๐mod4
        ๐=๐ฆ๐๐๐mod7
        ๐=โ๐ฆ๐๐๐/100โ
        ๐=โ(13+8๐)/25โ
        ๐=โ๐/4โ
        ๐=(15โ๐+๐โ๐)mod30
        ๐=(4+๐โ๐)mod7
        ๐=(19๐+๐)mod30
        ๐=(2๐+4๐+6๐+๐)mod7
        Gregorian Easter is 22+๐+๐ March or ๐+๐โ9 April

        if ๐=29 and ๐=6, replace 26 April with 19 April

        if ๐=28, ๐=6, and (11๐+11)mod30<19, replace 25 April with 18 April
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
        # Pรกscoa do ano
        pascoa = Pascoa(ano).data
        # Ano novo (confraternizaรงรฃo universal)
        self._feriados.add(date(ano, 1, 1))
        # Carnaval
        self._feriados.add(pascoa + timedelta(days=-48))
        self._feriados.add(pascoa + timedelta(days=-47))
        # Paixรฃo de Cristo
        self._feriados.add(pascoa + timedelta(days=-2))
        # Tiradentes
        self._feriados.add(date(ano, 4, 21))
        # Corpus Christi
        self._feriados.add(pascoa + timedelta(days=60))
        # Dia do Trabalho
        self._feriados.add(date(ano, 5, 1))
        # Dia da Independรชncia
        self._feriados.add(date(ano, 9, 7))
        # Nossa Senhora
        self._feriados.add(date(ano, 10, 12))
        # Dia de Finados
        self._feriados.add(date(ano, 11, 2))
        # Proclamaรงรฃo da Repรบblica
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
