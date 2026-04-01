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

"""abydos.tests.stemmer.test_stemmer_uealite.

This module contains unit tests for abydos.stemmer.UEALite
"""


from abydos.stemmer import UEALite

from .. import _corpus_file


class TestUEALite:
    """Test UEA-lite functions.

    abydos.stemmer.UEALite
    """

    stmr = UEALite()
    stmr_adams = UEALite(var='Adams')

    def test_uealite(self):
        """Test abydos.stemmer.UEALite."""
        # base case
        assert self.stmr.stem('') == ''

        # test cases copied from Ruby port
        # https://github.com/ealdent/uea-stemmer/blob/master/test/uea_stemmer_test.rb
        # These are corrected to match the Java version's output.
        # stem base words to just the base word
        assert self.stmr.stem('man') == 'man'
        assert self.stmr.stem('happiness') == 'happiness'
        # stem theses as thesis but not bases as basis
        assert self.stmr.stem('theses') == 'thesis'
        assert self.stmr.stem('bases') != 'basis'
        # stem preterite words ending in -ed without the -ed
        assert self.stmr.stem('ordained') == 'ordain'
        assert self.stmr.stem('killed') == 'kill'
        assert self.stmr.stem('liked') == 'lik'
        assert self.stmr.stem('helped') == 'help'
        assert self.stmr.stem('scarred') == 'scarre'
        assert self.stmr.stem('invited') == 'invit'
        assert self.stmr.stem('exited') == 'exit'
        assert self.stmr.stem('debited') == 'debit'
        assert self.stmr.stem('smited') == 'smit'
        # stem progressive verbs and gerunds without the -ing
        assert self.stmr.stem('running') == 'run'
        assert self.stmr.stem('settings') == 'set'
        assert self.stmr.stem('timing') == 'time'
        assert self.stmr.stem('dying') == 'dy'
        assert self.stmr.stem('harping') == 'harp'
        assert self.stmr.stem('charring') == 'char'
        # not stem false progressive verbs such as 'sing'
        assert self.stmr.stem('ring') == 'ring'
        assert self.stmr.stem('sing') == 'se'
        assert self.stmr.stem('bring') == 'br'
        assert self.stmr.stem('fling') == 'fle'
        # stem various plural nouns and 3rd-pres verbs without the -s/-es
        assert self.stmr.stem('changes') == 'change'
        assert self.stmr.stem('deaths') == 'death'
        assert self.stmr.stem('shadows') == 'shadow'
        assert self.stmr.stem('flies') == 'fly'
        assert self.stmr.stem('things') == 'thing'
        assert self.stmr.stem('nothings') == 'nothing'
        assert self.stmr.stem('witches') == 'witch'
        assert self.stmr.stem('makes') == 'mak'
        assert self.stmr.stem('smokes') == 'smok'
        assert self.stmr.stem('does') == 'do'
        # stem various words with -des suffix
        assert self.stmr.stem('abodes') == 'abod'
        assert self.stmr.stem('escapades') == 'escapad'
        assert self.stmr.stem('crusades') == 'crusad'
        assert self.stmr.stem('grades') == 'grad'
        # stem various words with -res suffix
        assert self.stmr.stem('wires') == 'wir'
        assert self.stmr.stem('acres') == 'acr'
        assert self.stmr.stem('fires') == 'fir'
        assert self.stmr.stem('cares') == 'car'
        # stem acronyms when pluralized otherwise they should be left alone
        assert self.stmr.stem('USA') == 'USA'
        assert self.stmr.stem('FLOSS') == 'FLOSS'
        assert self.stmr.stem('MREs') == 'MRE'
        assert self.stmr.stem('USAED') == 'USAED'

        # test cases copied from Ruby port
        # https://github.com/ealdent/uea-stemmer/blob/master/test/uea_stemmer_test.rb
        # stem base words to just the base word
        assert self.stmr_adams.stem('man') == 'man'
        assert self.stmr_adams.stem('happiness') == 'happiness'
        # stem theses as thesis but not bases as basis
        assert self.stmr_adams.stem('theses') == 'thesis'
        assert self.stmr_adams.stem('bases') != 'basis'
        # stem preterite words ending in -ed without the -ed
        assert self.stmr_adams.stem('ordained') == 'ordain'
        assert self.stmr_adams.stem('killed') == 'kill'
        assert self.stmr_adams.stem('liked') == 'like'
        assert self.stmr_adams.stem('helped') == 'help'
        assert self.stmr_adams.stem('scarred') == 'scar'
        assert self.stmr_adams.stem('invited') == 'invite'
        assert self.stmr_adams.stem('exited') == 'exit'
        assert self.stmr_adams.stem('debited') == 'debit'
        assert self.stmr_adams.stem('smited') == 'smite'
        # stem progressive verbs and gerunds without the -ing
        assert self.stmr_adams.stem('running') == 'run'
        assert self.stmr_adams.stem('settings') == 'set'
        assert self.stmr_adams.stem('timing') == 'time'
        assert self.stmr_adams.stem('dying') == 'die'
        assert self.stmr_adams.stem('harping') == 'harp'
        assert self.stmr_adams.stem('charring') == 'char'
        # not stem false progressive verbs such as 'sing'
        assert self.stmr_adams.stem('ring') == 'ring'
        assert self.stmr_adams.stem('sing') == 'sing'
        assert self.stmr_adams.stem('ring') == 'ring'
        assert self.stmr_adams.stem('bring') == 'bring'
        assert self.stmr_adams.stem('fling') == 'fling'
        # stem various plural nouns and 3rd-pres verbs without the -s/-es
        assert self.stmr_adams.stem('changes') == 'change'
        assert self.stmr_adams.stem('deaths') == 'death'
        assert self.stmr_adams.stem('shadows') == 'shadow'
        assert self.stmr_adams.stem('flies') == 'fly'
        assert self.stmr_adams.stem('things') == 'thing'
        assert self.stmr_adams.stem('nothings') == 'nothing'
        assert self.stmr_adams.stem('witches') == 'witch'
        assert self.stmr_adams.stem('makes') == 'make'
        assert self.stmr_adams.stem('smokes') == 'smoke'
        assert self.stmr_adams.stem('does') == 'do'
        # stem various words with -des suffix
        assert self.stmr_adams.stem('abodes') == 'abode'
        assert self.stmr_adams.stem('escapades') == 'escapade'
        assert self.stmr_adams.stem('crusades') == 'crusade'
        assert self.stmr_adams.stem('grades') == 'grade'
        # stem various words with -res suffix
        assert self.stmr_adams.stem('wires') == 'wire'
        assert self.stmr_adams.stem('acres') == 'acre'
        assert self.stmr_adams.stem('fires') == 'fire'
        assert self.stmr_adams.stem('cares') == 'care'
        # stem acronyms when pluralized otherwise they should be left alone
        assert self.stmr_adams.stem('USA') == 'USA'
        assert self.stmr_adams.stem('FLOSS') == 'FLOSS'
        assert self.stmr_adams.stem('MREs') == 'MRE'
        assert self.stmr_adams.stem('USAED') == 'USAED'

        # Perl version tests
        assert self.stmr.stem('ragings') == 'rage'
        assert UEALite(var='Perl').stem('ragings') == 'rag'

        # complete coverage
        assert self.stmr.stem('was') == 'was'
        assert self.stmr.stem('during') == 'during'
        assert (
            UEALite(max_word_length=20).stem('abcdefghijklmnopqrstuvwxyz')
            == 'abcdefghijklmnopqrstuvwxyz'
        )
        assert self.stmr.stem('10') == '10'
        assert self.stmr.stem('top-ten') == 'top-ten'
        assert self.stmr.stem('top-10') == 'top-10'
        assert self.stmr.stem('top_ten') == 'top_ten'
        assert UEALite(max_acro_length=8, var='Adams').stem('ABCDEFGHIJKLMs') == 'ABCDEFGHIJKLMs'
        assert UEALite(max_acro_length=8, var='Adams').stem('ABCDEFGHIJKLM') == 'ABCDEFGHIJKLM'
        assert self.stmr.stem('abcDefGhij') == 'abcDefGhij'
        assert self.stmr.stem('Tophat') == 'Tophat'

    def test_uealite_wsj_set(self):
        """Test abydos.stemmer.UEALite (WSJ testset)."""
        with open(_corpus_file('uea-lite_wsj.csv')) as wsj_ts:
            for wsj_line in wsj_ts:
                (word, uea, rule) = wsj_line.strip().split(',')
                assert (
                    self.stmr._stem_and_rule(word)
                    == (uea, float(rule))  # noqa: SF01
                )
