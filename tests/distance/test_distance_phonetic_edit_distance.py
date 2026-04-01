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

"""abydos.tests.distance.test_distance_phonetic_edit_distance.

This module contains unit tests for abydos.distance.PhoneticEditDistance
"""


import pytest

from abydos.distance import PhoneticEditDistance


ped = PhoneticEditDistance()


def test_phonetic_edit_distance_dist():
    """Test abydos.distance.PhoneticEditDistance.dist."""
    # Base cases
    assert ped.dist('', '') == 0.0
    assert ped.dist('a', '') == 1.0
    assert ped.dist('', 'a') == 1.0
    assert ped.dist('abc', '') == 1.0
    assert ped.dist('', 'abc') == 1.0
    assert ped.dist('abc', 'abc') == 0.0
    assert ped.dist('abcd', 'efgh') == 0.10483870967741934

    assert ped.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.1774193548387097)
    assert ped.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.1774193548387097)
    assert ped.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.1741935483870968)
    assert ped.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.1741935483870968)
    assert ped.dist('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.2370967741935484)

def test_phonetic_edit_distance_dist_abs():
    """Test abydos.distance.PhoneticEditDistance.dist_abs."""
    # Base cases
    assert ped.dist_abs('', '') == 0
    assert ped.dist_abs('a', '') == 1
    assert ped.dist_abs('', 'a') == 1
    assert ped.dist_abs('abc', '') == 3
    assert ped.dist_abs('', 'abc') == 3
    assert ped.dist_abs('abc', 'abc') == 0
    assert ped.dist_abs('abcd', 'efgh') == 0.4193548387096774

    assert ped.dist_abs('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.8870967741935485)
    assert ped.dist_abs('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.8870967741935485)
    assert ped.dist_abs('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.870967741935484)
    assert ped.dist_abs('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.870967741935484)
    assert ped.dist_abs('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=2.370967741935484)

    assert (
        PhoneticEditDistance(weights={'syllabic': 1.0}).dist_abs( 'Nigel', 'Niall' )
        == 0.0
    )
    assert PhoneticEditDistance(weights=(1, 1, 1)).dist_abs('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.33333333333333326)
    assert PhoneticEditDistance(mode='osa').dist_abs('Niel', 'Neil') == pytest.approx(abs=1e-7, expected=0.06451612903225801)

def test_phonetic_edit_distance_alignment():
    """Test abydos.distance.PhoneticEditDistance.alignment."""
    # Base cases
    assert ped.alignment('', '') == (0.0, '', '')
    assert ped.alignment('a', '') == (1.0, 'a', '-')
    assert ped.alignment('', 'a') == (1.0, '-', 'a')
    assert ped.alignment('abc', '') == (3.0, 'abc', '---')
    assert ped.alignment('', 'abc') == (3.0, '---', 'abc')
    assert ped.alignment('abc', 'abc') == (0.0, 'abc', 'abc')
    assert (
        ped.alignment('abcd', 'efgh')
        == (0.4193548387096774, 'abcd', 'efgh')
    )

    assert (
        ped.alignment('Nigel', 'Niall')
        == (0.8870967741935485, 'Nigel', 'Niall')
    )
    assert (
        ped.alignment('Niall', 'Nigel')
        == (0.8870967741935485, 'Niall', 'Nigel')
    )
    assert (
        ped.alignment('Colin', 'Coiln')
        == (0.870967741935484, 'Colin', 'Coiln')
    )
    assert (
        ped.alignment('Coiln', 'Colin')
        == (0.870967741935484, 'Coiln', 'Colin')
    )
    assert (
        PhoneticEditDistance(mode='osa').alignment('Niel', 'Neil')
        == (0.06451612903225801, 'Niel', 'Neil')
    )
