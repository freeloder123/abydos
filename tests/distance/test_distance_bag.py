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

"""abydos.tests.distance.test_distance_bag.

This module contains unit tests for abydos.distance.Bag
"""


import pytest

from abydos.distance import Bag
from abydos.tokenizer import SAPSTokenizer


cmp = Bag()


def test_bag_dist_abs():
    """Test abydos.distance.Bag.dist_abs."""
    assert cmp.dist_abs('', '') == 0
    assert cmp.dist_abs('nelson', '') == 6
    assert cmp.dist_abs('', 'neilsen') == 7
    assert cmp.dist_abs('ab', 'a') == 1
    assert cmp.dist_abs('ab', 'c') == 2
    assert cmp.dist_abs('nelson', 'neilsen') == 2
    assert cmp.dist_abs('neilsen', 'nelson') == 2
    assert cmp.dist_abs('niall', 'neal') == 2
    assert cmp.dist_abs('aluminum', 'Catalan') == 5
    assert cmp.dist_abs('abcdefg', 'hijklm') == 7
    assert cmp.dist_abs('abcdefg', 'hijklmno') == 8

def test_bag_sim():
    """Test abydos.distance.Bag.sim."""
    assert cmp.sim('', '') == 1
    assert cmp.sim('nelson', '') == 0
    assert cmp.sim('', 'neilsen') == 0
    assert cmp.sim('ab', 'a') == 0.5
    assert cmp.sim('ab', 'c') == 0
    assert cmp.sim('nelson', 'neilsen') == pytest.approx(abs=1e-7, expected=5 / 7)
    assert cmp.sim('neilsen', 'nelson') == pytest.approx(abs=1e-7, expected=5 / 7)
    assert cmp.sim('niall', 'neal') == pytest.approx(abs=1e-7, expected=3 / 5)
    assert cmp.sim('aluminum', 'Catalan') == pytest.approx(abs=1e-7, expected=3 / 8)
    assert cmp.sim('abcdefg', 'hijklm') == 0
    assert cmp.sim('abcdefg', 'hijklmno') == 0

    assert Bag(tokenizer=SAPSTokenizer()).sim('DNA', 'RNA') == 0.5

def test_bag_dist():
    """Test abydos.distance.Bag.dist."""
    assert cmp.dist('', '') == 0
    assert cmp.dist('nelson', '') == 1
    assert cmp.dist('', 'neilsen') == 1
    assert cmp.dist('ab', 'a') == 0.5
    assert cmp.dist('ab', 'c') == 1
    assert cmp.dist('nelson', 'neilsen') == pytest.approx(abs=1e-7, expected=2 / 7)
    assert cmp.dist('neilsen', 'nelson') == pytest.approx(abs=1e-7, expected=2 / 7)
    assert cmp.dist('niall', 'neal') == pytest.approx(abs=1e-7, expected=2 / 5)
    assert cmp.dist('aluminum', 'Catalan') == pytest.approx(abs=1e-7, expected=5 / 8)
    assert cmp.dist('abcdefg', 'hijklm') == 1
    assert cmp.dist('abcdefg', 'hijklmno') == 1
