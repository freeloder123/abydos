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

"""abydos.tests.distance.test_distance_baulieu_iv.

This module contains unit tests for abydos.distance.BaulieuIV
"""


import pytest

from abydos.distance import BaulieuIV


cmp = BaulieuIV()

cmp_no_d = BaulieuIV(alphabet=0)


def test_baulieu_iv_dist():
    """Test abydos.distance.BaulieuIV.dist."""
    # Base cases
    assert cmp.dist('', '') == 0.4999995930090347
    assert cmp.dist('a', '') == 0.4999995950831843
    assert cmp.dist('', 'a') == 0.4999995950831843
    assert cmp.dist('abc', '') == 0.49999959715204023
    assert cmp.dist('', 'abc') == 0.49999959715204023
    assert cmp.dist('abc', 'abc') == 0.49999637435083444
    assert cmp.dist('abcd', 'efgh') == 0.4999996033268451

    assert cmp.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.4999972161)
    assert cmp.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.4999972161)
    assert cmp.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.4999972161)
    assert cmp.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.4999972161)
    assert cmp.dist('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.4999941112)

    # Tests with alphabet=0 (no d factor)
    assert cmp_no_d.dist('', '') == 0.0
    assert cmp_no_d.dist('a', '') == 0.5229924650732152
    assert cmp_no_d.dist('', 'a') == 0.5229924650732152
    assert cmp_no_d.dist('abc', '') == 0.5028740581341519
    assert cmp_no_d.dist('', 'abc') == 0.5028740581341519
    assert cmp_no_d.dist('abc', 'abc') == 0.5
    assert cmp_no_d.dist('abcd', 'efgh') == 0.5001839397205857

    assert cmp_no_d.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.5001682119)
    assert cmp_no_d.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.5001682119)
    assert cmp_no_d.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.5001682119)
    assert cmp_no_d.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.5001682119)
    assert cmp_no_d.dist('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.5000335167)

def test_baulieu_iv_sim():
    """Test abydos.distance.BaulieuIV.sim."""
    # Base cases
    assert cmp.sim('', '') == 0.5000004069909654
    assert cmp.sim('a', '') == 0.5000004049168156
    assert cmp.sim('', 'a') == 0.5000004049168156
    assert cmp.sim('abc', '') == 0.5000004028479598
    assert cmp.sim('', 'abc') == 0.5000004028479598
    assert cmp.sim('abc', 'abc') == 0.5000036256491656
    assert cmp.sim('abcd', 'efgh') == 0.5000003966731549

    assert cmp.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.5000027839)
    assert cmp.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.5000027839)
    assert cmp.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.5000027839)
    assert cmp.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.5000027839)
    assert cmp.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.5000058888)

    # Tests with alphabet=0 (no d factor)
    assert cmp_no_d.sim('', '') == 1.0
    assert cmp_no_d.sim('a', '') == 0.4770075349267848
    assert cmp_no_d.sim('', 'a') == 0.4770075349267848
    assert cmp_no_d.sim('abc', '') == 0.49712594186584813
    assert cmp_no_d.sim('', 'abc') == 0.49712594186584813
    assert cmp_no_d.sim('abc', 'abc') == 0.5
    assert cmp_no_d.sim('abcd', 'efgh') == 0.4998160602794143

    assert cmp_no_d.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.4998317881)
    assert cmp_no_d.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.4998317881)
    assert cmp_no_d.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.4998317881)
    assert cmp_no_d.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.4998317881)
    assert cmp_no_d.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.4999664833)

def test_baulieu_iv_dist_abs():
    """Test abydos.distance.BaulieuIV.dist_abs."""
    # Base cases
    assert cmp.dist_abs('', '') == -1066.2460472130606
    assert cmp.dist_abs('a', '') == -1060.8121333300487
    assert cmp.dist_abs('', 'a') == -1060.8121333300487
    assert cmp.dist_abs('abc', '') == -1055.3920882318764
    assert cmp.dist_abs('', 'abc') == -1055.3920882318764
    assert cmp.dist_abs('abc', 'abc') == -9498.574712454234
    assert cmp.dist_abs('abcd', 'efgh') == -1039.2151656463932

    assert cmp.dist_abs('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=-7293.3912640224)
    assert cmp.dist_abs('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=-7293.3912640224)
    assert cmp.dist_abs('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=-7293.3912640224)
    assert cmp.dist_abs('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=-7293.3912640224)
    assert cmp.dist_abs('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=-15427.7573462754)

    # Tests with alphabet=0 (no d factor)
    assert cmp_no_d.dist_abs('', '') == 0.0
    assert cmp_no_d.dist_abs('a', '') == 1.0
    assert cmp_no_d.dist_abs('', 'a') == 1.0
    assert cmp_no_d.dist_abs('abc', '') == 1.0
    assert cmp_no_d.dist_abs('', 'abc') == 1.0
    assert cmp_no_d.dist_abs('abc', 'abc') == 0.0
    assert cmp_no_d.dist_abs('abcd', 'efgh') == 1.0

    assert cmp_no_d.dist_abs('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.6666666667)
    assert cmp_no_d.dist_abs('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.6666666667)
    assert cmp_no_d.dist_abs('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.6666666667)
    assert cmp_no_d.dist_abs('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.6666666667)
    assert cmp_no_d.dist_abs('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.5)
