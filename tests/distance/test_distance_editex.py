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

"""abydos.tests.distance.test_distance_editex.

This module contains unit tests for abydos.distance.Editex
"""


import pytest

from abydos.distance import Editex


cmp = Editex()

cmp_local = Editex(local=True)

cmp_taper = Editex(taper=True)


def test_editex_dist_abs():
    """Test abydos.distance.Editex.dist_abs."""
    assert cmp.dist_abs('', '') == 0
    assert cmp.dist_abs('nelson', '') == 12
    assert cmp.dist_abs('', 'neilsen') == 14
    assert cmp.dist_abs('ab', 'a') == 2
    assert cmp.dist_abs('ab', 'c') == 4
    assert cmp.dist_abs('nelson', 'neilsen') == 2
    assert cmp.dist_abs('neilsen', 'nelson') == 2
    assert cmp.dist_abs('niall', 'neal') == 1
    assert cmp.dist_abs('neal', 'niall') == 1
    assert cmp.dist_abs('niall', 'nihal') == 2
    assert cmp.dist_abs('nihal', 'niall') == 2
    assert cmp.dist_abs('neal', 'nihl') == 3
    assert cmp.dist_abs('nihl', 'neal') == 3

    # Test tapering variant
    assert cmp_taper.dist_abs('nelson', 'neilsen') == pytest.approx(abs=1e-7, expected=2.7142857143)

def test_editex_dist_abs_local():
    """Test abydos.distance.Editex.dist_abs (local variant)."""
    assert cmp_local.dist_abs('', '') == 0
    assert cmp_local.dist_abs('nelson', '') == 12
    assert cmp_local.dist_abs('', 'neilsen') == 14
    assert cmp_local.dist_abs('ab', 'a') == 2
    assert cmp_local.dist_abs('ab', 'c') == 2
    assert cmp_local.dist_abs('nelson', 'neilsen') == 2
    assert cmp_local.dist_abs('neilsen', 'nelson') == 2
    assert cmp_local.dist_abs('niall', 'neal') == 1
    assert cmp_local.dist_abs('neal', 'niall') == 1
    assert cmp_local.dist_abs('niall', 'nihal') == 2
    assert cmp_local.dist_abs('nihal', 'niall') == 2
    assert cmp_local.dist_abs('neal', 'nihl') == 3
    assert cmp_local.dist_abs('nihl', 'neal') == 3

def test_editex_sim():
    """Test abydos.distance.Editex.sim."""
    assert cmp.sim('', '') == 1
    assert cmp.sim('nelson', '') == 0
    assert cmp.sim('', 'neilsen') == 0
    assert cmp.sim('ab', 'a') == 0.5
    assert cmp.sim('ab', 'c') == 0
    assert cmp.sim('nelson', 'neilsen') == pytest.approx(abs=1e-7, expected=12 / 14)
    assert cmp.sim('neilsen', 'nelson') == pytest.approx(abs=1e-7, expected=12 / 14)
    assert cmp.sim('niall', 'neal') == 0.9

def test_editex_dist():
    """Test abydos.distance.Editex.dist."""
    assert cmp.dist('', '') == 0
    assert cmp.dist('nelson', '') == 1
    assert cmp.dist('', 'neilsen') == 1
    assert cmp.dist('ab', 'a') == 0.5
    assert cmp.dist('ab', 'c') == 1
    assert cmp.dist('nelson', 'neilsen') == pytest.approx(abs=1e-7, expected=2 / 14)
    assert cmp.dist('neilsen', 'nelson') == pytest.approx(abs=1e-7, expected=2 / 14)
    assert cmp.dist('niall', 'neal') == 0.1

    # Test tapering variant
    assert cmp_taper.dist('nelson', 'neilsen') == pytest.approx(abs=1e-7, expected=0.123376623)
