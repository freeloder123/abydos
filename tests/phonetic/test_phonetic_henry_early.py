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

"""abydos.tests.phonetic.test_phonetic_henry_early.

This module contains unit tests for abydos.phonetic.HenryEarly
"""

from abydos.phonetic import HenryEarly


pa = HenryEarly()

def test_henry_early():
    """Test abydos.phonetic.HenryEarly."""
    # Base case
    assert pa.encode('') == ''

    # Examples from Legare 1972 paper
    assert pa.encode('Descarry') == 'DKR'
    assert pa.encode('Descaries') == 'DKR'
    assert pa.encode('Campo') == 'KP'
    assert pa.encode('Campot') == 'KP'
    assert pa.encode('Gausselin') == 'GSL'
    assert pa.encode('Gosselin') == 'GSL'
    assert pa.encode('Bergeron') == 'BRJ'
    assert pa.encode('Bergereau') == 'BRJ'
    assert pa.encode('Bosseron') == 'BSR'
    assert pa.encode('Cicire') == 'SSR'
    assert pa.encode('Lechevalier') == 'LCV'
    assert pa.encode('Chevalier') == 'CVL'
    assert pa.encode('Peloy') == 'PL'
    assert pa.encode('Beloy') == 'BL'
    assert pa.encode('Beret') == 'BR'
    assert pa.encode('Benet') == 'BN'
    assert pa.encode('Turcot') == 'TRK'
    assert pa.encode('Turgot') == 'TRG'
    assert pa.encode('Vigier') == 'VJ'
    assert pa.encode('Vigiere') == 'VJR'
    assert pa.encode('Dodin') == 'DD'
    assert pa.encode('Dodelin') == 'DDL'

    # Tests to complete coverage
    assert pa.encode('Anil') == 'ANL'
    assert pa.encode('Emmanuel') == 'AMN'
    assert pa.encode('Ainu') == 'EN'
    assert pa.encode('Oeuf') == 'OF'
    assert pa.encode('Yves') == 'IV'
    assert pa.encode('Yo') == 'I'
    assert pa.encode('Umman') == 'EM'
    assert pa.encode('Omman') == 'OM'
    assert pa.encode('Zoe') == 'S'
    assert pa.encode('Beauchamp') == 'BCP'
    assert pa.encode('Chloe') == 'KL'
    assert pa.encode('Gerard') == 'JRR'
    assert pa.encode('Agnes') == 'ANN'
    assert pa.encode('Pinot') == 'PN'
    assert pa.encode('Philo') == 'FL'
    assert pa.encode('Quisling') == 'GL'
    assert pa.encode('Qualite') == 'KLT'
    assert pa.encode('Sainte-Marie') == 'XMR'
    assert pa.encode('Saint-Jean') == 'XJ'
    assert pa.encode('Ste-Marie') == 'XMR'
    assert pa.encode('St-Jean') == 'XJ'
    assert pa.encode('Cloe') == 'KL'
    assert pa.encode('Ahch-To') == 'AKT'
    assert pa.encode('Zdavros') == 'SDV'
    assert pa.encode('Sdavros') == 'DVR'
    assert pa.encode('Coulomb') == 'KLB'
    assert pa.encode('Calm') == 'K'
    assert pa.encode('Omnia') == 'ON'
    assert pa.encode('Ramps') == 'RPS'
    assert pa.encode('Renault') == 'RN'
    assert pa.encode('Czech') == 'CSK'
    assert pa.encode('Imran') == 'ER'
    assert HenryEarly(max_length=-1).encode('Christopher') == 'KRXF'
