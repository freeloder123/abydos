# Copyright 2018-2020 by Christopher C. Little.
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

"""abydos.tests.distance.test_distance_ozbay.

This module contains unit tests for abydos.distance.Ozbay
"""


import pytest

from abydos.distance import Ozbay


cmp = Ozbay()


def test_ozbay_dist_abs():
    """Test abydos.distance.Ozbay.dist_abs."""
    assert cmp.dist_abs('', '') == 0.0

    assert cmp.dist_abs('piccadilly', 'bandage') == pytest.approx(abs=1e-7, expected=73.63636363636363)
    assert cmp.dist_abs('abcd', 'efgh') == pytest.approx(abs=1e-7, expected=16)

    # Test cases from https://github.com/hakanozbay/ozbay-metric
    assert cmp.dist_abs('ban', 'ban') == 0.0
    assert cmp.dist_abs('ban', 'bane') == pytest.approx(abs=1e-7, expected=0.3333333333)
    assert cmp.dist_abs('ban', 'band') == pytest.approx(abs=1e-7, expected=0.3333333333)
    assert cmp.dist_abs('ban', 'bat') == 0.75
    assert cmp.dist_abs('ban', 'bands') == pytest.approx(abs=1e-7, expected=1.3333333333)
    assert cmp.dist_abs('ban', 'banana') == 2.0
    assert cmp.dist_abs('ban', 'bandana') == pytest.approx(abs=1e-7, expected=2.3333333333)
    assert cmp.dist_abs('ban', 'bandit') == 3.0
    assert cmp.dist_abs('ban', 'bandage') == pytest.approx(abs=1e-7, expected=4.6666666666)

    assert cmp.dist_abs('piccadilly', 'piccadilly') == 0.0
    assert cmp.dist_abs('piccadilly', 'piccadilyl') == 0.25
    assert cmp.dist_abs('piccadilly', 'piccadlily') == pytest.approx(abs=1e-7, expected=0.3333333333)
    assert cmp.dist_abs('piccadilly', 'picacdilly') == 0.4
    assert cmp.dist_abs('piccadilly', 'picadily') == 0.4
    assert cmp.dist_abs('picadily', 'piccadilly') == 0.5
    assert cmp.dist_abs('piccadilly', 'picacdlily') == pytest.approx(abs=1e-7, expected=1.3333333333)
    assert cmp.dist_abs('ipcacdily', 'piccadilly') == pytest.approx(abs=1e-7, expected=1.4814814814814814)
    assert cmp.dist_abs('piccadilly', 'ipcacdily') == pytest.approx(abs=1e-7, expected=1.333333333)
    assert cmp.dist_abs('piccadilly', 'pcicadlyil') == 2.0

def test_ozbay_dist():
    """Test abydos.distance.Ozbay.dist."""
    assert cmp.dist('', '') == 0

    assert cmp.dist('piccadilly', 'bandage') == pytest.approx(abs=1e-7, expected=0.9467532467532467)
    assert cmp.dist('abcd', 'efgh') == pytest.approx(abs=1e-7, expected=1.0)

    # Test cases from https://github.com/hakanozbay/ozbay-metric
    assert cmp.dist('ban', 'ban') == 0.0
    assert cmp.dist('ban', 'bane') == pytest.approx(abs=1e-7, expected=0.006944444444444444)
    assert cmp.dist('ban', 'band') == pytest.approx(abs=1e-7, expected=0.006944444444444444)
    assert cmp.dist('ban', 'bat') == 0.02777777777777778
    assert cmp.dist('ban', 'bands') == pytest.approx(abs=1e-7, expected=0.03555555555555556)
    assert cmp.dist('ban', 'banana') == 0.05555555555555555
    assert cmp.dist('ban', 'bandana') == pytest.approx(abs=1e-7, expected=0.0634920634920635)
    assert cmp.dist('ban', 'bandit') == 0.08333333333333333
    assert cmp.dist('ban', 'bandage') == pytest.approx(abs=1e-7, expected=0.126984126984127)

    assert cmp.dist('piccadilly', 'piccadilly') == 0.0
    assert cmp.dist('piccadilly', 'piccadilyl') == 0.0004999999999999999
    assert cmp.dist('piccadilly', 'piccadlily') == pytest.approx(abs=1e-7, expected=0.0013333333333333335)
    assert cmp.dist('piccadilly', 'picacdilly') == 0.002
    assert cmp.dist('piccadilly', 'picadily') == 0.0025
    assert cmp.dist('picadily', 'piccadilly') == 0.003125
    assert cmp.dist('piccadilly', 'picacdlily') == pytest.approx(abs=1e-7, expected=0.009333333333333334)
    assert cmp.dist('ipcacdily', 'piccadilly') == pytest.approx(abs=1e-7, expected=0.011522633744855966)
    assert cmp.dist('piccadilly', 'ipcacdily') == pytest.approx(abs=1e-7, expected=0.01037037037037037)
    assert cmp.dist('piccadilly', 'pcicadlyil') == 0.014
