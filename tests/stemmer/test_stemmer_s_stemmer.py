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

"""abydos.tests.stemmer.test_stemmer_s_stemmer.

This module contains unit tests for abydos.stemmer.SStemmer
"""


from abydos.stemmer import SStemmer


stmr = SStemmer()


def test_s_stemmer():
    """Test abydos.stemmer.SStemmer."""
    # Base case
    assert stmr.stem('') == ''

    # Tests from Harman paper
    assert stmr.stem('panels') == 'panel'
    assert stmr.stem('subjected') == 'subjected'
    assert stmr.stem('aerodynamics') == 'aerodynamic'
    assert stmr.stem('heating') == 'heating'

    # Additional tests to complete coverage
    assert stmr.stem('dairies') == 'dairy'
    assert stmr.stem('census') == 'census'
    assert stmr.stem('boss') == 'boss'
    assert stmr.stem('bosses') == 'bosse'
    assert stmr.stem('raises') == 'raise'
    assert stmr.stem('fees') == 'fee'
    assert stmr.stem('attourneies') == 'attourneie'
    assert stmr.stem('portemonnaies') == 'portemonnaie'
    assert stmr.stem('foes') == 'foe'
    assert stmr.stem('sundaes') == 'sundae'
