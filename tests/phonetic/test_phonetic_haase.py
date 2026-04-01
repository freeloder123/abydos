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

"""abydos.tests.phonetic.test_phonetic_haase.

This module contains unit tests for abydos.phonetic.Haase
"""

from abydos.phonetic import Haase


pa = Haase()

def test_haase_phonetik():
    """Test abydos.phonetic.Haase."""
    # Base cases
    assert pa.encode('') == ''

    # equivalents
    assert pa.encode('Häschen') == pa.encode('Haeschen')
    assert pa.encode('Schloß') == pa.encode('Schloss')
    assert pa.encode('üben') == pa.encode('ueben')
    assert pa.encode('Eichörnchen') == pa.encode('Eichoernchen'
    )

    # coverage completion
    assert pa.encode('Häschen') == '9896,9496'
    assert Haase(primary_only=True).encode('Häschen') == '9896'
    assert pa.encode('Eichörnchen') == '94976496'
    assert pa.encode('Hexe') == '9489'
    assert pa.encode('Chemie') == '4969,8969'

    assert pa.encode('Brille') == '17959,179'
    assert pa.encode('Brilleille') == '1795959,17959,179'
    assert pa.encode('Niveau') == '6939'
    assert pa.encode('Korb') == '4971,4973'
    assert pa.encode('Heino') == '969,9693'
    assert pa.encode('Nekka') == '6949,69497'
    assert pa.encode('Aleph') == '9593'
    assert pa.encode('Aleppo') == '95919,959193'
    assert pa.encode('Endzipfel') == '96891395'
    assert pa.encode('verbrandt') == '39717962,39737962'
    assert pa.encode('Cent') == '8962'
    assert pa.encode('addiscendae') == '92989629'
    assert pa.encode('kickx') == '4948'
    assert pa.encode('sanctionen') == '896829696'

    # encode_alpha
    assert pa.encode_alpha('Niveau') == 'NAFA'
    assert pa.encode_alpha('Korb') == 'KARP,KARF'
    assert pa.encode_alpha('Heino') == 'ANA,ANAF'
    assert pa.encode_alpha('Nekka') == 'NAKA,NAKAR'
