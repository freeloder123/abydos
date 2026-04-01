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

"""abydos.tests.distance.test_distance_length.

This module contains unit tests for abydos.distance.Length
"""


from abydos.distance import Length


cmp = Length()


def test_length_sim():
    """Test abydos.distance.Length.sim."""
    assert cmp.sim('', '') == 1
    assert cmp.sim('', 'a') == 0
    assert cmp.sim('a', '') == 0
    assert cmp.sim('a', 'a') == 1
    assert cmp.sim('abcd', 'abcd') == 1
    assert cmp.sim('abcd', 'dcba') == 1
    assert cmp.sim('abc', 'cba') == 1
    assert cmp.sim('abc', 'dcba') == 0.75
    assert cmp.sim('abcd', 'cba') == 0.75
    assert cmp.sim('ab', 'dcba') == 0.5
    assert cmp.sim('abcd', 'ba') == 0.5

def test_length_dist():
    """Test abydos.distance.Length.dist."""
    assert cmp.dist('', '') == 0
    assert cmp.dist('', 'a') == 1
    assert cmp.dist('a', '') == 1
    assert cmp.dist('a', 'a') == 0
    assert cmp.dist('abcd', 'abcd') == 0
    assert cmp.dist('abcd', 'dcba') == 0
    assert cmp.dist('abc', 'cba') == 0
    assert cmp.dist('abc', 'dcba') == 0.25
    assert cmp.dist('abcd', 'cba') == 0.25
    assert cmp.dist('ab', 'dcba') == 0.5
    assert cmp.dist('abcd', 'ba') == 0.5
