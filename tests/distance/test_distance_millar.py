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

"""abydos.tests.distance.test_distance_millar.

This module contains unit tests for abydos.distance.Millar
"""


import pytest

from abydos.distance import Millar


cmp = Millar()


def test_millar_dist_abs():
    """Test abydos.distance.Millar.dist_abs."""
    assert cmp.dist_abs('', '') == 0.0
    assert cmp.dist_abs('a', '') == 1.3862943611198906
    assert cmp.dist_abs('', 'a') == 1.3862943611198906
    assert cmp.dist_abs('a', 'a') == 0.0
    assert cmp.dist_abs('abc', '') == 2.772588722239781
    assert cmp.dist_abs('', 'abc') == 2.772588722239781
    assert cmp.dist_abs('abc', 'abc') == 0.0
    assert cmp.dist_abs('abcd', 'efgh') == 6.931471805599453

    assert cmp.dist_abs('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=4.1588830833596715)
    assert cmp.dist_abs('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=4.1588830833596715)
    assert cmp.dist_abs('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=4.1588830833596715)
    assert cmp.dist_abs('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=4.1588830833596715)
    assert cmp.dist_abs('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=4.852030263919617)

def test_millar_dist():
    """Test abydos.distance.Millar.dist."""
    with pytest.raises(NotImplementedError):
        cmp.dist()

def test_millar_sim():
    """Test abydos.distance.Millar.sim."""
    with pytest.raises(NotImplementedError):
        cmp.sim()
