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

"""abydos.tests.stemmer.test_stemmer_clef_german.

This module contains unit tests for abydos.stemmer.CLEFGerman
"""


from abydos.stemmer import CLEFGerman


stmr = CLEFGerman()


def test_clef_german():
    """Test abydos.stemmer.CLEFGerman."""
    # base case
    assert stmr.stem('') == ''

    # len <= 2
    assert stmr.stem('ä') == 'a'
    assert stmr.stem('er') == 'er'
    assert stmr.stem('es') == 'es'
    assert stmr.stem('äh') == 'ah'

    # len > 2
    assert stmr.stem('deinen') == 'dein'
    assert stmr.stem('können') == 'konn'
    assert stmr.stem('Damen') == 'dame'
    assert stmr.stem('kleines') == 'klein'
    assert stmr.stem('Namen') == 'name'
    assert stmr.stem('Äpfel') == 'apfel'
    assert stmr.stem('Jahre') == 'jahr'
    assert stmr.stem('Mannes') == 'mann'
    assert stmr.stem('Häuser') == 'haus'
    assert stmr.stem('Motoren') == 'motor'
    assert stmr.stem('kleine') == 'klein'
    assert stmr.stem('Pfingsten') == 'pfingst'
    assert stmr.stem('lautest') == 'lautest'
    assert stmr.stem('lauteste') == 'lautest'
    assert stmr.stem('lautere') == 'lauter'
    assert stmr.stem('lautste') == 'lautst'
    assert stmr.stem('kleinen') == 'klei'
