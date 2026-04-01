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

"""abydos.tests.distance.test_distance_strcmp95.

This module contains unit tests for abydos.distance.Strcmp95
"""


import pytest

from abydos.distance import Strcmp95


cmp = Strcmp95()

cmp_ls = Strcmp95(True)


def test_strcmp95_sim():
    """Test abydos.distance.Strcmp95.sim."""
    assert cmp.sim('', '') == 1
    assert cmp.sim('MARTHA', '') == 0
    assert cmp.sim('', 'MARTHA') == 0
    assert cmp.sim('MARTHA', 'MARTHA') == 1

    assert cmp.sim('MARTHA', 'MARHTA') == pytest.approx(abs=1e-7, expected=0.96111111)
    assert cmp.sim('DWAYNE', 'DUANE') == pytest.approx(abs=1e-7, expected=0.873)
    assert cmp.sim('DIXON', 'DICKSONX') == pytest.approx(abs=1e-7, expected=0.839333333)

    assert cmp.sim('ABCD', 'EFGH') == pytest.approx(abs=1e-7, expected=0.0)

    # long_strings = True
    assert cmp_ls.sim('DIXON', 'DICKSONX') == pytest.approx(abs=1e-7, expected=0.85393939)
    assert cmp_ls.sim('DWAYNE', 'DUANE') == pytest.approx(abs=1e-7, expected=0.89609090)
    assert cmp_ls.sim('MARTHA', 'MARHTA') == pytest.approx(abs=1e-7, expected=0.97083333)

    # cover case where we don't boost, etc.
    assert cmp.sim('A', 'ABCDEFGHIJK') == pytest.approx(abs=1e-7, expected=69 / 99)
    assert cmp_ls.sim('A', 'ABCDEFGHIJK') == pytest.approx(abs=1e-7, expected=69 / 99)
    assert cmp.sim('d', 'abcdefgh') == pytest.approx(abs=1e-7, expected=0.708333333)
    assert cmp_ls.sim('d', 'abcdefgh') == pytest.approx(abs=1e-7, expected=0.708333333)
    assert cmp_ls.sim('1', 'abc1efgh') == pytest.approx(abs=1e-7, expected=0.708333333)
    assert cmp_ls.sim('12hundredths', '12hundred') == pytest.approx(abs=1e-7, expected=0.916666667)

def test_strcmp95_dist():
    """Test abydos.distance.Strcmp95.dist."""
    assert cmp.dist('', '') == 0
    assert cmp.dist('MARTHA', '') == 1
    assert cmp.dist('', 'MARTHA') == 1
    assert cmp.dist('MARTHA', 'MARTHA') == 0

    assert cmp.dist('MARTHA', 'MARHTA') == pytest.approx(abs=1e-7, expected=0.03888888)
    assert cmp.dist('DWAYNE', 'DUANE') == pytest.approx(abs=1e-7, expected=0.127)
    assert cmp.dist('DIXON', 'DICKSONX') == pytest.approx(abs=1e-7, expected=0.160666666)

    assert cmp.dist('ABCD', 'EFGH') == pytest.approx(abs=1e-7, expected=1.0)
