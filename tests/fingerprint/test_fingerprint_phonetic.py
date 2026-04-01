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

"""abydos.tests.fingerprint.test_fingerprint_phonetic_fingerprint.

This module contains unit tests for abydos.fingerprint.Phonetic
"""


from abydos.fingerprint import Phonetic
from abydos.phonetic import Phonet, Soundex


from .. import NIALL


fp = Phonetic()

fp_phonet = Phonetic(Phonet())

fp_soundex = Phonetic(Soundex())

soundex = Soundex()


def test_phonetic_fingerprint():
    """Test abydos.fingerprint.Phonetic."""
    # Base case
    assert fp.fingerprint('') == ''

    assert fp.fingerprint(' '.join(NIALL)) == 'a anl mknl njl nklk nl'
    assert (
        fp_phonet.fingerprint(' '.join(NIALL))
        == 'knile makneil maknele neil nel nele nial nigeli ' + 'nigl nil noigialach oneil ui'
    )
    assert (
        fp_soundex.fingerprint(' '.join(NIALL))
        == 'k540 m254 n240 n242 n400 o540 u000'
    )
