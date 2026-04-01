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

"""abydos.tests.distance.test_distance_discounted_levenshtein.

This module contains unit tests for abydos.distance.DiscountedLevenshtein
"""


import pytest

from abydos.distance import DiscountedLevenshtein


cmp = DiscountedLevenshtein()

cmp_coda = DiscountedLevenshtein(discount_from='coda')


def test_discounted_levenshtein_aligmnent():
    """Test abydos.distance.DiscountedLevenshtein.alignment."""
    assert cmp.alignment('', '') == (0, '', '')

    assert cmp.alignment('a', 'a') == (0.0, 'a', 'a')
    assert cmp.alignment('ab', 'ab') == (0.0, 'ab', 'ab')
    assert cmp.alignment('', 'a') == (1.0, '-', 'a')
    assert cmp.alignment('', 'ab') == (1.845793595028118, '--', 'ab')
    assert cmp.alignment('a', 'c') == (1.0, 'a', 'c')

    assert cmp.alignment('abc', 'ac') == (1.0, 'abc', 'a-c')
    assert cmp.alignment('abbc', 'ac') == (1.845793595028118, 'abbc', 'a--c')
    assert cmp.alignment('abbc', 'abc') == (0.8457935950281179, 'abbc', 'ab-c')

    assert (
        DiscountedLevenshtein(mode='osa').alignment('Niall', 'Naill')
        == (0.8457935950281179, 'Niall', 'Naill')
    )

    assert cmp.alignment('abcd', 'efgh') == (3.594032108779918, 'abcd', 'efgh')

    assert (
        cmp.alignment('Nigel', 'Niall')
        == (1.5940321087799176, 'Nigel', 'Niall')
    )
    assert (
        cmp.alignment('Niall', 'Nigel')
        == (1.5940321087799176, 'Niall', 'Nigel')
    )
    assert (
        cmp.alignment('Colin', 'Coiln')
        == (1.5940321087799176, 'Coli-n', 'Co-iln')
    )
    assert (
        cmp.alignment('Coiln', 'Colin')
        == (1.5940321087799176, 'Coil-n', 'Co-lin')
    )
    assert (
        cmp.alignment('cccColin', 'Colin')
        == (2.594032108779918, 'cccColin', '---Colin')
    )
    assert (
        cmp.alignment('Colin', 'cccColin')
        == (2.594032108779918, '---Colin', 'cccColin')
    )

def test_discounted_levenshtein_dist_abs():
    """Test abydos.distance.DiscountedLevenshtein.dist_abs."""
    # Base cases
    assert cmp.dist_abs('', '') == 0.0
    assert cmp.dist_abs('a', '') == 1.0
    assert cmp.dist_abs('', 'a') == 1.0
    assert cmp.dist_abs('abc', '') == 2.845793595028118
    assert cmp.dist_abs('', 'abc') == 2.845793595028118
    assert cmp.dist_abs('abc', 'abc') == 0.0
    assert cmp.dist_abs('abcd', 'efgh') == 3.594032108779918

    assert cmp.dist_abs('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=1.5940321087799176)
    assert cmp.dist_abs('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=1.5940321087799176)
    assert cmp.dist_abs('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=1.5940321087799176)
    assert cmp.dist_abs('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=1.5940321087799176)
    assert cmp.dist_abs('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=3.480037325627888)

def test_discounted_levenshtein_dist():
    """Test abydos.distance.DiscountedLevenshtein.dist."""
    # Base cases
    assert cmp.dist('', '') == 0.0
    assert cmp.dist('a', '') == 1.0
    assert cmp.dist('', 'a') == 1.0
    assert cmp.dist('abc', '') == 1.0
    assert cmp.dist('', 'abc') == 1.0
    assert cmp.dist('abc', 'abc') == 0.0
    assert cmp.dist('abcd', 'efgh') == 1.0

    assert cmp.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.3729338516783247)
    assert cmp.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.3729338516783247)
    assert cmp.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.3729338516783247)
    assert cmp.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.3729338516783247)
    assert cmp.dist('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.49025364879218414)

    assert cmp_coda.dist('', '') == 0.0
    assert cmp_coda.dist('a', '') == 1.0
    assert cmp_coda.dist('', 'a') == 1.0
    assert cmp_coda.dist('abc', '') == 1.0
    assert cmp_coda.dist('', 'abc') == 1.0
    assert cmp_coda.dist('abc', 'abc') == 0.0
    assert cmp_coda.dist('abcd', 'efgh') == 1.0

    assert cmp_coda.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.43183503707707127)
    assert cmp_coda.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.43183503707707127)
    assert cmp_coda.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.43183503707707127)
    assert cmp_coda.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.43183503707707127)
    assert cmp_coda.dist('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.49025364879218414)

    # coverage additions
    assert DiscountedLevenshtein(discount_func='exp').dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.3776202500185377)
    assert DiscountedLevenshtein(
            discount_func=lambda x: 1 / (x + 2) ** 0.3
        ).dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.3808786265263343)
    assert cmp_coda.dist('da', 'dde') == pytest.approx(abs=1e-7, expected=0.7027916583599728)
    assert cmp_coda.dist('d', 'dd') == pytest.approx(abs=1e-7, expected=0.42289679751405895)
    assert DiscountedLevenshtein(discount_from='invalid value').dist(
            'Nigel', 'Niall'
        ) == pytest.approx(abs=1e-7, expected=0.3729338516783247)
    assert DiscountedLevenshtein(mode='osa').dist('Nigel', 'Ngiall') == pytest.approx(abs=1e-7, expected=0.4534644632194963)
