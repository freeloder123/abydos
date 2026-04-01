# Copyright 2018-2020 by Christopher C. Little.
# This file is part of Abydos.
#
# Abydos is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Abydos is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Abydos. If not, see <http://www.gnu.org/licenses/>.

"""abydos.tests.phonetic.test_phonetic_spanish_metaphone.

This module contains unit tests for abydos.phonetic.SpanishMetaphone
"""

from abydos.phonetic import SpanishMetaphone


pa = SpanishMetaphone()

pa_mod = SpanishMetaphone(modified=True)

def test_spanish_metaphone():
    """Test abydos.phonetic.SpanishMetaphone."""
    # Base case
    assert pa.encode('') == ''

    # Examples given in
    # https://github.com/amsqr/Spanish-Metaphone/blob/master/phonetic_algorithms_es.py
    assert pa.encode('X') == 'X'
    assert pa.encode('xplosion') == 'EXPLSN'
    assert pa.encode('escalera') == 'ESKLR'
    assert pa.encode('scalera') == 'ESKLR'
    assert pa.encode('mi') == 'M'
    assert pa.encode('tu') == 'T'
    assert pa.encode('su') == 'S'
    assert pa.encode('te') == 'T'
    assert pa.encode('ochooomiiiillllllll') == 'OXMYY'
    assert pa.encode('complicado') == 'KMPLKD'
    assert pa.encode('ácaro') == 'AKR'
    assert pa.encode('ácido') == 'AZD'
    assert pa.encode('clown') == 'KLUN'
    assert pa.encode('down') == 'DUN'
    assert pa.encode('col') == 'KL'
    assert pa.encode('clon') == 'KLN'
    assert pa.encode('waterpolo') == 'UTRPL'
    assert pa.encode('aquino') == 'AKN'
    assert pa.encode('rebosar') == 'RVSR'
    assert pa.encode('rebozar') == 'RVZR'
    assert pa.encode('grajea') == 'GRJ'
    assert pa.encode('gragea') == 'GRJ'
    assert pa.encode('encima') == 'ENZM'
    assert pa.encode('enzima') == 'ENZM'
    assert pa.encode('alhamar') == 'ALAMR'
    assert pa.encode('abollar') == 'AVYR'
    assert pa.encode('aboyar') == 'AVYR'
    assert pa.encode('huevo') == 'UV'
    assert pa.encode('webo') == 'UV'
    assert pa.encode('macho') == 'MX'
    assert pa.encode('xocolate') == 'XKLT'
    assert pa.encode('chocolate') == 'XKLT'
    assert pa.encode('axioma') == 'AXM'
    assert pa.encode('abedul') == 'AVDL'
    assert pa.encode('a') == 'A'
    assert pa.encode('gengibre') == 'JNJVR'
    assert pa.encode('yema') == 'YM'
    assert pa.encode('wHISKY') == 'UISKY'
    assert pa.encode('google') == 'GGL'
    assert pa.encode('xilófono') == 'XLFN'
    assert pa.encode('web') == 'UV'
    assert pa.encode('guerra') == 'GRR'
    assert pa.encode('pingüino') == 'PNUN'
    assert pa.encode('si') == 'S'
    assert pa.encode('ke') == 'K'
    assert pa.encode('que') == 'K'
    assert pa.encode('tu') == 'T'
    assert pa.encode('gato') == 'GT'
    assert pa.encode('gitano') == 'JTN'
    assert pa.encode('queso') == 'KS'
    assert pa.encode('paquete') == 'PKT'
    assert pa.encode('cuco') == 'KK'
    assert pa.encode('perro') == 'PRR'
    assert pa.encode('pero') == 'PR'
    assert pa.encode('arrebato') == 'ARRVT'
    assert pa.encode('hola') == 'OL'
    assert pa.encode('zapato') == 'ZPT'
    assert pa.encode('españa') == 'ESPNY'
    assert pa.encode('garrulo') == 'GRRL'
    assert pa.encode('expansión') == 'EXPNSN'
    assert pa.encode('membrillo') == 'MMVRY'
    assert pa.encode('jamón') == 'JMN'
    assert pa.encode('risa') == 'RS'
    assert pa.encode('caricia') == 'KRZ'
    assert pa.encode('llaves') == 'YVS'
    assert pa.encode('paella') == 'PY'
    assert pa.encode('cerilla') == 'ZRY'

    # tests from file:///home/chrislit/Downloads/ICTRS_2016_12.pdf
    # including of the modified version of the algorithm
    assert pa.encode('Caricia') == 'KRZ'
    assert pa_mod.encode('Caricia') == 'KRZ'
    assert pa.encode('Llaves') == 'YVS'
    assert pa_mod.encode('Llaves') == 'YVZ'
    assert pa.encode('Paella') == 'PY'
    assert pa_mod.encode('Paella') == 'PY'
    assert pa.encode('Cerilla') == 'ZRY'
    assert pa_mod.encode('Cerilla') == 'ZRY'
    assert pa.encode('Empeorar') == 'EMPRR'
    assert pa_mod.encode('Empeorar') == 'ENPRR'
    assert pa.encode('Embotellar') == 'EMVTYR'
    assert pa_mod.encode('Embotellar') == 'ENVTYR'
    assert pa.encode('Hoy') == 'OY'
    assert pa_mod.encode('Hoy') == 'OY'
    assert pa.encode('Xochimilco') == 'XXMLK'
    assert pa_mod.encode('Xochimilco') == 'XXMLK'
    assert pa.encode('Psiquiatra') == 'PSKTR'
    assert pa_mod.encode('Psiquiatra') == 'ZKTR'
    assert pa.encode('siquiatra') == 'SKTR'
    assert pa_mod.encode('siquiatra') == 'ZKTR'
    assert pa.encode('Obscuro') == 'OVSKR'
    assert pa_mod.encode('Obscuro') == 'OZKR'
    assert pa.encode('Oscuro') == 'OSKR'
    assert pa_mod.encode('Oscuro') == 'OZKR'
    assert pa.encode('Combate') == 'KMVT'
    assert pa_mod.encode('Combate') == 'KNVT'
    assert pa.encode('Convate') == 'KNVT'
    assert pa_mod.encode('Convate') == 'KNVT'
    assert pa.encode('Conbate') == 'KNVT'
    assert pa_mod.encode('Conbate') == 'KNVT'
    assert pa.encode('Comportar') == 'KMPRTR'
    assert pa_mod.encode('Comportar') == 'KNPRTR'
    assert pa.encode('Conportar') == 'KNPRTR'
    assert pa_mod.encode('Conportar') == 'KNPRTR'
    assert pa.encode('Zapato') == 'ZPT'
    assert pa_mod.encode('Zapato') == 'ZPT'
    assert pa.encode('Sapato') == 'SPT'
    assert pa_mod.encode('Sapato') == 'ZPT'
    assert pa.encode('Escalera') == 'ESKLR'
    assert pa_mod.encode('Escalera') == 'EZKLR'
    assert pa.encode('scalera') == 'ESKLR'
    assert pa_mod.encode('scalera') == 'EZKLR'

    # terms from algorithm/source
    assert pa.encode('acción') == 'AXN'
    assert pa.encode('reacción') == 'RXN'
    assert pa.encode('cesar') == 'ZSR'
    assert pa.encode('cien') == 'ZN'
    assert pa.encode('cid') == 'ZD'
    assert pa.encode('conciencia') == 'KNZNZ'
    assert pa.encode('gente') == 'JNT'
    assert pa.encode('ecologia') == 'EKLJ'

    # completing coverage
    assert pa.encode('hola') == 'OL'
    assert pa.encode('aqi') == 'AK'
    assert pa.encode('hjordis') == 'HJRDS'
