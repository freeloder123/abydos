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

"""abydos.tests.stats.test_stats_pairwise.

This module contains unit tests for abydos.stats pairwise functions
"""


import pytest

from abydos.distance import Jaccard, JaroWinkler
from abydos.stats import (
    amean,
    gmean,
    hmean,
    mean_pairwise_similarity,
    pairwise_similarity_statistics,
)

NIALL = (
    'Niall',
    'Neal',
    'Neil',
    'Njall',
    'Njáll',
    'Nigel',
    'Neel',
    'Nele',
    'Nigelli',
    'Nel',
    'Kneale',
    'Uí Néill',
    "O'Neill",
    'MacNeil',
    'MacNele',
    'Niall Noígíallach',
)

NIALL_1WORD = (
    'Niall',
    'Neal',
    'Neil',
    'Njall',
    'Njáll',
    'Nigel',
    'Neel',
    'Nele',
    'Nigelli',
    'Nel',
    'Kneale',
    "O'Neill",
    'MacNeil',
    'MacNele',
)


def test_mean_pairwise_similarity():
    """Test abydos.stats.mean_pairwise_similarity."""
    assert mean_pairwise_similarity(NIALL) == pytest.approx(abs=1e-7, expected=0.29362587170180671)
    assert mean_pairwise_similarity(NIALL, symmetric=True) == pytest.approx(abs=1e-7, expected=0.2936258717018066)
    assert mean_pairwise_similarity(NIALL, mean_func=hmean) == pytest.approx(abs=1e-7, expected=0.29362587170180671)
    assert mean_pairwise_similarity(NIALL, mean_func=hmean, symmetric=True) == pytest.approx(abs=1e-7, expected=0.2936258717018066)
    assert mean_pairwise_similarity(NIALL, mean_func=gmean) == pytest.approx(abs=1e-7, expected=0.33747245800668441)
    assert mean_pairwise_similarity(NIALL, mean_func=gmean, symmetric=True) == pytest.approx(abs=1e-7, expected=0.33747245800668441)
    assert mean_pairwise_similarity(NIALL, mean_func=amean) == pytest.approx(abs=1e-7, expected=0.38009278711484601)
    assert mean_pairwise_similarity(NIALL, mean_func=amean, symmetric=True) == pytest.approx(abs=1e-7, expected=0.38009278711484623)

    assert (
        mean_pairwise_similarity(NIALL_1WORD)
        == mean_pairwise_similarity(' '.join(NIALL_1WORD))
    )
    assert (
        mean_pairwise_similarity(NIALL_1WORD, symmetric=True)
        == mean_pairwise_similarity(' '.join(NIALL_1WORD), symmetric=True)
    )
    assert (
        mean_pairwise_similarity(NIALL_1WORD, mean_func=gmean)
        == mean_pairwise_similarity(' '.join(NIALL_1WORD), mean_func=gmean)
    )
    assert (
        mean_pairwise_similarity(NIALL_1WORD, mean_func=amean)
        == mean_pairwise_similarity(' '.join(NIALL_1WORD), mean_func=amean)
    )

    with pytest.raises(ValueError):
        mean_pairwise_similarity(['a b c'])
    with pytest.raises(ValueError):
        mean_pairwise_similarity('abc')
    with pytest.raises(ValueError):
        mean_pairwise_similarity(0)
    with pytest.raises(ValueError):
        mean_pairwise_similarity(NIALL, mean_func='imaginary')
    with pytest.raises(ValueError):
        mean_pairwise_similarity(NIALL, metric='imaginary')

    assert (
        mean_pairwise_similarity(NIALL)
        == mean_pairwise_similarity(tuple(NIALL))
    )
    assert (
        mean_pairwise_similarity(NIALL)
        == mean_pairwise_similarity(list(NIALL))
    )
    assert mean_pairwise_similarity(NIALL) == pytest.approx(abs=1e-7, expected=mean_pairwise_similarity(sorted(NIALL)))
    assert mean_pairwise_similarity(NIALL) == pytest.approx(abs=1e-7, expected=mean_pairwise_similarity(set(NIALL)))


def test_pairwise_similarity_statistics():
    """Test abydos.stats.pairwise_similarity_statistics."""
    (pw_max, pw_min, pw_mean, pw_std) = pairwise_similarity_statistics(
        NIALL, NIALL
    )
    assert pw_max == pytest.approx(abs=1e-7, expected=1.0)
    assert pw_min == pytest.approx(abs=1e-7, expected=0.11764705882352944)
    assert pw_mean == pytest.approx(abs=1e-7, expected=0.4188369879201684)
    assert pw_std == pytest.approx(abs=1e-7, expected=0.2265099631340623)

    (pw_max, pw_min, pw_mean, pw_std) = pairwise_similarity_statistics(
        NIALL, ('Kneal',)
    )
    assert pw_max == pytest.approx(abs=1e-7, expected=0.8333333333333334)
    assert pw_min == pytest.approx(abs=1e-7, expected=0.11764705882352944)
    assert pw_mean == pytest.approx(abs=1e-7, expected=0.30474877450980387)
    assert pw_std == pytest.approx(abs=1e-7, expected=0.1842666797571549)

    # Test symmetric
    (pw_max, pw_min, pw_mean, pw_std) = pairwise_similarity_statistics(
        NIALL, NIALL, symmetric=True
    )
    assert pw_max == pytest.approx(abs=1e-7, expected=1.0)
    assert pw_min == pytest.approx(abs=1e-7, expected=0.11764705882352944)
    assert pw_mean == pytest.approx(abs=1e-7, expected=0.4188369879201679)
    assert pw_std == pytest.approx(abs=1e-7, expected=0.22650996313406255)

    (pw_max, pw_min, pw_mean, pw_std) = pairwise_similarity_statistics(
        NIALL, ('Kneal',), symmetric=True
    )
    assert pw_max == pytest.approx(abs=1e-7, expected=0.8333333333333334)
    assert pw_min == pytest.approx(abs=1e-7, expected=0.11764705882352944)
    assert pw_mean == pytest.approx(abs=1e-7, expected=0.304748774509804)
    assert pw_std == pytest.approx(abs=1e-7, expected=0.18426667975715486)

    # Test with splittable strings
    (pw_max, pw_min, pw_mean, pw_std) = pairwise_similarity_statistics(
        'The quick brown fox', 'jumped over the lazy dog.'
    )
    assert pw_max == pytest.approx(abs=1e-7, expected=0.6666666666666667)
    assert pw_min == pytest.approx(abs=1e-7, expected=0.0)
    assert pw_mean == pytest.approx(abs=1e-7, expected=0.08499999999999999)
    assert pw_std == pytest.approx(abs=1e-7, expected=0.16132265804901677)

    (pw_max, pw_min, pw_mean, pw_std) = pairwise_similarity_statistics(
        'The', 'jumped'
    )
    assert pw_max == pytest.approx(abs=1e-7, expected=0.16666666666666663)
    assert pw_min == pytest.approx(abs=1e-7, expected=0.16666666666666663)
    assert pw_mean == pytest.approx(abs=1e-7, expected=0.16666666666666663)
    assert pw_std == pytest.approx(abs=1e-7, expected=0.0)

    # Test with a set metric
    (pw_max, pw_min, pw_mean, pw_std) = pairwise_similarity_statistics(
        NIALL, NIALL, metric=Jaccard().sim
    )
    assert pw_max == pytest.approx(abs=1e-7, expected=1.0)
    assert pw_min == pytest.approx(abs=1e-7, expected=0.0)
    assert pw_mean == pytest.approx(abs=1e-7, expected=0.23226906681010506)
    assert pw_std == pytest.approx(abs=1e-7, expected=0.24747101181262784)

    (pw_max, pw_min, pw_mean, pw_std) = pairwise_similarity_statistics(
        NIALL, NIALL, metric=JaroWinkler().dist
    )
    assert pw_max == pytest.approx(abs=1e-7, expected=1.0)
    assert pw_min == pytest.approx(abs=1e-7, expected=0.0)
    assert pw_mean == pytest.approx(abs=1e-7, expected=0.3352660334967324)
    assert pw_std == pytest.approx(abs=1e-7, expected=0.18394505847524578)

    # Test using hmean'
    (pw_max, pw_min, pw_mean, pw_std) = pairwise_similarity_statistics(
        NIALL, NIALL, mean_func=hmean
    )
    assert pw_max == pytest.approx(abs=1e-7, expected=1.0)
    assert pw_min == pytest.approx(abs=1e-7, expected=0.11764705882352944)
    assert pw_mean == pytest.approx(abs=1e-7, expected=0.30718771249150056)
    assert pw_std == pytest.approx(abs=1e-7, expected=0.25253182790044676)

    # Test exceptions
    with pytest.raises(ValueError):
        pairwise_similarity_statistics(NIALL, NIALL, mean_func='mean')
    with pytest.raises(ValueError):
        pairwise_similarity_statistics(NIALL, NIALL, metric='Levenshtein')
    with pytest.raises(ValueError):
        pairwise_similarity_statistics(5, NIALL)
    with pytest.raises(ValueError):
        pairwise_similarity_statistics(NIALL, 5)
