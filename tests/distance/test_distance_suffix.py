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

"""abydos.tests.distance.test_distance_suffix.

This module contains unit tests for abydos.distance.suffix
"""


import pytest

from abydos.distance import Suffix


cmp = Suffix()


def test_suffix_sim():
    """Test abydos.distance.Suffix.sim."""
    assert cmp.sim('', '') == 1
    assert cmp.sim('a', '') == 0
    assert cmp.sim('', 'a') == 0
    assert cmp.sim('a', 'a') == 1
    assert cmp.sim('ax', 'a') == 0
    assert cmp.sim('axx', 'a') == 0
    assert cmp.sim('ax', 'ay') == 0
    assert cmp.sim('a', 'ay') == 0
    assert cmp.sim('a', 'ayy') == 0
    assert cmp.sim('ax', 'ay') == 0
    assert cmp.sim('a', 'y') == 0
    assert cmp.sim('y', 'a') == 0
    assert cmp.sim('aaax', 'aaa') == 0
    assert cmp.sim('axxx', 'aaa') == 0
    assert cmp.sim('aaxx', 'aayy') == 0
    assert cmp.sim('xxaa', 'yyaa') == 1 / 2
    assert cmp.sim('aaxxx', 'aay') == 0
    assert cmp.sim('aaxxxx', 'aayyy') == 0
    assert cmp.sim('xa', 'a') == 1
    assert cmp.sim('xxa', 'a') == 1
    assert cmp.sim('xa', 'ya') == 1 / 2
    assert cmp.sim('a', 'ya') == 1
    assert cmp.sim('a', 'yya') == 1
    assert cmp.sim('xa', 'ya') == 1 / 2
    assert cmp.sim('xaaa', 'aaa') == 1
    assert cmp.sim('xxxa', 'aaa') == pytest.approx(abs=1e-7, expected=1 / 3)
    assert cmp.sim('xxxaa', 'yaa') == pytest.approx(abs=1e-7, expected=2 / 3)
    assert cmp.sim('xxxxaa', 'yyyaa') == 2 / 5

def test_suffix_dist():
    """Test abydos.distance.Suffix.dist."""
    assert cmp.dist('', '') == 0
    assert cmp.dist('a', '') == 1
    assert cmp.dist('', 'a') == 1
    assert cmp.dist('a', 'a') == 0
    assert cmp.dist('ax', 'a') == 1
    assert cmp.dist('axx', 'a') == 1
    assert cmp.dist('ax', 'ay') == 1
    assert cmp.dist('a', 'ay') == 1
    assert cmp.dist('a', 'ayy') == 1
    assert cmp.dist('ax', 'ay') == 1
    assert cmp.dist('a', 'y') == 1
    assert cmp.dist('y', 'a') == 1
    assert cmp.dist('aaax', 'aaa') == 1
    assert cmp.dist('axxx', 'aaa') == 1
    assert cmp.dist('aaxx', 'aayy') == 1
    assert cmp.dist('xxaa', 'yyaa') == 1 / 2
    assert cmp.dist('aaxxx', 'aay') == 1
    assert cmp.dist('aaxxxx', 'aayyy') == 1
    assert cmp.dist('xa', 'a') == 0
    assert cmp.dist('xxa', 'a') == 0
    assert cmp.dist('xa', 'ya') == 1 / 2
    assert cmp.dist('a', 'ya') == 0
    assert cmp.dist('a', 'yya') == 0
    assert cmp.dist('xa', 'ya') == 1 / 2
    assert cmp.dist('xaaa', 'aaa') == 0
    assert cmp.dist('xxxa', 'aaa') == pytest.approx(abs=1e-7, expected=2 / 3)
    assert cmp.dist('xxxaa', 'yaa') == pytest.approx(abs=1e-7, expected=1 / 3)
    assert cmp.dist('xxxxaa', 'yyyaa') == 3 / 5
