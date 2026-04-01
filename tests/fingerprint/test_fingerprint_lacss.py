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

"""abydos.tests.fingerprint.test_fingerprint_lacss.

This module contains unit tests for abydos.fingerprint.LACSS
"""


from abydos.fingerprint import LACSS


fp = LACSS()


def test_lacss_fingerprint():
    """Test abydos.fingerprint.LACSS."""
    # Base case
    assert fp.fingerprint('') == '1732050'

    # Test cases from paper
    assert fp.fingerprint('Williams') == '8312716'
    assert fp.fingerprint('2AB2') == '2449489'
