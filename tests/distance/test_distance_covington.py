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

"""abydos.tests.distance.test_distance_covington.

This module contains unit tests for abydos.distance.Covington
"""

import pytest

from abydos.distance import Covington


class TestCovington:
    """Test Covington functions.

    abydos.distance.Covington
    """

    cmp = Covington()

    def test_covington_dist(self):
        """Test abydos.distance.Covington.dist."""
        # Base cases
        assert self.cmp.dist('', '') == 0.0
        assert self.cmp.dist('a', '') == 1.0
        assert self.cmp.dist('', 'a') == 1.0
        assert self.cmp.dist('abc', '') == 1.0
        assert self.cmp.dist('', 'abc') == 1.0
        assert self.cmp.dist('abc', 'abc') == 0.014705882352941176
        assert self.cmp.dist('abcd', 'efgh') == 0.4772727272727273

        assert self.cmp.dist('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.2592592593)
        assert self.cmp.dist('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.2592592593)
        assert self.cmp.dist('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.2037037037)
        assert self.cmp.dist('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.2037037037)
        assert self.cmp.dist('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.3578947368)

        assert self.cmp.dist('bcd', 'bcd') == 0.0

    def test_covington_sim(self):
        """Test abydos.distance.Covington.sim."""
        # Base cases
        assert self.cmp.sim('', '') == 1.0
        assert self.cmp.sim('a', '') == 0.0
        assert self.cmp.sim('', 'a') == 0.0
        assert self.cmp.sim('abc', '') == 0.0
        assert self.cmp.sim('', 'abc') == 0.0
        assert self.cmp.sim('abc', 'abc') == 0.9852941176470589
        assert self.cmp.sim('abcd', 'efgh') == 0.5227272727272727

        assert self.cmp.sim('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=0.7407407407)
        assert self.cmp.sim('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=0.7407407407)
        assert self.cmp.sim('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=0.7962962963)
        assert self.cmp.sim('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=0.7962962963)
        assert self.cmp.sim('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=0.6421052632)

        assert self.cmp.sim('bcd', 'bcd') == 1.0

    def test_covington_dist_abs(self):
        """Test abydos.distance.Covington.dist_abs."""
        # Base cases
        assert self.cmp.dist_abs('', '') == 0
        assert self.cmp.dist_abs('a', '') == 50
        assert self.cmp.dist_abs('', 'a') == 50
        assert self.cmp.dist_abs('abc', '') == 130
        assert self.cmp.dist_abs('', 'abc') == 130
        assert self.cmp.dist_abs('abc', 'abc') == 5
        assert self.cmp.dist_abs('abcd', 'efgh') == 210

        assert self.cmp.dist_abs('Nigel', 'Niall') == pytest.approx(abs=1e-7, expected=140)
        assert self.cmp.dist_abs('Niall', 'Nigel') == pytest.approx(abs=1e-7, expected=140)
        assert self.cmp.dist_abs('Colin', 'Coiln') == pytest.approx(abs=1e-7, expected=110)
        assert self.cmp.dist_abs('Coiln', 'Colin') == pytest.approx(abs=1e-7, expected=110)
        assert self.cmp.dist_abs('ATCAACGAGT', 'AACGATTAG') == pytest.approx(abs=1e-7, expected=340)

    def test_covington_alignments(self):
        """Test abydos.distance.Covington.alignments."""
        assert repr(self.cmp.alignments('yo', 'ze', top_n=1)[0]) == "Alignment(src='yo', tar='ze', score=130)"
        assert repr(self.cmp.alignments('tres', 'trwa', top_n=1)[0]) == "Alignment(src='tr-es', tar='trwa-', score=130)"
        assert repr(self.cmp.alignments('detir', 'dir', top_n=1)[0]) == "Alignment(src='detir', tar='d--ir', score=95)"
        assert repr(self.cmp.alignments('niy', 'kni', top_n=1)[0]) == "Alignment(src='-niy', tar='kni-', score=105)"
        assert repr(self.cmp.alignments('hart', 'kordis', top_n=1)[0]) == "Alignment(src='hart--', tar='kordis', score=240)"
        assert repr(self.cmp.alignments('niy', 'genu', top_n=1)[0]) == "Alignment(src='--niy', tar='genu-', score=170)"
        assert repr(self.cmp.alignments('namesa', 'namiqs', top_n=1)[0]) == "Alignment(src='name-sa', tar='namiqs-', score=135)"
        assert repr(self.cmp.alignments('kentum', 'satem', top_n=1)[0]) == "Alignment(src='kentum', tar='sa-tem', score=170)"
        assert repr(self.cmp.alignments('kentum', 'hekaton', top_n=1)[0]) == "Alignment(src='--kentum', tar='heka-ton', score=260)"
        assert repr(self.cmp.alignments('doter', 'tugatir', top_n=2)[1]) == "Alignment(src='do--ter', tar='tugatir', score=210)"
        assert repr(self.cmp.alignments('sit', 'sedere', top_n=1)[0]) == "Alignment(src='sit---', tar='sedere', score=220)"

        assert repr(self.cmp.alignments('doter', 'tugatir', top_n=0)) == "[Alignment(src='--doter', tar='tugatir', score=210), Alignment(src='do--ter', tar='tugatir', score=210), Alignment(src='d--oter', tar='tugatir', score=210)]"
        assert repr(self.cmp.alignments('sit', 'sed')) == "[Alignment(src='sit', tar='sed', score=90), Alignment(src='s-it', tar='sed-', score=200), Alignment(src='sit-', tar='s-ed', score=200), Alignment(src='--sit', tar='sed--', score=240), Alignment(src='sit--', tar='--sed', score=240), Alignment(src='-sit', tar='se-d', score=260), Alignment(src='si-t', tar='-sed', score=260), Alignment(src='-sit', tar='sed-', score=300), Alignment(src='sit-', tar='-sed', score=300)]"
        assert repr(self.cmp.alignments('sit', 'sīt', top_n=1)[0]) == "Alignment(src='sit', tar='sīt', score=10)"

    def test_covington_alignment(self):
        """Test abydos.distance.Covington.alignment."""
        assert self.cmp.alignment('doter', 'tugatir') == (210, '--doter', 'tugatir')
        assert self.cmp.alignment('sit', 'sedere') == (220, 'sit---', 'sedere')
        assert self.cmp.alignment('sit', 'sed') == (90, 'sit', 'sed')
        assert self.cmp.alignment('sit', 'sīt') == (10, 'sit', 'sīt')
