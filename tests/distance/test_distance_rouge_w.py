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

"""abydos.tests.distance.test_distance_rouge_w.

This module contains unit tests for abydos.distance.RougeW
"""


import pytest

from abydos.distance import RougeW


cmp = RougeW()

cmp_cubed = RougeW(f_func=lambda x: x ** 3, f_inv=lambda x: x ** (1 / 3))


def test_rouge_w_sim():
    """Test abydos.distance.RougeW.sim."""
    # Base cases
    assert cmp.sim('', '') == 1.0
    assert cmp.sim('a', '') == 0.0
    assert cmp.sim('', 'a') == 0.0
    assert cmp.sim('abc', '') == 0.0
    assert cmp.sim('', 'abc') == 0.0
    assert cmp.sim('abc', 'abc') == 1.0
    assert cmp.sim('abcd', 'efgh') == 0.0

    assert cmp.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.4472135955)
    assert cmp.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.4472135955)
    assert cmp.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.4898979486)
    assert cmp.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.4898979486)
    assert cmp.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.548566506)

    # Examples from paper
    assert round(cmp.sim('ABCDEFG', 'ABCDHIK'), 3) == 0.571
    assert round(cmp.sim('ABCDEFG', 'AHBKCID'), 3) == 0.286

    # Coverage
    assert cmp_cubed.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.4160167646)
    assert cmp_cubed.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.4308869380)
    assert cmp_cubed.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.5125114739)

def test_rouge_w_dist():
    """Test abydos.distance.RougeW.dist."""
    # Base cases
    assert cmp.dist('', '') == 0.0
    assert cmp.dist('a', '') == 1.0
    assert cmp.dist('', 'a') == 1.0
    assert cmp.dist('abc', '') == 1.0
    assert cmp.dist('', 'abc') == 1.0
    assert cmp.dist('abc', 'abc') == 0.0
    assert cmp.dist('abcd', 'efgh') == 1.0

    assert cmp.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.5527864045)
    assert cmp.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.5527864045)
    assert cmp.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.5101020514)
    assert cmp.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.5101020514)
    assert cmp.dist('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.451433494)

def test_rouge_w_wlcs():
    """Test abydos.distance.RougeW.wlcs."""
    assert cmp.wlcs('', '') == 0
    assert cmp.wlcs('a', '') == 0
    assert cmp.wlcs('', 'a') == 0
    assert cmp.wlcs('abc', '') == 0
    assert cmp.wlcs('', 'abc') == 0
    assert cmp.wlcs('abc', 'abc') == 9
