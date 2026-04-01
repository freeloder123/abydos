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

"""abydos.tests.distance.test_distance_mlipns.

This module contains unit tests for abydos.distance.MLIPNS
"""


from abydos.distance import MLIPNS


cmp = MLIPNS()


def test_mlipns_sim():
    """Test abydos.distance.MLIPNS.sim."""
    assert cmp.sim('', '') == 1
    assert cmp.sim('a', '') == 0
    assert cmp.sim('', 'a') == 0
    assert cmp.sim('a', 'a') == 1
    assert cmp.sim('ab', 'a') == 1
    assert cmp.sim('abc', 'abc') == 1
    assert cmp.sim('abc', 'abcde') == 1
    assert cmp.sim('abcg', 'abcdeg') == 1
    assert cmp.sim('abcg', 'abcdefg') == 0
    assert cmp.sim('Tomato', 'Tamato') == 1
    assert cmp.sim('ato', 'Tam') == 1

def test_mlipns_dist():
    """Test abydos.distance.MLIPNS.dist."""
    assert cmp.dist('', '') == 0
    assert cmp.dist('a', '') == 1
    assert cmp.dist('', 'a') == 1
    assert cmp.dist('a', 'a') == 0
    assert cmp.dist('ab', 'a') == 0
    assert cmp.dist('abc', 'abc') == 0
    assert cmp.dist('abc', 'abcde') == 0
    assert cmp.dist('abcg', 'abcdeg') == 0
    assert cmp.dist('abcg', 'abcdefg') == 1
    assert cmp.dist('Tomato', 'Tamato') == 0
    assert cmp.dist('ato', 'Tam') == 0
