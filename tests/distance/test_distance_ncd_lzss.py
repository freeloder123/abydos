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

"""abydos.tests.distance.test_distance_ncd_lzss.

This module contains unit tests for abydos.distance.NCDlzss
"""


import pytest

from abydos.distance import NCDlzss


cmp = NCDlzss()


def test_ncd_lzss_dist():
    """Test abydos.distance.NCDlzss.dist."""
    try:
        import lzss  # noqa: F401
    except ImportError:  # pragma: no cover
        return

    # Base cases
    assert cmp.dist('', '') == 0.0
    assert cmp.dist('a', '') == 1.0
    assert cmp.dist('', 'a') == 1.0
    assert cmp.dist('abc', '') == 1.0
    assert cmp.dist('', 'abc') == 1.0
    assert cmp.dist('abc', 'abc') == 0.0
    assert cmp.dist('abcd', 'efgh') == 0.8

    assert cmp.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.8333333333)
    assert cmp.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.8333333333)
    assert cmp.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.8333333333)
    assert cmp.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.8333333333)
    assert cmp.dist('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.5)

def test_ncd_lzss_sim():
    """Test abydos.distance.NCDlzss.sim."""
    try:
        import lzss  # noqa: F401
    except ImportError:  # pragma: no cover
        return

    # Base cases
    assert cmp.sim('', '') == 1.0
    assert cmp.sim('a', '') == 0.0
    assert cmp.sim('', 'a') == 0.0
    assert cmp.sim('abc', '') == 0.0
    assert cmp.sim('', 'abc') == 0.0
    assert cmp.sim('abc', 'abc') == 1.0
    assert cmp.sim('abcd', 'efgh') == 0.19999999999999996

    assert cmp.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.1666666667)
    assert cmp.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.1666666667)
    assert cmp.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.1666666667)
    assert cmp.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.1666666667)
    assert cmp.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.5)
