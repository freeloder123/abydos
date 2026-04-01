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

"""abydos.tests.distance.test_distance_jaro_winkler.

This module contains unit tests for abydos.distance.JaroWinkler
"""


import pytest

from abydos.distance import JaroWinkler


jaro = JaroWinkler(mode='jaro')

jaro_winkler = JaroWinkler(mode='winkler')


def test_sim_jaro_winkler():
    """Test abydos.distance.JaroWinkler.sim."""
    assert jaro.sim('', '') == 1
    assert jaro_winkler.sim('', '') == 1
    assert jaro.sim('MARTHA', '') == 0
    assert jaro_winkler.sim('MARTHA', '') == 0
    assert jaro.sim('', 'MARHTA') == 0
    assert jaro_winkler.sim('', 'MARHTA') == 0
    assert jaro.sim('MARTHA', 'MARTHA') == 1
    assert jaro_winkler.sim('MARTHA', 'MARTHA') == 1

    # https://en.wikipedia.org/wiki/Jaro-Winkler_distance
    assert jaro.sim('MARTHA', 'MARHTA') == pytest.approx(abs=1e-7, expected=0.94444444)
    assert jaro_winkler.sim('MARTHA', 'MARHTA') == pytest.approx(abs=1e-7, expected=0.96111111)
    assert jaro.sim('DWAYNE', 'DUANE') == pytest.approx(abs=1e-7, expected=0.82222222)
    assert jaro_winkler.sim('DWAYNE', 'DUANE') == pytest.approx(abs=1e-7, expected=0.84)
    assert jaro.sim('DIXON', 'DICKSONX') == pytest.approx(abs=1e-7, expected=0.76666666)
    assert jaro_winkler.sim('DIXON', 'DICKSONX') == pytest.approx(abs=1e-7, expected=0.81333333)

    with pytest.raises(ValueError):
        JaroWinkler(boost_threshold=2).sim('abcd', 'dcba')
    with pytest.raises(ValueError):
        JaroWinkler(boost_threshold=-1).sim('abcd', 'dcba')
    with pytest.raises(ValueError):
        JaroWinkler(scaling_factor=0.3).sim('abcd', 'dcba')
    with pytest.raises(ValueError):
        JaroWinkler(scaling_factor=-1).sim('abcd', 'dcba')

    assert jaro_winkler.sim('ABCD', 'EFGH') == pytest.approx(abs=1e-7, expected=0.0)

    # long_strings = True (applies only to Jaro-Winkler, not Jaro)
    assert (
        JaroWinkler(long_strings=True).sim('ABCD', 'EFGH')
        == jaro.sim('ABCD', 'EFGH')
    )
    assert (
        JaroWinkler(mode='jaro', long_strings=True).sim( 'DIXON', 'DICKSONX' )
        == jaro.sim('DIXON', 'DICKSONX')
    )
    assert JaroWinkler(mode='winkler', long_strings=True).sim(
            'DIXON', 'DICKSONX'
        ) == pytest.approx(abs=1e-7, expected=0.83030303)
    assert JaroWinkler(mode='winkler', long_strings=True).sim(
            'MARTHA', 'MARHTA'
        ) == pytest.approx(abs=1e-7, expected=0.97083333)

def test_dist_jaro_winkler():
    """Test abydos.distance.JaroWinkler.dist."""
    assert jaro.dist('', '') == 0
    assert jaro_winkler.dist('', '') == 0
    assert jaro.dist('MARTHA', '') == 1
    assert jaro_winkler.dist('MARTHA', '') == 1
    assert jaro.dist('', 'MARHTA') == 1
    assert jaro_winkler.dist('', 'MARHTA') == 1
    assert jaro.dist('MARTHA', 'MARTHA') == 0
    assert jaro_winkler.dist('MARTHA', 'MARTHA') == 0

    # https://en.wikipedia.org/wiki/Jaro-Winkler_distance
    assert jaro.dist('MARTHA', 'MARHTA') == pytest.approx(abs=1e-7, expected=0.05555555)
    assert jaro_winkler.dist('MARTHA', 'MARHTA') == pytest.approx(abs=1e-7, expected=0.03888888)
    assert jaro.dist('DWAYNE', 'DUANE') == pytest.approx(abs=1e-7, expected=0.17777777)
    assert jaro_winkler.dist('DWAYNE', 'DUANE') == pytest.approx(abs=1e-7, expected=0.16)
    assert jaro.dist('DIXON', 'DICKSONX') == pytest.approx(abs=1e-7, expected=0.23333333)
    assert jaro_winkler.dist('DIXON', 'DICKSONX') == pytest.approx(abs=1e-7, expected=0.18666666)

    with pytest.raises(ValueError):
        JaroWinkler(boost_threshold=2).dist('abcd', 'dcba')
    with pytest.raises(ValueError):
        JaroWinkler(boost_threshold=-1).dist('abcd', 'dcba')
    with pytest.raises(ValueError):
        JaroWinkler(scaling_factor=0.3).dist('abcd', 'dcba')
    with pytest.raises(ValueError):
        JaroWinkler(scaling_factor=-1).dist('abcd', 'dcba')

    assert jaro_winkler.dist('ABCD', 'EFGH') == pytest.approx(abs=1e-7, expected=1.0)
