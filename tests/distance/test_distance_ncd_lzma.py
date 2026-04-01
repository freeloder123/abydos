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

"""abydos.tests.distance.test_distance_ncd_lzma.

This module contains unit tests for abydos.distance.NCDlzma
"""


import pytest

from abydos.distance import NCDlzma


cmp = NCDlzma()


def test_ncd_lzma_dist():
    """Test abydos.distance.NCDlzma.dist."""
    assert cmp.dist('', '') == 0
    assert cmp.dist('a', '') == pytest.approx(abs=1e-7, expected=0.6086956521739)
    assert cmp.dist('abcdefg', 'fg') == pytest.approx(abs=1e-7, expected=0.16)

def test_ncd_lzma_sim():
    """Test abydos.distance.NCDlzma.sim."""
    assert cmp.sim('', '') == 1
    assert cmp.sim('a', '') == pytest.approx(abs=1e-7, expected=0.391304347826)
    assert cmp.sim('abcdefg', 'fg') == pytest.approx(abs=1e-7, expected=0.84)
