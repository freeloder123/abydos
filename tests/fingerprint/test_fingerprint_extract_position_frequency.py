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

"""abydos.tests.fingerprint.test_fingerprint_extract_position_frequence.

This module contains unit tests for abydos.fingerprint.ExtractPositionFrequency
"""


from abydos.fingerprint import ExtractPositionFrequency


fp = ExtractPositionFrequency()


def test_extract_position_frequence_fingerprint():
    """Test abydos.fingerprint.ExtractPositionFrequency."""
    # Base case
    assert fp.fingerprint('') == ''

    # Test cases from paper
    assert fp.fingerprint('Wilkinson') == 'WKON'
