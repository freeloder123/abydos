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

"""abydos.tests.fingerprint.test_fingerprint_skeleton_key.

This module contains unit tests for abydos.fingerprint.SkeletonKey
"""


from abydos.fingerprint import SkeletonKey


fp = SkeletonKey()


def test_skeleton_key():
    """Test abydos.fingerprint.SkeletonKey."""
    # Base case
    assert fp.fingerprint('') == ''

    # http://dl.acm.org/citation.cfm?id=358048
    assert fp.fingerprint('chemogenic') == 'CHMGNEOI'
    assert fp.fingerprint('chemomagnetic') == 'CHMGNTEOAI'
    assert fp.fingerprint('chemcal') == 'CHMLEA'
    assert fp.fingerprint('chemcial') == 'CHMLEIA'
    assert fp.fingerprint('chemical') == 'CHMLEIA'
    assert fp.fingerprint('chemicial') == 'CHMLEIA'
    assert fp.fingerprint('chimical') == 'CHMLIA'
    assert fp.fingerprint('chemiluminescence') == 'CHMLNSEIU'
    assert fp.fingerprint('chemiluminescent') == 'CHMLNSTEIU'
    assert fp.fingerprint('chemicals') == 'CHMLSEIA'
    assert fp.fingerprint('chemically') == 'CHMLYEIA'
