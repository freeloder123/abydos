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

"""abydos.tests.distance.test_distance_bisim.

This module contains unit tests for abydos.distance.BISIM
"""


import pytest

from abydos.distance import BISIM


cmp = BISIM()

cmp3 = BISIM(qval=3)


def test_bi_sim_sim():
    """Test abydos.distance.BISIM.sim."""
    # Base cases
    assert cmp.sim('', '') == 1.0
    assert cmp.sim('a', '') == 0.0
    assert cmp.sim('', 'a') == 0.0
    assert cmp.sim('abc', '') == 0.0
    assert cmp.sim('', 'abc') == 0.0
    assert cmp.sim('abc', 'abc') == 1.0
    assert cmp.sim('abcd', 'efgh') == 0.0

    assert cmp.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.6)
    assert cmp.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.6)
    assert cmp.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.6)
    assert cmp.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.6)
    assert cmp.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.6)

    # test cases from Kondrak and Dorr (2003)
    assert cmp.sim('ara', 'ala') == pytest.approx(abs=1e-7, expected=0.6666666667)
    assert cmp.sim('atara', 'arata') == pytest.approx(abs=1e-7, expected=0.6)
    assert cmp.sim('amaryl', 'amikin') == pytest.approx(abs=1e-7, expected=0.4166666667)
    assert cmp.sim('amaryl', 'altoce') == pytest.approx(abs=1e-7, expected=0.250)

    # other examples from Kondrak and Dorr (2004)
    assert cmp.sim('Zantac', 'Xanax') == pytest.approx(abs=1e-7, expected=0.4166666667)
    assert cmp.sim('Zantac', 'Contac') == pytest.approx(abs=1e-7, expected=0.5833333333)
    assert cmp.sim('Xanax', 'Contac') == pytest.approx(abs=1e-7, expected=0.25)
    assert cmp3.sim('Zantac', 'Xanax') == pytest.approx(abs=1e-7, expected=0.333333333)
    assert cmp3.sim('Zantac', 'Contac') == pytest.approx(abs=1e-7, expected=0.5)
    assert cmp3.sim('Xanax', 'Contac') == pytest.approx(abs=1e-7, expected=0.166666667)

    assert cmp.sim('Toradol', 'Tramadol') == pytest.approx(abs=1e-7, expected=0.6875)
    assert cmp.sim('Toradol', 'Tobradex') == pytest.approx(abs=1e-7, expected=0.6250)
    assert cmp.sim('Toradol', 'Torecan') == pytest.approx(abs=1e-7, expected=0.57142857)
    assert cmp.sim('Toradol', 'Stadol') == pytest.approx(abs=1e-7, expected=0.5)
    assert cmp.sim('Toradol', 'Torsemide') == pytest.approx(abs=1e-7, expected=0.5)
    assert cmp.sim('Toradol', 'Theraflu') == pytest.approx(abs=1e-7, expected=0.5)
    assert cmp.sim('Toradol', 'Tegretol') == pytest.approx(abs=1e-7, expected=0.5)
    assert cmp.sim('Toradol', 'Taxol') == pytest.approx(abs=1e-7, expected=0.5)
