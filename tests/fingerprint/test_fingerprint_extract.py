# Copyright 2019-2020 by Christopher C. Little.
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

"""abydos.tests.fingerprint.test_fingerprint_extract.

This module contains unit tests for abydos.fingerprint.Extract
"""


from abydos.fingerprint import Extract


fp = Extract()


def test_extract_fingerprint():
    """Test abydos.fingerprint.Extract."""
    # Base case
    assert fp.fingerprint('') == ''

    # Test cases from paper
    assert fp.fingerprint('Johnson') == 'JHNS'

    assert Extract(letter_list=2).fingerprint('Johnson') == 'JHNN'
    assert (
        Extract(letter_list='ETASIONRHCDLPMFBUWGYKVJQZX').fingerprint( 'Johnson' )
        == 'JHNN'
    )
    assert Extract(letter_list=0).fingerprint('Johnson') == 'JHNS'
