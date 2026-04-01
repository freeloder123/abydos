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

"""abydos.tests.distance.test_distance_ncd_paq9a.

This module contains unit tests for abydos.distance.NCDpaq9a
"""


import pytest

from abydos.distance import NCDpaq9a


cmp = NCDpaq9a()


def test_ncd_paq9a_dist():
    """Test abydos.distance.NCDpaq9a.dist."""
    try:
        import paq  # noqa: F401
    except ImportError:  # pragma: no cover
        return

    # Base cases
    assert cmp.dist('', '') == 0.0
    assert cmp.dist('a', '') == 0.2
    assert cmp.dist('', 'a') == 0.2
    assert cmp.dist('abc', '') == 0.42857142857142855
    assert cmp.dist('', 'abc') == 0.42857142857142855
    assert cmp.dist('abc', 'abc') == 0.0
    assert cmp.dist('abcd', 'efgh') == 0.5

    assert cmp.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.5555555556)
    assert cmp.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.5555555556)
    assert cmp.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.5555555556)
    assert cmp.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.5555555556)
    assert cmp.dist('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.6153846154)

def test_ncd_paq9a_sim():
    """Test abydos.distance.NCDpaq9a.sim."""
    try:
        import paq  # noqa: F401
    except ImportError:  # pragma: no cover
        return

    # Base cases
    assert cmp.sim('', '') == 1.0
    assert cmp.sim('a', '') == 0.8
    assert cmp.sim('', 'a') == 0.8
    assert cmp.sim('abc', '') == 0.5714285714285714
    assert cmp.sim('', 'abc') == 0.5714285714285714
    assert cmp.sim('abc', 'abc') == 1.0
    assert cmp.sim('abcd', 'efgh') == 0.5

    assert cmp.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.4444444444)
    assert cmp.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.4444444444)
    assert cmp.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.4444444444)
    assert cmp.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.4444444444)
    assert cmp.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.3846153846)
