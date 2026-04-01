# Copyright 2014-2020 by Christopher C. Little.
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

"""abydos.tests.phonetic.test_phonetic_metaphone.

This module contains unit tests for abydos.phonetic.Metaphone
"""

import pytest

from abydos.phonetic import Metaphone


pa = Metaphone()

pa4 = Metaphone(4)

def test_metaphone():
    """Test abydos.phonetic.Metaphone."""
    assert pa.encode('') == ''
    assert pa.encode('...') == ''

    # http://ntz-develop.blogspot.com/2011/03/phonetic-algorithms.html
    assert pa4.encode('Fishpool') == 'FXPL'
    assert pa4.encode('Fishpoole') == 'FXPL'
    assert pa4.encode('Gellately') == 'JLTL'
    assert pa4.encode('Gelletly') == 'JLTL'
    assert pa4.encode('Lowers') == 'LWRS'
    assert pa4.encode('Lowerson') == 'LWRS'
    assert pa4.encode('Mallabar') == 'MLBR'
    assert pa4.encode('Melbert') == 'MLBR'
    assert pa4.encode('Melbourn') == 'MLBR'
    assert pa4.encode('Melbourne') == 'MLBR'
    assert pa4.encode('Melburg') == 'MLBR'
    assert pa4.encode('Melbury') == 'MLBR'
    assert pa4.encode('Milberry') == 'MLBR'
    assert pa4.encode('Milborn') == 'MLBR'
    assert pa4.encode('Milbourn') == 'MLBR'
    assert pa4.encode('Milbourne') == 'MLBR'
    assert pa4.encode('Milburn') == 'MLBR'
    assert pa4.encode('Milburne') == 'MLBR'
    assert pa4.encode('Millberg') == 'MLBR'
    assert pa4.encode('Mulberry') == 'MLBR'
    assert pa4.encode('Mulbery') == 'MLBR'
    assert pa4.encode('Mulbry') == 'MLBR'
    assert pa4.encode('Saipy') == 'SP'
    assert pa4.encode('Sapey') == 'SP'
    assert pa4.encode('Sapp') == 'SP'
    assert pa4.encode('Sappy') == 'SP'
    assert pa4.encode('Sepey') == 'SP'
    assert pa4.encode('Seppey') == 'SP'
    assert pa4.encode('Sopp') == 'SP'
    assert pa4.encode('Zoppie') == 'SP'
    assert pa4.encode('Zoppo') == 'SP'
    assert pa4.encode('Zupa') == 'SP'
    assert pa4.encode('Zupo') == 'SP'
    assert pa4.encode('Zuppa') == 'SP'

    # assorted tests to complete code coverage
    assert pa.encode('Xavier') == 'SFR'
    assert pa.encode('Acacia') == 'AKX'
    assert pa.encode('Schuler') == 'SKLR'
    assert pa.encode('Sign') == 'SN'
    assert pa.encode('Signed') == 'SNT'
    assert pa.encode('Horatio') == 'HRX'
    assert pa.encode('Ignatio') == 'IKNX'
    assert pa.encode('Lucretia') == 'LKRX'
    assert pa.encode('Wright') == 'RKT'
    assert pa.encode('White') == 'WT'
    assert pa.encode('Black') == 'BLK'
    assert pa.encode('Chance') == 'XNS'
    assert pa.encode('Dgengo') == 'JJNK'
    assert pa.encode('Ghost') == 'ST'
    assert pa.encode('Qing') == 'KNK'
    assert pa.encode('Asia') == 'AX'
    assert pa.encode('Ax') == 'AKS'
    assert pa.encode('Thegn') == '0N'
    assert pa.encode('acknowledged') == 'AKNLJT'
    assert pa.encode('awkward') == 'AKWRT'
    assert pa.encode('admitted') == 'ATMTT'
    assert pa.encode('dahl') == 'TL'
    assert pa.encode('autobiography') == 'ATBKRF'
    assert pa.encode('exaggerate') == 'EKSKRT'
    assert pa.encode('pitch') == 'PX'
    assert pa.encode('chracter') == 'KRKTR'

    # assorted tests to complete branch coverage
    assert pa.encode('Lamb') == 'LM'
    assert pa.encode('science') == 'SNS'

    # max_length bounds tests
    assert Metaphone(max_length=-1).encode('Niall') == 'NL'
    assert Metaphone(max_length=0).encode('Niall') == 'NL'


def test_metaphone_validation():
    """Test input validation for Metaphone."""
    pa = Metaphone()
    with pytest.raises(TypeError):
        pa.encode(42)
    with pytest.raises(TypeError):
        pa.encode(None)
    with pytest.raises(TypeError):
        Metaphone(max_length='10')
