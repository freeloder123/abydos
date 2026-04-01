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

"""abydos.tests.phonetic.test_phonetic_meta_soundex.

This module contains unit tests for abydos.phonetic.MetaSoundex
"""

from abydos.phonetic import MetaSoundex


pa = MetaSoundex()

pa_en = MetaSoundex(lang='en')

pa_es = MetaSoundex(lang='es')

def test_meta_soundex():
    """Test abydos.phonetic.MetaSoundex."""
    # Base cases
    assert pa.encode('') == '0000'
    assert pa_en.encode('') == '0000'
    assert pa_es.encode('') == ''

    # Top 10 Anglo surnames in US
    assert pa_en.encode('Smith') == '4500'
    assert pa_en.encode('Johnson') == '1525'
    assert pa_en.encode('Williams') == '7452'
    assert pa_en.encode('Brown') == '7650'
    assert pa_en.encode('Jones') == '1520'
    assert pa_en.encode('Miller') == '6460'
    assert pa_en.encode('Davis') == '3120'
    assert pa_en.encode('Wilson') == '7425'
    assert pa_en.encode('Anderson') == '0536'
    assert pa_en.encode('Thomas') == '6200'

    assert pa_es.encode('Smith') == '4632'
    assert pa_es.encode('Johnson') == '82646'
    assert pa_es.encode('Williams') == '564'
    assert pa_es.encode('Brown') == '196'
    assert pa_es.encode('Jones') == '864'
    assert pa_es.encode('Miller') == '659'
    assert pa_es.encode('Davis') == '314'
    assert pa_es.encode('Wilson') == '546'
    assert pa_es.encode('Anderson') == '63946'
    assert pa_es.encode('Thomas') == '364'

    # Top 10 Mexican surnames
    assert pa_en.encode('Hernández') == '5653'
    assert pa_en.encode('García') == '5620'
    assert pa_en.encode('Lòpez') == '8120'
    assert pa_en.encode('Martìnez') == '6635'
    assert pa_en.encode('Rodrìguez') == '9362'
    assert pa_en.encode('González') == '5524'
    assert pa_en.encode('Pérez') == '7620'
    assert pa_en.encode('Sánchez') == '4520'
    assert pa_en.encode('Gómez') == '5520'
    assert pa_en.encode('Flores') == '7462'

    assert pa_es.encode('Hernández') == '96634'
    assert pa_es.encode('García') == '894'
    assert pa_es.encode('Lòpez') == '504'
    assert pa_es.encode('Martìnez') == '69364'
    assert pa_es.encode('Rodrìguez') == '93984'
    assert pa_es.encode('González') == '86454'
    assert pa_es.encode('Pérez') == '094'
    assert pa_es.encode('Sánchez') == '4644'
    assert pa_es.encode('Gómez') == '864'
    assert pa_es.encode('Flores') == '2594'

    # encode_alpha
    assert pa_en.encode_alpha('Smith') == 'SN'
    assert pa_en.encode_alpha('Johnson') == 'JNKN'
    assert pa_es.encode_alpha('Hernández') == 'RNNTS'
    assert pa_es.encode_alpha('García') == 'GRS'
