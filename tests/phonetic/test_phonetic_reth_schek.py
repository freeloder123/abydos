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

"""abydos.tests.phonetic.test_phonetic_reth_schek.

This module contains unit tests for abydos.phonetic.RethSchek
"""

from abydos.phonetic import RethSchek


pa = RethSchek()

def test_reth_schek_phonetik():
    """Test abydos.phonetic.RethSchek."""
    # Base cases
    assert pa.encode('') == ''

    # equivalents
    assert pa.encode('Häschen') == pa.encode('Haeschen')
    assert pa.encode('Schloß') == pa.encode('Schloss')
    assert pa.encode('üben') == pa.encode('ueben')
    assert pa.encode('Eichörnchen') == pa.encode('Eichoernchen'
    )

    assert pa.encode('Häschen') == 'HESCHEN'
    assert pa.encode('Eichörnchen') == 'AIGHOERNGHEN'
    assert pa.encode('Hexe') == 'HEXE'
    assert pa.encode('Chemie') == 'GHEMI'
    assert pa.encode('Brille') == 'BRILE'
    assert pa.encode('Brilleille') == 'BRILAILE'
    assert pa.encode('Niveau') == 'NIFEAU'
    assert pa.encode('Korb') == 'GORB'
    assert pa.encode('Heino') == 'HAINO'
    assert pa.encode('Nekka') == 'NEKA'
    assert pa.encode('Aleph') == 'ALEF'
    assert pa.encode('Aleppo') == 'ALEBO'
    assert pa.encode('Endzipfel') == 'ENDZIBFL'
    assert pa.encode('verbrandt') == 'FERBRAND'
    assert pa.encode('Cent') == 'GEND'
    assert pa.encode('addiscendae') == 'ADISGENDE'
    assert pa.encode('kickx') == 'GIGX'
    assert pa.encode('sanctionen') == 'SANGDIONEN'
    assert pa.encode('Kuh') == 'GU'
    assert pa.encode('lecker') == 'LEGR'
    assert pa.encode('rödlich') == 'ROEDLIG'
