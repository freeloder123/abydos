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

"""abydos.tests.distance.test_distance_ncd_bwtrle.

This module contains unit tests for abydos.distance.NCDbwtrle
"""

import pytest

from abydos.distance import NCDbwtrle


class TestNCDbwtrle:
    """Test compression distance functions.

    abydos.distance.NCDbwtrle
    """

    cmp = NCDbwtrle()

    def test_ncd_bwtrle_dist(self):
        """Test abydos.distance.NCDbwtrle.dist."""
        assert self.cmp.dist('', '') == 0
        assert self.cmp.dist('a', '') > 0
        assert self.cmp.dist('abcdefg', 'fg') > 0

        assert self.cmp.dist('abc', 'abc') == pytest.approx(
            abs=1e-7, expected=0
        )
        assert self.cmp.dist('abc', 'def') == pytest.approx(
            abs=1e-7, expected=0.75
        )

        assert self.cmp.dist('banana', 'banane') == pytest.approx(
            abs=1e-7, expected=0.57142857142
        )
        assert self.cmp.dist('bananas', 'bananen') == pytest.approx(
            abs=1e-7, expected=0.5
        )

    def test_ncd_bwtrle_sim(self):
        """Test abydos.distance.NCDbwtrle.sim."""
        assert self.cmp.sim('', '') == 1
        assert self.cmp.sim('a', '') < 1
        assert self.cmp.sim('abcdefg', 'fg') < 1

        assert self.cmp.sim('abc', 'abc') == pytest.approx(
            abs=1e-7, expected=1
        )
        assert self.cmp.sim('abc', 'def') == pytest.approx(
            abs=1e-7, expected=0.25
        )

        assert self.cmp.sim('banana', 'banane') == pytest.approx(
            abs=1e-7, expected=0.42857142857
        )
        assert self.cmp.sim('bananas', 'bananen') == pytest.approx(
            abs=1e-7, expected=0.5
        )
