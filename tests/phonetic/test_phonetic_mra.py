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

"""abydos.tests.phonetic.test_phonetic_mra.

This module contains unit tests for abydos.phonetic.MRA
"""

from abydos.phonetic import MRA


pa = MRA()

def test_mra():
    """Test abydos.phonetic.MRA."""
    assert pa.encode('') == ''

    # https://en.wikipedia.org/wiki/Match_rating_approach
    assert pa.encode('Byrne') == 'BYRN'
    assert pa.encode('Boern') == 'BRN'
    assert pa.encode('Smith') == 'SMTH'
    assert pa.encode('Smyth') == 'SMYTH'
    assert pa.encode('Catherine') == 'CTHRN'
    assert pa.encode('Kathryn') == 'KTHRYN'

    # length checks
    assert pa.encode('Christopher') == 'CHRPHR'
    assert pa.encode('Dickensianistic') == 'DCKSTC'
    assert pa.encode('Acetylcholinesterase') == 'ACTTRS'
