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

"""abydos.tests.stats.test_stats_confusion_table.

This module contains unit tests for abydos.stats.ConfusionTable
"""

import pytest

from math import isnan, sqrt

from abydos.stats import ConfusionTable


UNIT_TABLE = ConfusionTable(1, 1, 1, 1)
NULL_TABLE = ConfusionTable(0, 0, 0, 0)
SCALE_TABLE = ConfusionTable(1, 2, 3, 4)
# https://en.wikipedia.org/wiki/Confusion_matrix#Table_of_confusion
CATSNDOGS_TABLE = ConfusionTable(5, 17, 2, 3)
# https://en.wikipedia.org/wiki/Sensitivity_and_specificity#Worked_example
WORKED_EG_TABLE = ConfusionTable(20, 1820, 180, 10)
VERY_POOR_TABLE = ConfusionTable(0, 0, 200, 200)

ALL_TABLES = (
    UNIT_TABLE,
    NULL_TABLE,
    SCALE_TABLE,
    CATSNDOGS_TABLE,
    WORKED_EG_TABLE,
    VERY_POOR_TABLE,
)

# def ct2arrays(ct):
#     y_pred = []
#     y_true = []
#     y_pred += [1]*ct.tpos
#     y_true += [1]*ct.tpos
#     y_pred += [0]*ct.tneg
#     y_true += [0]*ct.tneg
#     y_pred += [1]*ct.fpos
#     y_true += [0]*ct.fpos
#     y_pred += [0]*ct.fneg
#     y_true += [1]*ct.fneg
#     return y_pred, y_true


def test_constructors():
    """Test abydos.stats.ConfusionTable constructors."""
    assert ConfusionTable() == ConfusionTable()
    assert ConfusionTable() == ConfusionTable(0)
    assert ConfusionTable() == ConfusionTable(0, 0)
    assert ConfusionTable() == ConfusionTable(0, 0, 0)
    assert ConfusionTable() == ConfusionTable(0, 0, 0, 0)
    assert ConfusionTable() != ConfusionTable(1)
    assert ConfusionTable() != ConfusionTable(0, 1)
    assert ConfusionTable() != ConfusionTable(0, 0, 1)
    assert ConfusionTable() != ConfusionTable(0, 0, 0, 1)

    # test int constructor & __eq__ by value
    assert SCALE_TABLE == ConfusionTable(1, 2, 3, 4)
    # test tuple constructor
    assert SCALE_TABLE == ConfusionTable((1, 2, 3, 4))
    assert SCALE_TABLE == ConfusionTable((1, 2, 3, 4), 5, 6, 7)
    # test list constructor
    assert SCALE_TABLE == ConfusionTable([1, 2, 3, 4])
    assert SCALE_TABLE == ConfusionTable([1, 2, 3, 4], 5, 6, 7)
    # test dict constructor
    assert SCALE_TABLE == ConfusionTable({'tp': 1, 'tn': 2, 'fp': 3, 'fn': 4})
    assert (
        SCALE_TABLE
        == ConfusionTable({'tp': 1, 'tn': 2, 'fp': 3, 'fn': 4}, 5, 6, 7)
    )
    assert NULL_TABLE == ConfusionTable({})
    assert NULL_TABLE == ConfusionTable({'pt': 1, 'nt': 2, 'pf': 3, 'nf': 4})

    # test __eq__ by id()
    assert SCALE_TABLE == SCALE_TABLE
    assert not CATSNDOGS_TABLE == SCALE_TABLE
    # test __eq__ by tuple
    assert SCALE_TABLE == (1, 2, 3, 4)
    assert not CATSNDOGS_TABLE == (1, 2, 3, 4)
    # test __eq__ by list
    assert SCALE_TABLE == [1, 2, 3, 4]
    assert not CATSNDOGS_TABLE == [1, 2, 3, 4]
    # test __eq__ by dict
    assert SCALE_TABLE == {'tp': 1, 'tn': 2, 'fp': 3, 'fn': 4}
    assert not (CATSNDOGS_TABLE == {'tp': 1, 'tn': 2, 'fp': 3, 'fn': 4})
    # test __eq__ with non-ConfusionTable/tuple/list/dict
    assert not SCALE_TABLE == 5

    # test invalid tuple constructor
    with pytest.raises(AttributeError):
        ConfusionTable((1, 2))


def test_to_tuple():
    """Test abydos.stats.ConfusionTable.to_tuple."""
    assert isinstance(SCALE_TABLE.to_tuple(), tuple)
    assert SCALE_TABLE.to_tuple() == (1, 2, 3, 4)
    assert list(SCALE_TABLE.to_tuple()) == [1, 2, 3, 4]

def test_to_dict():
    """Test abydos.stats.ConfusionTable.to_dict."""
    assert isinstance(SCALE_TABLE.to_dict(), dict)
    assert SCALE_TABLE.to_dict() == {'tp': 1, 'tn': 2, 'fp': 3, 'fn': 4}

def test_str():
    """Test abydos.stats.ConfusionTable._str_."""
    assert isinstance(str(SCALE_TABLE), str)
    assert str(SCALE_TABLE) == 'tp:1, tn:2, fp:3, fn:4'

def test_repr():
    """Test abydos.stats.ConfusionTable._repr_."""
    assert isinstance(repr(SCALE_TABLE), str)
    assert repr(SCALE_TABLE) == 'ConfusionTable(tp=1, tn=2, fp=3, fn=4)'


def test_correct_pop():
    """Test abydos.stats.ConfusionTable.correct_pop."""
    assert UNIT_TABLE.correct_pop() == 2
    assert NULL_TABLE.correct_pop() == 0
    assert SCALE_TABLE.correct_pop() == 3
    assert CATSNDOGS_TABLE.correct_pop() == 22
    assert WORKED_EG_TABLE.correct_pop() == 1840

def test_error_pop():
    """Test abydos.stats.ConfusionTable.error_pop."""
    assert UNIT_TABLE.error_pop() == 2
    assert NULL_TABLE.error_pop() == 0
    assert SCALE_TABLE.error_pop() == 7
    assert CATSNDOGS_TABLE.error_pop() == 5
    assert WORKED_EG_TABLE.error_pop() == 190

def test_pred_pos_pop():
    """Test abydos.stats.ConfusionTable.pred_pos_pop."""
    assert UNIT_TABLE.pred_pos_pop() == 2
    assert NULL_TABLE.pred_pos_pop() == 0
    assert SCALE_TABLE.pred_pos_pop() == 4
    assert CATSNDOGS_TABLE.pred_pos_pop() == 7
    assert WORKED_EG_TABLE.pred_pos_pop() == 200

def test_pred_neg_pop():
    """Test abydos.stats.ConfusionTable.pred_neg_pop."""
    assert UNIT_TABLE.pred_neg_pop() == 2
    assert NULL_TABLE.pred_neg_pop() == 0
    assert SCALE_TABLE.pred_neg_pop() == 6
    assert CATSNDOGS_TABLE.pred_neg_pop() == 20
    assert WORKED_EG_TABLE.pred_neg_pop() == 1830

def test_cond_pos_pop():
    """Test abydos.stats.ConfusionTable.cond_pos_pop."""
    assert UNIT_TABLE.cond_pos_pop() == 2
    assert NULL_TABLE.cond_pos_pop() == 0
    assert SCALE_TABLE.cond_pos_pop() == 5
    assert CATSNDOGS_TABLE.cond_pos_pop() == 8
    assert WORKED_EG_TABLE.cond_pos_pop() == 30

def test_cond_neg_pop():
    """Test abydos.stats.ConfusionTable.cond_neg_pop."""
    assert UNIT_TABLE.cond_neg_pop() == 2
    assert NULL_TABLE.cond_neg_pop() == 0
    assert SCALE_TABLE.cond_neg_pop() == 5
    assert CATSNDOGS_TABLE.cond_neg_pop() == 19
    assert WORKED_EG_TABLE.cond_neg_pop() == 2000

def test_population():
    """Test abydos.stats.ConfusionTable.population."""
    assert UNIT_TABLE.population() == 4
    assert NULL_TABLE.population() == 0
    assert SCALE_TABLE.population() == 10
    assert CATSNDOGS_TABLE.population() == 27
    assert WORKED_EG_TABLE.population() == 2030


def test_precision():
    """Test abydos.stats.ConfusionTable.precision."""
    assert UNIT_TABLE.precision() == 0.5
    assert isnan(NULL_TABLE.precision())
    assert SCALE_TABLE.precision() == pytest.approx(abs=1e-7, expected=0.25)
    assert CATSNDOGS_TABLE.precision() == pytest.approx(abs=1e-7, expected=5 / 7)
    assert WORKED_EG_TABLE.precision() == pytest.approx(abs=1e-7, expected=0.1)

def test_precision_gain():
    """Test abydos.stats.ConfusionTable.precision_gain."""
    assert UNIT_TABLE.precision_gain() == 1
    assert isnan(NULL_TABLE.precision_gain())
    assert SCALE_TABLE.precision_gain() == pytest.approx(abs=1e-7, expected=0.25 / 0.5)
    assert CATSNDOGS_TABLE.precision_gain() == pytest.approx(abs=1e-7, expected=(5 / 7) / (8 / 27))
    assert WORKED_EG_TABLE.precision_gain() == pytest.approx(abs=1e-7, expected=0.1 / (30 / 2030))

def test_recall():
    """Test abydos.stats.ConfusionTable.recall."""
    assert UNIT_TABLE.recall() == 0.5
    assert isnan(NULL_TABLE.recall())
    assert SCALE_TABLE.recall() == pytest.approx(abs=1e-7, expected=0.2)
    assert CATSNDOGS_TABLE.recall() == pytest.approx(abs=1e-7, expected=5 / 8)
    assert WORKED_EG_TABLE.recall() == pytest.approx(abs=1e-7, expected=2 / 3)

def test_specificity():
    """Test abydos.stats.ConfusionTable.specificity."""
    assert UNIT_TABLE.specificity() == 0.5
    assert isnan(NULL_TABLE.specificity())
    assert SCALE_TABLE.specificity() == pytest.approx(abs=1e-7, expected=0.4)
    assert CATSNDOGS_TABLE.specificity() == pytest.approx(abs=1e-7, expected=17 / 19)
    assert WORKED_EG_TABLE.specificity() == pytest.approx(abs=1e-7, expected=0.91)

def test_fnr():
    """Test abydos.stats.ConfusionTable.fnr."""
    assert UNIT_TABLE.fnr() == 0.5
    assert isnan(NULL_TABLE.fnr())
    assert SCALE_TABLE.fnr() == pytest.approx(abs=1e-7, expected=0.8)
    assert CATSNDOGS_TABLE.fnr() == pytest.approx(abs=1e-7, expected=3 / 8)
    assert WORKED_EG_TABLE.fnr() == pytest.approx(abs=1e-7, expected=1 / 3)

def test_npv():
    """Test abydos.stats.ConfusionTable.npv."""
    assert UNIT_TABLE.npv() == 0.5
    assert isnan(NULL_TABLE.npv())
    assert SCALE_TABLE.npv() == pytest.approx(abs=1e-7, expected=1 / 3)
    assert CATSNDOGS_TABLE.npv() == pytest.approx(abs=1e-7, expected=17 / 20)
    assert WORKED_EG_TABLE.npv() == pytest.approx(abs=1e-7, expected=182 / 183)

def test_false_omission_rate():
    """Test abydos.stats.ConfusionTable.false_omission_rate."""
    assert UNIT_TABLE.false_omission_rate() == 0.5
    assert isnan(NULL_TABLE.false_omission_rate())
    assert SCALE_TABLE.false_omission_rate() == pytest.approx(abs=1e-7, expected=2 / 3)
    assert CATSNDOGS_TABLE.false_omission_rate() == pytest.approx(abs=1e-7, expected=3 / 20)
    assert WORKED_EG_TABLE.false_omission_rate() == pytest.approx(abs=1e-7, expected=10 / 1830)

def test_fallout():
    """Test abydos.stats.ConfusionTable.fallout."""
    assert UNIT_TABLE.fallout() == 0.5
    assert isnan(NULL_TABLE.fallout())
    assert SCALE_TABLE.fallout() == pytest.approx(abs=1e-7, expected=0.6)
    assert CATSNDOGS_TABLE.fallout() == pytest.approx(abs=1e-7, expected=2 / 19)
    assert WORKED_EG_TABLE.fallout() == pytest.approx(abs=1e-7, expected=0.09)

def test_pos_likelihood_ratio():
    """Test abydos.stats.ConfusionTable.pos_likelihood_ratio."""
    assert UNIT_TABLE.pos_likelihood_ratio() == 1.0
    assert isnan(NULL_TABLE.pos_likelihood_ratio())
    assert SCALE_TABLE.pos_likelihood_ratio() == pytest.approx(abs=1e-7, expected=1 / 3)
    assert CATSNDOGS_TABLE.pos_likelihood_ratio() == pytest.approx(abs=1e-7, expected=5.9375)
    assert WORKED_EG_TABLE.pos_likelihood_ratio() == pytest.approx(abs=1e-7, expected=7.407407407407409)

def test_neg_likelihood_ratio():
    """Test abydos.stats.ConfusionTable.neg_likelihood_ratio."""
    assert UNIT_TABLE.neg_likelihood_ratio() == 1.0
    assert isnan(NULL_TABLE.neg_likelihood_ratio())
    assert SCALE_TABLE.neg_likelihood_ratio() == pytest.approx(abs=1e-7, expected=2.0)
    assert CATSNDOGS_TABLE.neg_likelihood_ratio() == pytest.approx(abs=1e-7, expected=0.41911764705882354)
    assert WORKED_EG_TABLE.neg_likelihood_ratio() == pytest.approx(abs=1e-7, expected=0.36630036630036633)

def test_diagnostic_odds_ratio():
    """Test abydos.stats.ConfusionTable.diagnostic_odds_ratio."""
    assert UNIT_TABLE.diagnostic_odds_ratio() == 1.0
    assert isnan(NULL_TABLE.diagnostic_odds_ratio())
    assert SCALE_TABLE.diagnostic_odds_ratio() == pytest.approx(abs=1e-7, expected=1 / 6)
    assert CATSNDOGS_TABLE.diagnostic_odds_ratio() == pytest.approx(abs=1e-7, expected=85 / 6)
    assert WORKED_EG_TABLE.diagnostic_odds_ratio() == pytest.approx(abs=1e-7, expected=20.22222222222222)

def test_fdr():
    """Test abydos.stats.ConfusionTable.fdr."""
    assert UNIT_TABLE.fdr() == 0.5
    assert isnan(NULL_TABLE.fdr())
    assert SCALE_TABLE.fdr() == pytest.approx(abs=1e-7, expected=0.75)
    assert CATSNDOGS_TABLE.fdr() == pytest.approx(abs=1e-7, expected=2 / 7)
    assert WORKED_EG_TABLE.fdr() == pytest.approx(abs=1e-7, expected=0.9)

def test_accuracy():
    """Test abydos.stats.ConfusionTable.accuracy."""
    assert UNIT_TABLE.accuracy() == 0.5
    assert isnan(NULL_TABLE.accuracy())
    assert SCALE_TABLE.accuracy() == pytest.approx(abs=1e-7, expected=3 / 10)
    assert CATSNDOGS_TABLE.accuracy() == pytest.approx(abs=1e-7, expected=22 / 27)
    assert WORKED_EG_TABLE.accuracy() == pytest.approx(abs=1e-7, expected=184 / 203)

def test_accuracy_gain():
    """Test abydos.stats.ConfusionTable.accuracy_gain."""
    assert UNIT_TABLE.accuracy_gain() == 1
    assert isnan(NULL_TABLE.accuracy_gain())
    assert SCALE_TABLE.accuracy_gain() == pytest.approx(abs=1e-7, expected=(3 / 10) / ((5 / 10) ** 2 + (5 / 10) ** 2))
    assert CATSNDOGS_TABLE.accuracy_gain() == pytest.approx(abs=1e-7, expected=(22 / 27) / ((8 / 27) ** 2 + (19 / 27) ** 2))
    assert WORKED_EG_TABLE.accuracy_gain() == pytest.approx(abs=1e-7, expected=(184 / 203) / ((30 / 2030) ** 2 + (2000 / 2030) ** 2))

def test_balanced_accuracy():
    """Test abydos.stats.ConfusionTable.balanced_accuracy."""
    assert UNIT_TABLE.balanced_accuracy() == 0.5
    assert isnan(NULL_TABLE.balanced_accuracy())
    assert SCALE_TABLE.balanced_accuracy() == pytest.approx(abs=1e-7, expected=0.3)
    assert CATSNDOGS_TABLE.balanced_accuracy() == pytest.approx(abs=1e-7, expected=231 / 304)
    assert WORKED_EG_TABLE.balanced_accuracy() == pytest.approx(abs=1e-7, expected=473 / 600)

def test_error_rate():
    """Test abydos.stats.ConfusionTable.error_rate."""
    assert UNIT_TABLE.error_rate() == 0.5
    assert isnan(NULL_TABLE.error_rate())
    assert SCALE_TABLE.error_rate() == pytest.approx(abs=1e-7, expected=0.7)
    assert CATSNDOGS_TABLE.error_rate() == pytest.approx(abs=1e-7, expected=5 / 27)
    assert WORKED_EG_TABLE.error_rate() == pytest.approx(abs=1e-7, expected=190 / 2030)

def test_prevalence():
    """Test abydos.stats.ConfusionTable.prevalence."""
    assert UNIT_TABLE.prevalence() == 0.5
    assert isnan(NULL_TABLE.prevalence())
    assert SCALE_TABLE.prevalence() == pytest.approx(abs=1e-7, expected=0.5)
    assert CATSNDOGS_TABLE.prevalence() == pytest.approx(abs=1e-7, expected=8 / 27)
    assert WORKED_EG_TABLE.prevalence() == pytest.approx(abs=1e-7, expected=30 / 2030)

def test_informedness():
    """Test abydos.stats.ConfusionTable.informedness."""
    assert UNIT_TABLE.informedness() == 0
    assert isnan(NULL_TABLE.informedness())
    assert SCALE_TABLE.informedness() == pytest.approx(abs=1e-7, expected=-0.4)
    assert CATSNDOGS_TABLE.informedness() == pytest.approx(abs=1e-7, expected=79 / 152)
    assert WORKED_EG_TABLE.informedness() == pytest.approx(abs=1e-7, expected=2 / 3 - 0.09)

def test_markedness():
    """Test abydos.stats.ConfusionTable.markedness."""
    assert UNIT_TABLE.markedness() == 0
    assert isnan(NULL_TABLE.markedness())
    assert SCALE_TABLE.markedness() == pytest.approx(abs=1e-7, expected=-5 / 12)
    assert CATSNDOGS_TABLE.markedness() == pytest.approx(abs=1e-7, expected=79 / 140)
    assert WORKED_EG_TABLE.markedness() == pytest.approx(abs=1e-7, expected=173 / 1830)



prre = tuple(((i.precision(), i.recall()) for i in ALL_TABLES))


def test_pr_amean():
    """Test abydos.stats.ConfusionTable.pr_amean."""
    assert UNIT_TABLE.pr_amean() == 0.5
    assert isnan(NULL_TABLE.pr_amean())
    assert SCALE_TABLE.pr_amean() == pytest.approx(abs=1e-7, expected=0.225)
    assert CATSNDOGS_TABLE.pr_amean() == pytest.approx(abs=1e-7, expected=0.6696428571428572)
    assert WORKED_EG_TABLE.pr_amean() == pytest.approx(abs=1e-7, expected=0.3833333333333333)
    assert VERY_POOR_TABLE.pr_amean() == pytest.approx(abs=1e-7, expected=0.0)

def test_pr_gmean():
    """Test abydos.stats.ConfusionTable.pr_gmean."""
    assert UNIT_TABLE.pr_gmean() == 0.5
    assert isnan(NULL_TABLE.pr_gmean())
    assert SCALE_TABLE.pr_gmean() == pytest.approx(abs=1e-7, expected=0.22360679774997899)
    assert CATSNDOGS_TABLE.pr_gmean() == pytest.approx(abs=1e-7, expected=0.66815310478106094)
    assert WORKED_EG_TABLE.pr_gmean() == pytest.approx(abs=1e-7, expected=0.25819888974716115)
    assert VERY_POOR_TABLE.pr_gmean() == pytest.approx(abs=1e-7, expected=0.0)

def test_pr_hmean():
    """Test abydos.stats.ConfusionTable.pr_hmean."""
    assert UNIT_TABLE.pr_hmean() == 0.5
    assert isnan(NULL_TABLE.pr_hmean())
    assert SCALE_TABLE.pr_hmean() == pytest.approx(abs=1e-7, expected=0.22222222222222221)
    assert CATSNDOGS_TABLE.pr_hmean() == pytest.approx(abs=1e-7, expected=0.66666666666666663)
    assert WORKED_EG_TABLE.pr_hmean() == pytest.approx(abs=1e-7, expected=0.17391304347826086)
    assert VERY_POOR_TABLE.pr_hmean() == pytest.approx(abs=1e-7, expected=0.0)

def test_pr_qmean():
    """Test abydos.stats.ConfusionTable.pr_qmean."""
    assert UNIT_TABLE.pr_qmean() == sqrt(sum(i ** 2 for i in prre[0]) / 2)
    assert isnan(NULL_TABLE.pr_qmean())
    assert SCALE_TABLE.pr_qmean() == pytest.approx(abs=1e-7, expected=sqrt(sum(i ** 2 for i in prre[2]) / 2))
    assert CATSNDOGS_TABLE.pr_qmean() == pytest.approx(abs=1e-7, expected=sqrt(sum(i ** 2 for i in prre[3]) / 2))
    assert WORKED_EG_TABLE.pr_qmean() == pytest.approx(abs=1e-7, expected=sqrt(sum(i ** 2 for i in prre[4]) / 2))
    assert VERY_POOR_TABLE.pr_qmean() == pytest.approx(abs=1e-7, expected=0.0)

def test_pr_cmean():
    """Test abydos.stats.ConfusionTable.pr_cmean."""
    assert UNIT_TABLE.pr_cmean() == 0.5
    assert isnan(NULL_TABLE.pr_cmean())
    assert SCALE_TABLE.pr_cmean() == pytest.approx(abs=1e-7, expected=41 / 180)
    assert CATSNDOGS_TABLE.pr_cmean() == pytest.approx(abs=1e-7, expected=113 / 168)
    assert WORKED_EG_TABLE.pr_cmean() == pytest.approx(abs=1e-7, expected=409 / 690)

def test_pr_lmean():
    """Test abydos.stats.ConfusionTable.pr_lmean."""
    assert UNIT_TABLE.pr_lmean() == 0.5
    assert isnan(NULL_TABLE.pr_lmean())
    assert SCALE_TABLE.pr_lmean() == pytest.approx(abs=1e-7, expected=0.2240710058862275)
    assert CATSNDOGS_TABLE.pr_lmean() == pytest.approx(abs=1e-7, expected=0.6686496151266621)
    assert WORKED_EG_TABLE.pr_lmean() == pytest.approx(abs=1e-7, expected=0.2986983802717959)
    assert VERY_POOR_TABLE.pr_lmean() == pytest.approx(abs=1e-7, expected=0.0)

def test_pr_imean():
    """Test abydos.stats.ConfusionTable.pr_imean."""
    assert UNIT_TABLE.pr_imean() == 0.5
    assert isnan(NULL_TABLE.pr_imean())
    assert SCALE_TABLE.pr_imean() == pytest.approx(abs=1e-7, expected=0.224535791730617)
    assert CATSNDOGS_TABLE.pr_imean() == pytest.approx(abs=1e-7, expected=0.6691463467789889)
    assert WORKED_EG_TABLE.pr_imean() == pytest.approx(abs=1e-7, expected=0.34277561539033635)
    assert isnan(VERY_POOR_TABLE.pr_imean())

def test_pr_seiffert_mean():
    """Test abydos.stats.ConfusionTable.pr_seiffert_mean."""
    assert isnan(UNIT_TABLE.pr_seiffert_mean())
    assert isnan(NULL_TABLE.pr_seiffert_mean())
    assert SCALE_TABLE.pr_seiffert_mean() == pytest.approx(abs=1e-7, expected=0.2245354073)
    assert CATSNDOGS_TABLE.pr_seiffert_mean() == pytest.approx(abs=1e-7, expected=0.6691461993)
    assert WORKED_EG_TABLE.pr_seiffert_mean() == pytest.approx(abs=1e-7, expected=0.3406355792)
    assert isnan(VERY_POOR_TABLE.pr_seiffert_mean())

def test_pr_lehmer_mean():
    """Test abydos.stats.ConfusionTable.pr_lehmer_mean."""
    assert UNIT_TABLE.pr_lehmer_mean(3) == 0.5
    assert isnan(NULL_TABLE.pr_lehmer_mean(3))
    assert SCALE_TABLE.pr_lehmer_mean(3) == pytest.approx(abs=1e-7, expected=189 / 820)
    assert CATSNDOGS_TABLE.pr_lehmer_mean(3) == pytest.approx(abs=1e-7, expected=4275 / 6328)
    assert WORKED_EG_TABLE.pr_lehmer_mean(3) == pytest.approx(abs=1e-7, expected=8027 / 12270)

    assert UNIT_TABLE.pr_lehmer_mean() == 0.5
    assert isnan(NULL_TABLE.pr_lehmer_mean())
    assert SCALE_TABLE.pr_lehmer_mean() == pytest.approx(abs=1e-7, expected=41 / 180)
    assert CATSNDOGS_TABLE.pr_lehmer_mean() == pytest.approx(abs=1e-7, expected=113 / 168)
    assert WORKED_EG_TABLE.pr_lehmer_mean() == pytest.approx(abs=1e-7, expected=409 / 690)

    assert UNIT_TABLE.pr_lehmer_mean(2) == 0.5
    assert isnan(NULL_TABLE.pr_lehmer_mean(2))
    assert SCALE_TABLE.pr_lehmer_mean(2) == pytest.approx(abs=1e-7, expected=41 / 180)
    assert CATSNDOGS_TABLE.pr_lehmer_mean(2) == pytest.approx(abs=1e-7, expected=113 / 168)
    assert WORKED_EG_TABLE.pr_lehmer_mean(2) == pytest.approx(abs=1e-7, expected=409 / 690)

    # check equivalences to other specific means
    assert WORKED_EG_TABLE.pr_lehmer_mean(0) == pytest.approx(abs=1e-7, expected=WORKED_EG_TABLE.pr_hmean())
    assert WORKED_EG_TABLE.pr_lehmer_mean(0.5) == pytest.approx(abs=1e-7, expected=WORKED_EG_TABLE.pr_gmean())
    assert WORKED_EG_TABLE.pr_lehmer_mean(1) == pytest.approx(abs=1e-7, expected=WORKED_EG_TABLE.pr_amean())
    assert WORKED_EG_TABLE.pr_lehmer_mean(2) == pytest.approx(abs=1e-7, expected=WORKED_EG_TABLE.pr_cmean())

def test_pr_heronian_mean():
    """Test abydos.stats.ConfusionTable.pr_heronian_mean."""
    assert UNIT_TABLE.pr_heronian_mean() == 0.5
    assert isnan(NULL_TABLE.pr_heronian_mean())
    assert SCALE_TABLE.pr_heronian_mean() == pytest.approx(abs=1e-7, expected=0.2245355992)
    assert CATSNDOGS_TABLE.pr_heronian_mean() == pytest.approx(abs=1e-7, expected=0.6691462730)
    assert WORKED_EG_TABLE.pr_heronian_mean() == pytest.approx(abs=1e-7, expected=0.3416218521)
    assert VERY_POOR_TABLE.pr_heronian_mean() == 0

def test_pr_hoelder_mean():
    """Test abydos.stats.ConfusionTable.pr_hoelder_mean."""
    assert UNIT_TABLE.pr_hoelder_mean() == 0.5
    assert isnan(NULL_TABLE.pr_hoelder_mean())
    assert SCALE_TABLE.pr_hoelder_mean() == pytest.approx(abs=1e-7, expected=0.22638462845343543)
    assert CATSNDOGS_TABLE.pr_hoelder_mean() == pytest.approx(abs=1e-7, expected=0.6711293026059334)
    assert WORKED_EG_TABLE.pr_hoelder_mean() == pytest.approx(abs=1e-7, expected=0.4766783215358364)

    assert UNIT_TABLE.pr_hoelder_mean(0) == 0.5
    assert isnan(NULL_TABLE.pr_hoelder_mean(0))
    assert SCALE_TABLE.pr_hoelder_mean(0) == pytest.approx(abs=1e-7, expected=0.22360679774997899)
    assert CATSNDOGS_TABLE.pr_hoelder_mean(0) == pytest.approx(abs=1e-7, expected=0.66815310478106094)
    assert WORKED_EG_TABLE.pr_hoelder_mean(0) == pytest.approx(abs=1e-7, expected=0.25819888974716115)

    assert UNIT_TABLE.pr_hoelder_mean(1) == 0.5
    assert isnan(NULL_TABLE.pr_hoelder_mean(1))
    assert SCALE_TABLE.pr_hoelder_mean(1) == pytest.approx(abs=1e-7, expected=9 / 40)
    assert CATSNDOGS_TABLE.pr_hoelder_mean(1) == pytest.approx(abs=1e-7, expected=75 / 112)
    assert WORKED_EG_TABLE.pr_hoelder_mean(1) == pytest.approx(abs=1e-7, expected=23 / 60)

    assert UNIT_TABLE.pr_hoelder_mean(2) == 0.5
    assert isnan(NULL_TABLE.pr_hoelder_mean(2))
    assert SCALE_TABLE.pr_hoelder_mean(2) == pytest.approx(abs=1e-7, expected=0.22638462845343543)
    assert CATSNDOGS_TABLE.pr_hoelder_mean(2) == pytest.approx(abs=1e-7, expected=0.6711293026059334)
    assert WORKED_EG_TABLE.pr_hoelder_mean(2) == pytest.approx(abs=1e-7, expected=0.4766783215358364)

    assert UNIT_TABLE.pr_hoelder_mean(3) == 0.5
    assert isnan(NULL_TABLE.pr_hoelder_mean(3))
    assert SCALE_TABLE.pr_hoelder_mean(3) == pytest.approx(abs=1e-7, expected=0.2277441728906747)
    assert CATSNDOGS_TABLE.pr_hoelder_mean(3) == pytest.approx(abs=1e-7, expected=0.6726059172248808)
    assert WORKED_EG_TABLE.pr_hoelder_mean(3) == pytest.approx(abs=1e-7, expected=0.5297282909519099)

    # check equivalences to other specific means
    assert WORKED_EG_TABLE.pr_hoelder_mean(-1) == pytest.approx(abs=1e-7, expected=WORKED_EG_TABLE.pr_hmean())
    assert WORKED_EG_TABLE.pr_hoelder_mean(0) == pytest.approx(abs=1e-7, expected=WORKED_EG_TABLE.pr_gmean())
    assert WORKED_EG_TABLE.pr_hoelder_mean(1) == pytest.approx(abs=1e-7, expected=WORKED_EG_TABLE.pr_amean())
    assert WORKED_EG_TABLE.pr_hoelder_mean(2) == pytest.approx(abs=1e-7, expected=WORKED_EG_TABLE.pr_qmean())

def test_pr_agmean():
    """Test abydos.stats.ConfusionTable.pr_agmean.

    Test values computed via http://arithmeticgeometricmean.blogspot.de/
    """
    assert UNIT_TABLE.pr_agmean() == 0.5
    assert isnan(NULL_TABLE.pr_agmean())
    assert SCALE_TABLE.pr_agmean() == pytest.approx(abs=1e-7, expected=0.2243028580287603)
    assert CATSNDOGS_TABLE.pr_agmean() == pytest.approx(abs=1e-7, expected=0.6688977735879823)
    assert WORKED_EG_TABLE.pr_agmean() == pytest.approx(abs=1e-7, expected=0.3176780357448827)
    assert VERY_POOR_TABLE.pr_agmean() == pytest.approx(abs=1e-7, expected=0.0)

def test_pr_ghmean():
    """Test abydos.stats.ConfusionTable.pr_ghmean."""
    assert UNIT_TABLE.pr_ghmean() == 0.5
    assert isnan(NULL_TABLE.pr_ghmean())
    assert SCALE_TABLE.pr_ghmean() == pytest.approx(abs=1e-7, expected=0.2229128974)
    assert CATSNDOGS_TABLE.pr_ghmean() == pytest.approx(abs=1e-7, expected=0.6674092650)
    assert WORKED_EG_TABLE.pr_ghmean() == pytest.approx(abs=1e-7, expected=0.2098560781)
    assert VERY_POOR_TABLE.pr_ghmean() == pytest.approx(abs=1e-7, expected=0.0)

def test_pr_aghmean():
    """Test abydos.stats.ConfusionTable.pr_aghmean."""
    assert UNIT_TABLE.pr_aghmean() == 0.5
    assert isnan(NULL_TABLE.pr_aghmean())
    assert SCALE_TABLE.pr_aghmean() == pytest.approx(abs=1e-7, expected=0.2236067977)
    assert CATSNDOGS_TABLE.pr_aghmean() == pytest.approx(abs=1e-7, expected=0.6681531047)
    assert WORKED_EG_TABLE.pr_aghmean() == pytest.approx(abs=1e-7, expected=0.2581988897)
    assert VERY_POOR_TABLE.pr_aghmean() == pytest.approx(abs=1e-7, expected=0.0)


    prre = tuple(((i.precision(), i.recall()) for i in ALL_TABLES))

def test_fbeta_score():
    """Test abydos.stats.ConfusionTable.fbeta_score."""
    assert UNIT_TABLE.fbeta_score(1) == 0.5
    assert isnan(NULL_TABLE.fbeta_score(1))
    assert SCALE_TABLE.fbeta_score(1) == pytest.approx(abs=1e-7, expected=2 / 9)
    assert CATSNDOGS_TABLE.fbeta_score(1) == pytest.approx(abs=1e-7, expected=2 / 3)
    assert WORKED_EG_TABLE.fbeta_score(1) == pytest.approx(abs=1e-7, expected=4 / 23)
    with pytest.raises(AttributeError):
        UNIT_TABLE.fbeta_score(-1)

def test_f2_score():
    """Test abydos.stats.ConfusionTable.f2_score."""
    assert UNIT_TABLE.f2_score() == 0.5
    assert isnan(NULL_TABLE.f2_score())
    assert SCALE_TABLE.f2_score() == pytest.approx(abs=1e-7, expected=5 / 24)
    assert CATSNDOGS_TABLE.f2_score() == pytest.approx(abs=1e-7, expected=25 / 39)
    assert WORKED_EG_TABLE.f2_score() == pytest.approx(abs=1e-7, expected=5 / 16)

def test_fhalf_score():
    """Test abydos.stats.ConfusionTable.fhalf_score."""
    assert UNIT_TABLE.fhalf_score() == 0.5
    assert isnan(NULL_TABLE.fhalf_score())
    assert SCALE_TABLE.fhalf_score() == pytest.approx(abs=1e-7, expected=5 / 21)
    assert CATSNDOGS_TABLE.fhalf_score() == pytest.approx(abs=1e-7, expected=25 / 36)
    assert WORKED_EG_TABLE.fhalf_score() == pytest.approx(abs=1e-7, expected=10 / 83)

def test_e_score():
    """Test abydos.stats.ConfusionTable.e_score."""
    assert UNIT_TABLE.e_score() == 0.5
    assert isnan(NULL_TABLE.e_score())
    assert SCALE_TABLE.e_score() == pytest.approx(abs=1e-7, expected=7 / 9)
    assert CATSNDOGS_TABLE.e_score() == pytest.approx(abs=1e-7, expected=1 / 3)
    assert WORKED_EG_TABLE.e_score() == pytest.approx(abs=1e-7, expected=19 / 23)

def test_f1_score():
    """Test abydos.stats.ConfusionTable.f1_score."""
    assert UNIT_TABLE.f1_score() == 0.5
    assert isnan(NULL_TABLE.f1_score())
    assert SCALE_TABLE.f1_score() == pytest.approx(abs=1e-7, expected=2 / 9)
    assert CATSNDOGS_TABLE.f1_score() == pytest.approx(abs=1e-7, expected=2 / 3)
    assert WORKED_EG_TABLE.f1_score() == pytest.approx(abs=1e-7, expected=4 / 23)

def test_jaccard():
    """Test abydos.stats.ConfusionTable.jaccard."""
    assert UNIT_TABLE.jaccard() == 1 / 3
    assert isnan(NULL_TABLE.jaccard())
    assert SCALE_TABLE.jaccard() == pytest.approx(abs=1e-7, expected=1 / 8)
    assert CATSNDOGS_TABLE.jaccard() == pytest.approx(abs=1e-7, expected=0.5)
    assert WORKED_EG_TABLE.jaccard() == pytest.approx(abs=1e-7, expected=20 / 210)

def test_d_measure():
    """Test abydos.stats.ConfusionTable.d_measure."""
    assert UNIT_TABLE.d_measure() == pytest.approx(abs=1e-7, expected=2 / 3)
    assert isnan(NULL_TABLE.d_measure())
    assert SCALE_TABLE.d_measure() == pytest.approx(abs=1e-7, expected=7 / 8)
    assert CATSNDOGS_TABLE.d_measure() == pytest.approx(abs=1e-7, expected=0.5)
    assert WORKED_EG_TABLE.d_measure() == pytest.approx(abs=1e-7, expected=0.9047619047619048)

def test_mcc():
    """Test abydos.stats.ConfusionTable.mcc."""
    assert UNIT_TABLE.mcc() == 0
    assert isnan(NULL_TABLE.mcc())
    assert SCALE_TABLE.mcc() == pytest.approx(abs=1e-7, expected=-10 / sqrt(600))
    assert CATSNDOGS_TABLE.mcc() == pytest.approx(abs=1e-7, expected=79 / sqrt(21280))
    assert WORKED_EG_TABLE.mcc() == pytest.approx(abs=1e-7, expected=34600 / sqrt(21960000000))

def test_significance():
    """Test abydos.stats.ConfusionTable.significance."""
    assert UNIT_TABLE.significance() == 0
    assert isnan(NULL_TABLE.significance())
    assert SCALE_TABLE.significance() == pytest.approx(abs=1e-7, expected=5 / 3)
    assert CATSNDOGS_TABLE.significance() == pytest.approx(abs=1e-7, expected=79 ** 2 / 21280 * 27)
    assert WORKED_EG_TABLE.significance() == pytest.approx(abs=1e-7, expected=34600 ** 2 / 21960000000 * 2030)

def test_kappa_statistic():
    """Test abydos.stats.ConfusionTable.kappa_statistic."""

    def _quick_kappa(acc, racc):
        return (acc - racc) / (1 - racc)

    assert UNIT_TABLE.kappa_statistic() == 0
    assert isnan(NULL_TABLE.kappa_statistic())
    assert SCALE_TABLE.kappa_statistic() == pytest.approx(abs=1e-7, expected=_quick_kappa((3 / 10), (1 / 2)))
    assert CATSNDOGS_TABLE.kappa_statistic() == pytest.approx(abs=1e-7, expected=_quick_kappa((22 / 27), (436 / 27 ** 2)))
    assert WORKED_EG_TABLE.kappa_statistic() == pytest.approx(abs=1e-7, expected=_quick_kappa((184 / 203), (((2000 * 1830) + 6000) / 2030 ** 2)))

def test_phi_coefficient():
    """Test abydos.stats.ConfusionTable.phi_coefficient."""
    assert UNIT_TABLE.phi_coefficient() == 0.0
    assert isnan(NULL_TABLE.phi_coefficient())
    assert SCALE_TABLE.phi_coefficient() == pytest.approx(abs=1e-7, expected=-0.408248290463863)
    assert CATSNDOGS_TABLE.phi_coefficient() == pytest.approx(abs=1e-7, expected=0.5415533908932432)
    assert WORKED_EG_TABLE.phi_coefficient() == pytest.approx(abs=1e-7, expected=0.23348550853492078)

def test_joint_entropy():
    """Test abydos.stats.ConfusionTable.joint_entropy."""
    assert UNIT_TABLE.joint_entropy() == 1.3862943611198906
    assert isnan(NULL_TABLE.joint_entropy())
    assert SCALE_TABLE.joint_entropy() == pytest.approx(abs=1e-7, expected=1.2798542258336676)
    assert CATSNDOGS_TABLE.joint_entropy() == pytest.approx(abs=1e-7, expected=1.040505471995055)
    assert WORKED_EG_TABLE.joint_entropy() == pytest.approx(abs=1e-7, expected=0.38442665366628237)

def test_actual_entropy():
    """Test abydos.stats.ConfusionTable.actual_entropy."""
    assert UNIT_TABLE.actual_entropy() == 0.6931471805599453
    assert isnan(NULL_TABLE.actual_entropy())
    assert SCALE_TABLE.actual_entropy() == pytest.approx(abs=1e-7, expected=0.6931471805599456)
    assert CATSNDOGS_TABLE.actual_entropy() == pytest.approx(abs=1e-7, expected=0.6076934238709568)
    assert WORKED_EG_TABLE.actual_entropy() == pytest.approx(abs=1e-7, expected=0.07695321955601564)

def test_predicted_entropy():
    """Test abydos.stats.ConfusionTable.predicted_entropy."""
    assert UNIT_TABLE.predicted_entropy() == 0.6931471805599453
    assert isnan(NULL_TABLE.predicted_entropy())
    assert SCALE_TABLE.predicted_entropy() == pytest.approx(abs=1e-7, expected=0.6730116670092565)
    assert CATSNDOGS_TABLE.predicted_entropy() == pytest.approx(abs=1e-7, expected=0.5722806988018472)
    assert WORKED_EG_TABLE.predicted_entropy() == pytest.approx(abs=1e-7, expected=0.3218236566720343)

def test_mutual_information():
    """Test abydos.stats.ConfusionTable.mutual_information."""
    assert UNIT_TABLE.mutual_information() == 0.0
    assert isnan(NULL_TABLE.mutual_information())
    assert SCALE_TABLE.mutual_information() == pytest.approx(abs=1e-7, expected=0.08630462173553424)
    assert CATSNDOGS_TABLE.mutual_information() == pytest.approx(abs=1e-7, expected=0.13946865067774858)
    assert WORKED_EG_TABLE.mutual_information() == pytest.approx(abs=1e-7, expected=0.014350222561768025)

def test_proficiency():
    """Test abydos.stats.ConfusionTable.proficiency."""
    assert UNIT_TABLE.proficiency() == 0.0
    assert isnan(NULL_TABLE.proficiency())
    assert SCALE_TABLE.proficiency() == pytest.approx(abs=1e-7, expected=0.12451124978365304)
    assert CATSNDOGS_TABLE.proficiency() == pytest.approx(abs=1e-7, expected=0.229504952989856)
    assert WORKED_EG_TABLE.proficiency() == pytest.approx(abs=1e-7, expected=0.1864798203968872)

def test_igr():
    """Test abydos.stats.ConfusionTable.igr."""
    assert UNIT_TABLE.igr() == 0.0
    assert isnan(NULL_TABLE.igr())
    assert SCALE_TABLE.igr() == pytest.approx(abs=1e-7, expected=0.12823644219877575)
    assert CATSNDOGS_TABLE.igr() == pytest.approx(abs=1e-7, expected=0.24370671764703314)
    assert WORKED_EG_TABLE.igr() == pytest.approx(abs=1e-7, expected=0.044590328474180894)

def test_dependency():
    """Test abydos.stats.ConfusionTable.dependency."""
    assert UNIT_TABLE.dependency() == 0.0
    assert isnan(NULL_TABLE.dependency())
    assert SCALE_TABLE.dependency() == pytest.approx(abs=1e-7, expected=0.06743316542891234)
    assert CATSNDOGS_TABLE.dependency() == pytest.approx(abs=1e-7, expected=0.13403932457013681)
    assert WORKED_EG_TABLE.dependency() == pytest.approx(abs=1e-7, expected=0.03732889596730547)

def test_lift():
    """Test abydos.stats.ConfusionTable.lift."""
    assert UNIT_TABLE.lift() == 1.0
    assert isnan(NULL_TABLE.lift())
    assert SCALE_TABLE.lift() == pytest.approx(abs=1e-7, expected=0.5)
    assert CATSNDOGS_TABLE.lift() == pytest.approx(abs=1e-7, expected=2.4107142857142856)
    assert WORKED_EG_TABLE.lift() == pytest.approx(abs=1e-7, expected=6.76666666666666)
