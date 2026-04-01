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

"""abydos.tests.distance.test_distance_baulieu_vi.

This module contains unit tests for abydos.distance.BaulieuVI
"""


import pytest

from abydos.distance import BaulieuVI


cmp = BaulieuVI()

cmp_no_d = BaulieuVI(alphabet=0)


def test_baulieu_vi_dist():
    """Test abydos.distance.BaulieuVI.dist."""
    # Base cases
    assert cmp.dist('', '') == 0.0
    assert cmp.dist('a', '') == 0.6666666666666666
    assert cmp.dist('', 'a') == 0.6666666666666666
    assert cmp.dist('abc', '') == 0.8
    assert cmp.dist('', 'abc') == 0.8
    assert cmp.dist('abc', 'abc') == 0.0
    assert cmp.dist('abcd', 'efgh') == 0.9090909090909091

    assert cmp.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.6)
    assert cmp.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.6)
    assert cmp.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.6)
    assert cmp.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.6)
    assert cmp.dist('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.4666666667)

def test_baulieu_vi_sim():
    """Test abydos.distance.BaulieuVI.sim."""
    # Base cases
    assert cmp.sim('', '') == 1.0
    assert cmp.sim('a', '') == 0.33333333333333337
    assert cmp.sim('', 'a') == 0.33333333333333337
    assert cmp.sim('abc', '') == 0.19999999999999996
    assert cmp.sim('', 'abc') == 0.19999999999999996
    assert cmp.sim('abc', 'abc') == 1.0
    assert cmp.sim('abcd', 'efgh') == 0.09090909090909094

    assert cmp.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.4)
    assert cmp.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.4)
    assert cmp.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.4)
    assert cmp.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.4)
    assert cmp.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.5333333333)
