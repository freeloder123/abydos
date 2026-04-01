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

"""abydos.tests.stats.test_stats_mean.

This module contains unit tests for abydos.stats mean functions
"""

import pytest

from math import isnan

from abydos.stats import (
    aghmean,
    agmean,
    amean,
    cmean,
    ghmean,
    gmean,
    heronian_mean,
    hmean,
    hoelder_mean,
    imean,
    lehmer_mean,
    lmean,
    median,
    midrange,
    mode,
    qmean,
    seiffert_mean,
    std,
    var,
)


class TestMeans:
    """Test abydos.stats mean functions."""

    _ones = [1, 1, 1, 1, 1]
    _zeros = [0, 0, 0, 0, 0]
    _one_to_five = [1, 2, 3, 4, 5]
    _onethreefive = [1, 1, 3, 5, 5]
    _floats = [0.5, 0.8, 0.1, 0.2, 0.25]
    _has_inf = [0, 1, 2, float('inf')]
    _2ones = [1, 1]
    _2zeros = [0, 0]
    _onetwo = [1, 2]
    _2floats = [0.5, 0.25]

    def test_means_amean(self):
        """Test abydos.stats.amean."""
        assert amean(self._ones) == pytest.approx(abs=1e-7, expected=1)
        assert amean(self._zeros) == pytest.approx(abs=1e-7, expected=0)
        assert amean(self._one_to_five) == pytest.approx(abs=1e-7, expected=3)
        assert amean(self._onethreefive) == pytest.approx(abs=1e-7, expected=3)
        assert amean(self._floats) == pytest.approx(abs=1e-7, expected=0.37)

    def test_means_gmean(self):
        """Test abydos.stats.gmean."""
        assert gmean(self._ones) == pytest.approx(abs=1e-7, expected=1)
        assert gmean(self._zeros) == pytest.approx(abs=1e-7, expected=0)
        assert gmean(self._one_to_five) == pytest.approx(abs=1e-7, expected=2.605171084697352)
        assert gmean(self._onethreefive) == pytest.approx(abs=1e-7, expected=2.3714406097793117)
        assert gmean(self._floats) == pytest.approx(abs=1e-7, expected=0.2885399811814427)

    def test_means_hmean(self):
        """Test abydos.stats.hmean."""
        assert hmean(self._ones) == pytest.approx(abs=1e-7, expected=1)
        assert hmean(self._zeros) == pytest.approx(abs=1e-7, expected=0)
        assert hmean(self._one_to_five) == pytest.approx(abs=1e-7, expected=2.18978102189781)
        assert hmean(self._onethreefive) == pytest.approx(abs=1e-7, expected=1.8292682926829265)
        assert hmean(self._floats) == pytest.approx(abs=1e-7, expected=0.2247191011235955)
        assert hmean([0, 1, 2]) == 0
        assert hmean([1, 2, 3, 0]) == 0
        assert isnan(hmean([0, 0, 1, 2]))
        assert isnan(hmean([1, 0, 2, 0, 3]))
        assert isnan(hmean([1, 0, 2, 0, 3, 0]))
        assert isnan(hmean([1, 0, 2, 0, 3, 0, 0]))
        assert hmean([0, 0]) == 0
        assert hmean([5, 5, 5, 5, 5]) == 5
        assert hmean([0]) == 0
        assert hmean([8]) == 8
        with pytest.raises(ValueError):
            hmean(([]))

    def test_means_qmean(self):
        """Test abydos.stats.qmean."""
        assert qmean(self._ones) == pytest.approx(abs=1e-7, expected=1)
        assert qmean(self._zeros) == pytest.approx(abs=1e-7, expected=0)
        assert qmean(self._one_to_five) == pytest.approx(abs=1e-7, expected=3.3166247903554)
        assert qmean(self._onethreefive) == pytest.approx(abs=1e-7, expected=3.492849839314596)
        assert qmean(self._floats) == pytest.approx(abs=1e-7, expected=0.4477722635447623)

    def test_means_cmean(self):
        """Test abydos.stats.cmean."""
        assert cmean(self._ones) == pytest.approx(abs=1e-7, expected=1)
        assert cmean(self._one_to_five) == pytest.approx(abs=1e-7, expected=3.6666666666666665)
        assert cmean(self._onethreefive) == pytest.approx(abs=1e-7, expected=4.066666666666666)
        assert cmean(self._floats) == pytest.approx(abs=1e-7, expected=0.5418918918918919)

    def test_means_lmean(self):
        """Test abydos.stats.lmean."""
        assert lmean(self._one_to_five) == pytest.approx(abs=1e-7, expected=2.6739681320855766)
        assert lmean(self._floats) == pytest.approx(abs=1e-7, expected=0.301387278840469)
        assert lmean([1, 1]) == 1.0
        assert lmean([2, 2]) == 2.0
        assert lmean([2, 0]) == 0.0
        assert lmean([1, 2]) == pytest.approx(abs=1e-7, expected=1.4426950408889634)
        with pytest.raises(ValueError):
            lmean((1, 1, 1))
        with pytest.raises(ValueError):
            lmean((0.15, 0.15, 1))

    def test_means_imean(self):
        """Test abydos.stats.imean."""
        with pytest.raises(ValueError):
            imean(self._ones)
        with pytest.raises(ValueError):
            imean(self._zeros)
        with pytest.raises(ValueError):
            imean(self._one_to_five)
        with pytest.raises(ValueError):
            imean(self._onethreefive)
        with pytest.raises(ValueError):
            imean(self._floats)
        assert imean(self._2ones) == pytest.approx(abs=1e-7, expected=1)
        assert isnan(imean(self._2zeros))
        assert imean(self._onetwo) == pytest.approx(abs=1e-7, expected=1.4715177646857693)
        assert imean(self._2floats) == pytest.approx(abs=1e-7, expected=0.36787944117144233)
        assert imean([1]) == 1
        assert imean([0.05]) == 0.05

    def test_means_seiffert_mean(self):
        """Test abydos.stats.seiffert_mean."""
        with pytest.raises(ValueError):
            seiffert_mean(self._ones)
        with pytest.raises(ValueError):
            seiffert_mean(self._zeros)
        with pytest.raises(ValueError):
            seiffert_mean(self._one_to_five)
        with pytest.raises(ValueError):
            seiffert_mean(self._onethreefive)
        with pytest.raises(ValueError):
            seiffert_mean(self._floats)
        assert seiffert_mean(self._onetwo) == pytest.approx(abs=1e-7, expected=1.4712939827611637)
        assert seiffert_mean(self._2floats) == pytest.approx(abs=1e-7, expected=0.36782349569029094)
        assert seiffert_mean([1]) == 1
        assert seiffert_mean([0.05]) == 0.05
        assert isnan(seiffert_mean([1, 1]))

    def test_means_lehmer_mean(self):
        """Test abydos.stats.lehmer_mean."""
        assert lehmer_mean(self._ones) == pytest.approx(abs=1e-7, expected=1)
        assert lehmer_mean(self._one_to_five) == pytest.approx(abs=1e-7, expected=3.6666666666666665)
        assert lehmer_mean(self._onethreefive) == pytest.approx(abs=1e-7, expected=4.066666666666666)
        assert lehmer_mean(self._floats) == pytest.approx(abs=1e-7, expected=0.5418918918918919)

    def test_means_heronian_mean(self):
        """Test abydos.stats.heronian_mean."""
        assert heronian_mean(self._ones) == pytest.approx(abs=1e-7, expected=1)
        assert heronian_mean(self._zeros) == pytest.approx(abs=1e-7, expected=0)
        assert heronian_mean(self._one_to_five) == pytest.approx(abs=1e-7, expected=2.8421165194322837)
        assert heronian_mean(self._onethreefive) == pytest.approx(abs=1e-7, expected=2.7436226811701165)
        assert heronian_mean(self._floats) == pytest.approx(abs=1e-7, expected=0.33526945542427006)

    def test_means_hoelder_mean(self):
        """Test abydos.stats.hoelder_mean."""
        assert hoelder_mean(self._ones) == pytest.approx(abs=1e-7, expected=1)
        assert hoelder_mean(self._zeros) == pytest.approx(abs=1e-7, expected=0)
        assert hoelder_mean(self._one_to_five) == pytest.approx(abs=1e-7, expected=3.3166247903554)
        assert hoelder_mean(self._onethreefive) == pytest.approx(abs=1e-7, expected=3.492849839314596)
        assert hoelder_mean(self._floats) == pytest.approx(abs=1e-7, expected=0.4477722635447623)
        assert hoelder_mean(self._floats, 0) == pytest.approx(abs=1e-7, expected=gmean(self._floats))

    def test_means_agmean(self):
        """Test abydos.stats.agmean."""
        assert agmean(self._ones) == pytest.approx(abs=1e-7, expected=1)
        assert agmean(self._zeros) == pytest.approx(abs=1e-7, expected=0)
        assert agmean(self._one_to_five) == pytest.approx(abs=1e-7, expected=2.799103662640505)
        assert agmean(self._onethreefive) == pytest.approx(abs=1e-7, expected=2.6764865062631356)
        assert agmean(self._floats) == pytest.approx(abs=1e-7, expected=0.32800436242611486)
        assert isnan(agmean(self._has_inf))

    def test_means_ghmean(self):
        """Test abydos.stats.ghmean."""
        assert ghmean(self._ones) == pytest.approx(abs=1e-7, expected=1)
        assert ghmean(self._one_to_five) == pytest.approx(abs=1e-7, expected=2.3839666656453167)
        assert ghmean(self._onethreefive) == pytest.approx(abs=1e-7, expected=2.0740491019412035)
        assert ghmean(self._floats) == pytest.approx(abs=1e-7, expected=0.2536468771476393)
        assert isnan(ghmean(self._has_inf))

    def test_means_aghmean(self):
        """Test abydos.stats.aghmean."""
        assert aghmean(self._ones) == pytest.approx(abs=1e-7, expected=1)
        assert aghmean(self._one_to_five) == pytest.approx(abs=1e-7, expected=2.5769530579812563)
        assert aghmean(self._onethreefive) == pytest.approx(abs=1e-7, expected=2.3520502484275387)
        assert aghmean(self._floats) == pytest.approx(abs=1e-7, expected=0.28841285333045547)
        assert isnan(aghmean(self._has_inf))

    def test_means_midrange(self):
        """Test abydos.stats.midrange."""
        assert midrange(self._ones) == pytest.approx(abs=1e-7, expected=1)
        assert midrange(self._zeros) == pytest.approx(abs=1e-7, expected=0)
        assert midrange(self._one_to_five) == pytest.approx(abs=1e-7, expected=3)
        assert midrange(self._onethreefive) == pytest.approx(abs=1e-7, expected=3)
        assert midrange(self._floats) == pytest.approx(abs=1e-7, expected=0.45)

    def test_means_median(self):
        """Test abydos.stats.median."""
        assert median(self._ones) == pytest.approx(abs=1e-7, expected=1)
        assert median(self._zeros) == pytest.approx(abs=1e-7, expected=0)
        assert median(self._one_to_five) == pytest.approx(abs=1e-7, expected=3)
        assert median(self._onethreefive) == pytest.approx(abs=1e-7, expected=3)
        assert median(self._floats) == pytest.approx(abs=1e-7, expected=0.25)
        assert median([0, 2, 4, 8]) == pytest.approx(abs=1e-7, expected=3)
        assert median([0.01, 0.2, 0.4, 5]) == pytest.approx(abs=1e-7, expected=0.3)

    def test_means_mode(self):
        """Test abydos.stats.mode."""
        assert mode(self._ones) == 1
        assert mode(self._zeros) == 0
        assert mode([1, 1, 2, 2, 2]) == 2
        assert mode([1, 5, 5, 2, 5, 2]) == 5

    def test_means_var(self):
        """Test abydos.stats.var."""
        assert var(self._ones) == pytest.approx(abs=1e-7, expected=0)
        assert var(self._zeros) == pytest.approx(abs=1e-7, expected=0)
        assert var(self._one_to_five) == pytest.approx(abs=1e-7, expected=2)
        assert var(self._onethreefive) == pytest.approx(abs=1e-7, expected=3.2)

    def test_means_std(self):
        """Test abydos.stats.std."""
        assert std(self._ones) == pytest.approx(abs=1e-7, expected=0)
        assert std(self._zeros) == pytest.approx(abs=1e-7, expected=0)
        assert std(self._one_to_five) == pytest.approx(abs=1e-7, expected=2 ** 0.5)
        assert std(self._onethreefive) == pytest.approx(abs=1e-7, expected=3.2 ** 0.5)
