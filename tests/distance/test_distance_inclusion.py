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

"""abydos.tests.distance.test_distance_inclusion.

This module contains unit tests for abydos.distance.Inclusion
"""


from abydos.distance import Inclusion


cmp = Inclusion()


def test_inclusion_dist():
    """Test abydos.distance.Inclusion.dist."""
    # Base cases
    assert cmp.dist('', '') == 0.0
    assert cmp.dist('a', '') == 1.0
    assert cmp.dist('', 'a') == 1.0
    assert cmp.dist('a', 'a') == 0.0
    assert cmp.dist('abc', '') == 1.0
    assert cmp.dist('', 'abc') == 1.0
    assert cmp.dist('abc', 'abc') == 0.0
    assert cmp.dist('abcd', 'efgh') == 1.0

    # Testcases from paper
    assert cmp.dist('ALINE', 'LINA') == 0.0
    assert cmp.dist('ADELINE', 'LINA') == 0.0
    assert cmp.dist('DIONNE', 'DONNE') == 0.0
    assert cmp.dist('ANGELINE', 'ADELINE') == 1.0
    assert cmp.dist('CASSEGRAIN', 'CASGRAIN') == 1.0

    # coverage
    assert cmp.dist('abc', 'abcd') == 0.0
    assert cmp.dist('abcd', 'abc') == 0.0
