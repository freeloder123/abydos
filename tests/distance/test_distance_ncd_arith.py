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

"""abydos.tests.distance.test_distance_ncd_arith.

This module contains unit tests for abydos.distance.NCDarith
"""

import pytest

from abydos.compression import Arithmetic
from abydos.distance import NCDarith

from .. import NIALL


class TestNCDarith:
    """Test compression distance functions.

    abydos.distance.NCDarith
    """

    arith = Arithmetic(' '.join(NIALL))
    cmp = NCDarith()
    cmp_probs = NCDarith(arith.get_probs())

    def test_ncd_arith_dist(self):
        """Test abydos.distance.NCDarith.dist."""
        assert self.cmp.dist('', '') == 0
        assert self.cmp_probs.dist('', '') == 0
        assert self.cmp.dist('a', '') > 0
        assert self.cmp_probs.dist('a', '') > 0
        assert self.cmp.dist('abcdefg', 'fg') > 0

        assert self.cmp_probs.dist('Niall', 'Neil') == pytest.approx(
            abs=1e-7, expected=0.608695652173913
        )
        assert self.cmp_probs.dist('Neil', 'Niall') == pytest.approx(
            abs=1e-7, expected=0.608695652173913
        )
        assert self.cmp.dist('Niall', 'Neil') == pytest.approx(
            abs=1e-7, expected=0.6875
        )
        assert self.cmp.dist('Neil', 'Niall') == pytest.approx(
            abs=1e-7, expected=0.6875
        )
        assert self.cmp_probs.dist('Njáll', 'Njall') == pytest.approx(
            abs=1e-7, expected=0.714285714285714
        )
        assert self.cmp_probs.dist('Njall', 'Njáll') == pytest.approx(
            abs=1e-7, expected=0.714285714285714
        )
        assert self.cmp.dist('Njáll', 'Njall') == pytest.approx(
            abs=1e-7, expected=0.75
        )
        assert self.cmp.dist('Njall', 'Njáll') == pytest.approx(
            abs=1e-7, expected=0.75
        )

    def test_ncd_arith_sim(self):
        """Test abydos.distance.NCDarith.sim."""
        assert self.cmp.sim('', '') == 1
        assert self.cmp_probs.sim('', '') == 1
        assert self.cmp.sim('a', '') < 1
        assert self.cmp_probs.sim('a', '') < 1
        assert self.cmp.sim('abcdefg', 'fg') < 1

        assert self.cmp_probs.sim('Niall', 'Neil') == pytest.approx(
            abs=1e-7, expected=0.3913043478260869
        )
        assert self.cmp_probs.sim('Neil', 'Niall') == pytest.approx(
            abs=1e-7, expected=0.3913043478260869
        )
        assert self.cmp.sim('Niall', 'Neil') == pytest.approx(
            abs=1e-7, expected=0.3125
        )
        assert self.cmp.sim('Neil', 'Niall') == pytest.approx(
            abs=1e-7, expected=0.3125
        )
        assert self.cmp_probs.sim('Njáll', 'Njall') == pytest.approx(
            abs=1e-7, expected=0.285714285714285
        )
        assert self.cmp_probs.sim('Njall', 'Njáll') == pytest.approx(
            abs=1e-7, expected=0.285714285714285
        )
        assert self.cmp.sim('Njáll', 'Njall') == pytest.approx(
            abs=1e-7, expected=0.25
        )
        assert self.cmp.sim('Njall', 'Njáll') == pytest.approx(
            abs=1e-7, expected=0.25
        )
