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

"""abydos.tests.distance.test_distance_generalized_fleiss.

This module contains unit tests for abydos.distance.GeneralizedFleiss
"""


import pytest

from abydos.distance import GeneralizedFleiss


cmp = GeneralizedFleiss(marginals='a')

cmp_no_d = GeneralizedFleiss(alphabet=0)

cmp_b = GeneralizedFleiss(marginals='b')

cmp_c = GeneralizedFleiss(marginals='c')

cmp_prop = GeneralizedFleiss(proportional=True)

cmp_quad = GeneralizedFleiss(mean_func='quadratic')

cmp_hero = GeneralizedFleiss(mean_func='heronian')

cmp_ag = GeneralizedFleiss(mean_func='ag')

cmp_gh = GeneralizedFleiss(mean_func='gh')

cmp_agh = GeneralizedFleiss(mean_func='agh')


def test_generalized_fleiss_sim():
    """Test abydos.distance.GeneralizedFleiss.sim."""
    # Base cases
    assert cmp.sim('', '') == 0.5
    assert cmp.sim('a', '') == 0.5
    assert cmp.sim('', 'a') == 0.5
    assert cmp.sim('abc', '') == 0.5
    assert cmp.sim('', 'abc') == 0.5
    assert cmp.sim('abc', 'abc') == 1.0
    assert cmp.sim('abcd', 'efgh') == 0.496790757381258

    assert cmp.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.7480719794)
    assert cmp.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.7480719794)
    assert cmp.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.7480719794)
    assert cmp.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.7480719794)
    assert cmp.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.8310964723)

    # Tests with alphabet=0 (no d factor)
    assert cmp_no_d.sim('', '') == 0.5
    assert cmp_no_d.sim('a', '') == 0.5
    assert cmp_no_d.sim('', 'a') == 0.5
    assert cmp_no_d.sim('abc', '') == 0.5
    assert cmp_no_d.sim('', 'abc') == 0.5
    assert cmp_no_d.sim('abc', 'abc') == 0.5
    assert cmp_no_d.sim('abcd', 'efgh') == 0.0

    assert cmp_no_d.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.25)
    assert cmp_no_d.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.25)
    assert cmp_no_d.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.25)
    assert cmp_no_d.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.25)
    assert cmp_no_d.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.3356164384)

    # marginals b
    assert cmp_b.sim('abc', 'abc') == 0.5051280702677116
    assert cmp_b.sim('abcd', 'efgh') == 0.4999588047443752

    assert cmp_b.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.5038260754642173)
    assert cmp_b.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.5038260754642173)
    assert cmp_b.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.5038260754642173)
    assert cmp_b.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.5038260754642173)
    assert cmp_b.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.5089871192422611)

    # marginals c
    assert cmp_c.sim('abc', 'abc') == 1.0
    assert cmp_c.sim('abcd', 'efgh') == 0.496790757381258

    assert cmp_c.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.7480719794344473)
    assert cmp_c.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.7480719794344473)
    assert cmp_c.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.7480719794344473)
    assert cmp_c.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.7480719794344473)
    assert cmp_c.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.8310760896330953)

    # proportional
    assert cmp_prop.sim('abc', 'abc') == 1.0
    assert cmp_prop.sim('abcd', 'efgh') == 0.496790757381258

    assert cmp_prop.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.7480719794)
    assert cmp_prop.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.7480719794)
    assert cmp_prop.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.7480719794)
    assert cmp_prop.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.7480719794)
    assert cmp_prop.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.8310964723)

    # quadratic mean
    assert cmp_quad.sim('abc', 'abc') == 1.0
    assert cmp_quad.sim('abcd', 'efgh') == 0.496790757381258

    assert cmp_quad.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.7480719794)
    assert cmp_quad.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.7480719794)
    assert cmp_quad.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.7480719794)
    assert cmp_quad.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.7480719794)
    assert cmp_quad.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.8307317829209393)

    # heronian mean
    assert cmp_hero.sim('abc', 'abc') == 1.0
    assert cmp_hero.sim('abcd', 'efgh') == 0.496790757381258

    assert cmp_hero.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.7480719794)
    assert cmp_hero.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.7480719794)
    assert cmp_hero.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.7480719794)
    assert cmp_hero.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.7480719794)
    assert cmp_hero.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.8312183486929234)

    # ag mean
    assert cmp_ag.sim('abc', 'abc') == 1.0
    assert cmp_ag.sim('abcd', 'efgh') == 0.496790757381258

    assert cmp_ag.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.7480719794)
    assert cmp_ag.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.7480719794)
    assert cmp_ag.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.7480719794)
    assert cmp_ag.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.7480719794)
    assert cmp_ag.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.8312793457877081)

    # gh mean
    assert cmp_gh.sim('abc', 'abc') == 1.0
    assert cmp_gh.sim('abcd', 'efgh') == 0.496790757381258

    assert cmp_gh.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.7480719794)
    assert cmp_gh.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.7480719794)
    assert cmp_gh.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.7480719794)
    assert cmp_gh.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.7480719794)
    assert cmp_gh.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.8316454969290444)

    # agh mean
    assert cmp_agh.sim('abc', 'abc') == 1.0
    assert cmp_agh.sim('abcd', 'efgh') == 0.496790757381258

    assert cmp_agh.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.7480719794)
    assert cmp_agh.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.7480719794)
    assert cmp_agh.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.7480719794)
    assert cmp_agh.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.7480719794)
    assert cmp_agh.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.8314623707995847)

def test_generalized_fleiss_dist():
    """Test abydos.distance.GeneralizedFleiss.dist."""
    # Base cases
    assert cmp.dist('', '') == 0.5
    assert cmp.dist('a', '') == 0.5
    assert cmp.dist('', 'a') == 0.5
    assert cmp.dist('abc', '') == 0.5
    assert cmp.dist('', 'abc') == 0.5
    assert cmp.dist('abc', 'abc') == 0.0
    assert cmp.dist('abcd', 'efgh') == 0.503209242618742

    assert cmp.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.2519280206)
    assert cmp.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.2519280206)
    assert cmp.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.2519280206)
    assert cmp.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.2519280206)
    assert cmp.dist('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.1689035277)

    # Tests with alphabet=0 (no d factor)
    assert cmp_no_d.dist('', '') == 0.5
    assert cmp_no_d.dist('a', '') == 0.5
    assert cmp_no_d.dist('', 'a') == 0.5
    assert cmp_no_d.dist('abc', '') == 0.5
    assert cmp_no_d.dist('', 'abc') == 0.5
    assert cmp_no_d.dist('abc', 'abc') == 0.5
    assert cmp_no_d.dist('abcd', 'efgh') == 1.0

    assert cmp_no_d.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.75)
    assert cmp_no_d.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.75)
    assert cmp_no_d.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.75)
    assert cmp_no_d.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.75)
    assert cmp_no_d.dist('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.6643835616)

def test_generalized_fleiss_corr():
    """Test abydos.distance.GeneralizedFleiss.corr."""
    # Base cases
    assert cmp.corr('', '') == 0.0
    assert cmp.corr('a', '') == 0.0
    assert cmp.corr('', 'a') == 0.0
    assert cmp.corr('abc', '') == 0.0
    assert cmp.corr('', 'abc') == 0.0
    assert cmp.corr('abc', 'abc') == 1.0
    assert cmp.corr('abcd', 'efgh') == -0.006418485237483954

    assert cmp.corr('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.4961439589)
    assert cmp.corr('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.4961439589)
    assert cmp.corr('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.4961439589)
    assert cmp.corr('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.4961439589)
    assert cmp.corr('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.6621929447)

    # Tests with alphabet=0 (no d factor)
    assert cmp_no_d.corr('', '') == 0.0
    assert cmp_no_d.corr('a', '') == 0.0
    assert cmp_no_d.corr('', 'a') == 0.0
    assert cmp_no_d.corr('abc', '') == 0.0
    assert cmp_no_d.corr('', 'abc') == 0.0
    assert cmp_no_d.corr('abc', 'abc') == 0.0
    assert cmp_no_d.corr('abcd', 'efgh') == -1.0

    assert cmp_no_d.corr('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=-0.5)
    assert cmp_no_d.corr('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=-0.5)
    assert cmp_no_d.corr('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=-0.5)
    assert cmp_no_d.corr('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=-0.5)
    assert cmp_no_d.corr('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=-0.3287671233)
