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

"""abydos.tests.distance.test_distance_lcsseq.

This module contains unit tests for abydos.distance.LCSseq
"""


import pytest

from abydos.distance import LCSseq


cmp = LCSseq()


def test_lcsseq():
    """Test abydos.distance.LCSseq.lcsseq."""
    assert cmp.lcsseq('', '') == ''
    assert cmp.lcsseq('A', '') == ''
    assert cmp.lcsseq('', 'A') == ''
    assert cmp.lcsseq('A', 'A') == 'A'
    assert cmp.lcsseq('ABCD', '') == ''
    assert cmp.lcsseq('', 'ABCD') == ''
    assert cmp.lcsseq('ABCD', 'ABCD') == 'ABCD'
    assert cmp.lcsseq('ABCD', 'BC') == 'BC'
    assert cmp.lcsseq('ABCD', 'AD') == 'AD'
    assert cmp.lcsseq('ABCD', 'AC') == 'AC'
    assert cmp.lcsseq('AB', 'CD') == ''
    assert cmp.lcsseq('ABC', 'BCD') == 'BC'

    assert cmp.lcsseq('DIXON', 'DICKSONX') == 'DION'

    # https://en.wikipedia.org/wiki/Longest_common_subsequence_problem
    assert cmp.lcsseq('AGCAT', 'GAC') == 'AC'
    assert cmp.lcsseq('XMJYAUZ', 'MZJAWXU') == 'MJAU'

    # https://github.com/jwmerrill/factor/blob/master/basis/lcs/lcs-tests.factor
    assert cmp.lcsseq('hell', 'hello') == 'hell'
    assert cmp.lcsseq('hello', 'hell') == 'hell'
    assert cmp.lcsseq('ell', 'hell') == 'ell'
    assert cmp.lcsseq('hell', 'ell') == 'ell'
    assert cmp.lcsseq('faxbcd', 'abdef') == 'abd'

    # http://www.unesco.org/culture/languages-atlas/assets/_core/php/qcubed_unit_tests.php
    assert cmp.lcsseq('hello world', 'world war 2') == 'world'
    assert cmp.lcsseq('foo bar', 'bar foo') == 'foo'
    assert cmp.lcsseq('aaa', 'aa') == 'aa'
    assert cmp.lcsseq('cc', 'bbbbcccccc') == 'cc'
    assert cmp.lcsseq('ccc', 'bcbb') == 'c'

def test_lcsseq_sim():
    """Test abydos.distance.LCSseq.sim."""
    assert cmp.sim('', '') == 1
    assert cmp.sim('A', '') == 0
    assert cmp.sim('', 'A') == 0
    assert cmp.sim('A', 'A') == 1
    assert cmp.sim('ABCD', '') == 0
    assert cmp.sim('', 'ABCD') == 0
    assert cmp.sim('ABCD', 'ABCD') == 1
    assert cmp.sim('ABCD', 'BC') == pytest.approx(abs=1e-7, expected=2 / 4)
    assert cmp.sim('ABCD', 'AD') == pytest.approx(abs=1e-7, expected=2 / 4)
    assert cmp.sim('ABCD', 'AC') == pytest.approx(abs=1e-7, expected=2 / 4)
    assert cmp.sim('AB', 'CD') == pytest.approx(abs=1e-7, expected=0)
    assert cmp.sim('ABC', 'BCD') == pytest.approx(abs=1e-7, expected=2 / 3)

    assert cmp.sim('DIXON', 'DICKSONX') == pytest.approx(abs=1e-7, expected=4 / 8)

    # https://en.wikipedia.org/wiki/Longest_common_subsequence_problem
    assert cmp.sim('AGCAT', 'GAC') == pytest.approx(abs=1e-7, expected=2 / 5)
    assert cmp.sim('XMJYAUZ', 'MZJAWXU') == pytest.approx(abs=1e-7, expected=4 / 7)

    # https://github.com/jwmerrill/factor/blob/master/basis/lcs/lcs-tests.factor
    assert cmp.sim('hell', 'hello') == pytest.approx(abs=1e-7, expected=4 / 5)
    assert cmp.sim('hello', 'hell') == pytest.approx(abs=1e-7, expected=4 / 5)
    assert cmp.sim('ell', 'hell') == pytest.approx(abs=1e-7, expected=3 / 4)
    assert cmp.sim('hell', 'ell') == pytest.approx(abs=1e-7, expected=3 / 4)
    assert cmp.sim('faxbcd', 'abdef') == pytest.approx(abs=1e-7, expected=3 / 6)

    # http://www.unesco.org/culture/languages-atlas/assets/_core/php/qcubed_unit_tests.php
    assert cmp.sim('hello world', 'world war 2') == pytest.approx(abs=1e-7, expected=5 / 11)
    assert cmp.sim('foo bar', 'bar foo') == pytest.approx(abs=1e-7, expected=3 / 7)
    assert cmp.sim('aaa', 'aa') == pytest.approx(abs=1e-7, expected=2 / 3)
    assert cmp.sim('cc', 'bbbbcccccc') == pytest.approx(abs=1e-7, expected=2 / 10)
    assert cmp.sim('ccc', 'bcbb') == pytest.approx(abs=1e-7, expected=1 / 4)

def test_lcsseq_dist():
    """Test abydos.distance.LCSseq.dist."""
    assert cmp.dist('', '') == 0
    assert cmp.dist('A', '') == 1
    assert cmp.dist('', 'A') == 1
    assert cmp.dist('A', 'A') == 0
    assert cmp.dist('ABCD', '') == 1
    assert cmp.dist('', 'ABCD') == 1
    assert cmp.dist('ABCD', 'ABCD') == 0
    assert cmp.dist('ABCD', 'BC') == pytest.approx(abs=1e-7, expected=2 / 4)
    assert cmp.dist('ABCD', 'AD') == pytest.approx(abs=1e-7, expected=2 / 4)
    assert cmp.dist('ABCD', 'AC') == pytest.approx(abs=1e-7, expected=2 / 4)
    assert cmp.dist('AB', 'CD') == pytest.approx(abs=1e-7, expected=1)
    assert cmp.dist('ABC', 'BCD') == pytest.approx(abs=1e-7, expected=1 / 3)

    assert cmp.dist('DIXON', 'DICKSONX') == pytest.approx(abs=1e-7, expected=4 / 8)

    # https://en.wikipedia.org/wiki/Longest_common_subsequence_problem
    assert cmp.dist('AGCAT', 'GAC') == pytest.approx(abs=1e-7, expected=3 / 5)
    assert cmp.dist('XMJYAUZ', 'MZJAWXU') == pytest.approx(abs=1e-7, expected=3 / 7)

    # https://github.com/jwmerrill/factor/blob/master/basis/lcs/lcs-tests.factor
    assert cmp.dist('hell', 'hello') == pytest.approx(abs=1e-7, expected=1 / 5)
    assert cmp.dist('hello', 'hell') == pytest.approx(abs=1e-7, expected=1 / 5)
    assert cmp.dist('ell', 'hell') == pytest.approx(abs=1e-7, expected=1 / 4)
    assert cmp.dist('hell', 'ell') == pytest.approx(abs=1e-7, expected=1 / 4)
    assert cmp.dist('faxbcd', 'abdef') == pytest.approx(abs=1e-7, expected=3 / 6)

    # http://www.unesco.org/culture/languages-atlas/assets/_core/php/qcubed_unit_tests.php
    assert cmp.dist('hello world', 'world war 2') == pytest.approx(abs=1e-7, expected=6 / 11)
    assert cmp.dist('foo bar', 'bar foo') == pytest.approx(abs=1e-7, expected=4 / 7)
    assert cmp.dist('aaa', 'aa') == pytest.approx(abs=1e-7, expected=1 / 3)
    assert cmp.dist('cc', 'bbbbcccccc') == pytest.approx(abs=1e-7, expected=8 / 10)
    assert cmp.dist('ccc', 'bcbb') == pytest.approx(abs=1e-7, expected=3 / 4)
