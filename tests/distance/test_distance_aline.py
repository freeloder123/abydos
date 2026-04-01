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

"""abydos.tests.distance.test_distance_aline.

This module contains unit tests for abydos.distance.ALINE
"""

import pytest

from abydos.distance import ALINE


class TestALINE:
    """Test ALINE functions.

    abydos.distance.ALINE
    """

    cmp = ALINE()
    cmp_downey = ALINE(normalizer=lambda x: sum(x) / len(x))

    def test_aline_alignments(self):
        """Test abydos.distance.ALINE.alignments."""
        # test cases from Kondrak (2000)
        assert self.cmp.alignments('driy', 'tres') == [(75.0, '‖ d r iy ‖', '‖ t r e  ‖ s')]
        assert self.cmp.alignments('blow', 'flare') == [(53.0, '‖ b l o ‖ w', '‖ f l a ‖ re')]
        assert self.cmp.alignments('ful', 'plenus') == [(48.0, '‖ f u l ‖', '‖ p - l ‖ enus')]
        assert self.cmp.alignments('fiz', 'piskis') == [(63.0, '‖ f i z ‖', '‖ p i s ‖ kis')]
        assert self.cmp.alignments('ay', 'ego') == [(17.5, '‖ ay ‖', '‖ e  ‖ go')]
        assert self.cmp.alignments('tuwz', 'dentis') == [(75.0, '‖ t uw z ‖', 'den ‖ t i  s ‖')]

        # test cases from Kondrak (2002) after Covington (1996)
        # Some of these alignments are a little different from what's in the
        # thesis because of the differing encoding used.
        assert self.cmp.alignments('jo', 'zPe') == [(29.0, '‖ j  o ‖', '‖ zP e ‖')]
        assert self.cmp.alignments('tu', 'tuF') == [(45.0, '‖ t u  ‖', '‖ t uF ‖')]
        assert self.cmp.alignments('nostros', 'nu') == [(47.5, '‖ n o ‖ stros', '‖ n u ‖')]
        assert self.cmp.alignments('kyen', 'ki') == [(47.5, '‖ k ye ‖ n', '‖ k i  ‖')]
        assert self.cmp.alignments('ke', 'kwa') == [(42.5, '‖ k e  ‖', '‖ k wa ‖')]
        assert self.cmp.alignments('todos', 'tu') == [(47.5, '‖ t o ‖ dos', '‖ t u ‖')]
        assert self.cmp.alignments('una', 'uFn') == [(45.0, '‖ u  n ‖ a', '‖ uF n ‖')]
        assert self.cmp.alignments('dos', 'doF') == [(45.0, '‖ d o  ‖ s', '‖ d oF ‖')]
        assert self.cmp.alignments('tres', 'trwa') == [(77.5, '‖ t r e  ‖ s', '‖ t r wa ‖')]
        assert self.cmp.alignments('ombre', 'om') == [
            (50.0, '‖ o m ‖ bre', '‖ o m ‖'),
            (50.0, '‖ o mb ‖ re', '‖ o m  ‖'),
        ]
        assert self.cmp.alignments('arbol', 'arbreC') == [(88.0, '‖ a r b o l ‖', '‖ a r b - r ‖ eC')]
        assert self.cmp.alignments('pluFma', 'plum') == [(115.0, '‖ p l uF m ‖ a', '‖ p l u  m ‖')]
        assert self.cmp.alignments('kabetSa', 'kap') == [(75.0, '‖ k a b ‖ etSa', '‖ k a p ‖')]
        assert self.cmp.alignments('boka', 'busP') == [(68.5, '‖ b o k  ‖ a', '‖ b u sP ‖')]
        assert self.cmp.alignments('pye', 'pye') == [(65.0, '‖ p y e ‖', '‖ p y e ‖')]
        assert self.cmp.alignments('koratSon', 'koFr') == [(80.0, '‖ k o  r ‖ atSon', '‖ k oF r ‖')]
        assert self.cmp.alignments('ber', 'vwar') == [(60.5, '‖ b e  r ‖', '‖ v wa r ‖')]
        assert self.cmp.alignments('benir', 'veCnir') == [(115.5, '‖ b e  n i r ‖', '‖ v eC n i r ‖')]
        assert self.cmp.alignments('detSir', 'dir') == [
            (65.0, 'de ‖ tS i r ‖', '‖ d  i r ‖'),
            (65.0, '‖ d e tS i r ‖', '‖ d - -  i r ‖'),
        ]
        assert self.cmp.alignments('pobre', 'povreC') == [(115.5, '‖ p o b r e  ‖', '‖ p o v r eC ‖')]
        assert self.cmp.alignments('dSis', 'diHzes') == [(77.5, '‖ dS i s ‖', 'diH ‖ z  e s ‖')]
        assert self.cmp.alignments('dSaFt', 'das') == [(62.5, '‖ dS aF t ‖', '‖ d  a  s ‖')]
        # Different from paper:
        assert self.cmp.alignments('wat', 'vas') == [(40.0, 'w ‖ a t ‖', 'v ‖ a s ‖')]
        assert self.cmp.alignments('nat', 'nixt') == [
            (62.5, '‖ n a - t ‖', '‖ n i x t ‖'),
            (62.5, '‖ n a t  ‖', '‖ n i xt ‖'),
        ]
        assert self.cmp.alignments('logN', 'lagN') == [(75.0, '‖ l o gN ‖', '‖ l a gN ‖')]
        assert self.cmp.alignments('maFn', 'man') == [(82.5, '‖ m aF n ‖', '‖ m a  n ‖')]
        assert self.cmp.alignments('flesP', 'flaysP') == [(122.5, '‖ f l e  sP ‖', '‖ f l ay sP ‖')]
        assert self.cmp.alignments('bleCd', 'bluHt') == [(99.0, '‖ b l eC d ‖', '‖ b l uH t ‖')]
        assert self.cmp.alignments('fedSeCr', 'feHdeCr') == [(124.0, '‖ f e  dS eC r ‖', '‖ f eH d  eC r ‖')]
        assert self.cmp.alignments('haFr', 'haHr') == [(81.5, '‖ h aF r ‖', '‖ h aH r ‖')]
        assert self.cmp.alignments('ir', 'oHr') == [(41.5, '‖ i  r ‖', '‖ oH r ‖')]
        assert self.cmp.alignments('ay', 'awgeC') == [(20.0, '‖ a y ‖', '‖ a w ‖ geC')]
        assert self.cmp.alignments('nowz', 'naHzeC') == [(70.5, '‖ n ow z ‖', '‖ n aH z ‖ eC')]
        assert self.cmp.alignments('mawtS', 'munt') == [(62.5, '‖ m aw - tS ‖', '‖ m u  n t  ‖')]
        assert self.cmp.alignments('teCgN', 'tsugNeC') == [(75.0, '‖ t  eC gN ‖', '‖ ts u  gN ‖ eC')]
        assert self.cmp.alignments('fut', 'fuHs') == [(74.0, '‖ f u  t ‖', '‖ f uH s ‖')]
        assert self.cmp.alignments('niy', 'kniH') == [(53.0, '‖ n iy ‖', 'k ‖ n iH ‖')]
        assert self.cmp.alignments('haFnd', 'hant') == [(107.5, '‖ h aF n d ‖', '‖ h a  n t ‖')]
        assert self.cmp.alignments('hart', 'herts') == [
            (115.0, '‖ h a r t ‖', '‖ h e r t ‖ s'),
            (115.0, '‖ h a r t  ‖', '‖ h e r ts ‖'),
        ]
        assert self.cmp.alignments('liveCr', 'leHbeCr') == [(109.5, '‖ l i  v eC r ‖', '‖ l eH b eC r ‖')]
        assert self.cmp.alignments('aFnd', 'ante') == [(72.5, '‖ aF n d ‖', '‖ a  n t ‖ e')]
        assert self.cmp.alignments('aFt', 'ad') == [(37.5, '‖ aF t ‖', '‖ a  d ‖')]
        assert self.cmp.alignments('blow', 'flaHre') == [(52.0, '‖ b l o  ‖ w', '‖ f l aH ‖ re')]
        # Different from paper:
        assert self.cmp.alignments('ir', 'awris') == [(45.0, '‖ i r ‖', 'a ‖ w r ‖ is')]
        assert self.cmp.alignments('iyt', 'edere') == [(40.0, '‖ iy t ‖', '‖ e  d ‖ ere')]
        assert self.cmp.alignments('fisS', 'piskis') == [(73.0, '‖ f i sS ‖', '‖ p i s  ‖ kis')]
        assert self.cmp.alignments('flow', 'fluere') == [(92.5, '‖ f l ow ‖', '‖ f l u  ‖ ere')]
        assert self.cmp.alignments('star', 'steHlla') == [(92.0, '‖ s t a  r ‖', '‖ s t eH l ‖ la')]
        assert self.cmp.alignments('ful', 'pleHnus') == [(48.0, '‖ f u l ‖', '‖ p - l ‖ eHnus')]
        assert self.cmp.alignments('graFs', 'graHmen') == [(81.5, '‖ g r aF ‖ s', '‖ g r aH ‖ men')]
        assert self.cmp.alignments('hart', 'kordis') == [(70.0, '‖ h a r t ‖', '‖ k o r d ‖ is')]
        assert self.cmp.alignments('horn', 'kornuH') == [(90.0, '‖ h o r n ‖', '‖ k o r n ‖ uH')]
        assert self.cmp.alignments('ay', 'ego') == [(17.5, '‖ ay ‖', '‖ e  ‖ go')]
        assert self.cmp.alignments('niy', 'genuH') == [(44.0, '‖ n i  ‖ y', 'ge ‖ n uH ‖')]
        assert self.cmp.alignments('meCdSeCr', 'maHter') == [(109.0, '‖ m eC dS eC r ‖', '‖ m aH t  e  r ‖')]
        assert self.cmp.alignments('mawnteCn', 'moHns') == [(105.5, '‖ m aw n t ‖ eCn', '‖ m oH n s ‖')]
        # The example below is different from the expected, but
        # (73.0, '‖ n ey m ‖', '‖ n oH m ‖ en') is the #2 alignment.
        # This is probably due to slightly differing weights/costs/features.
        assert self.cmp.alignments('neym', 'noHmen') == [(80.5, '‖ n ey m ‖', 'noH ‖ m e  n ‖')]
        assert self.cmp.alignments('nyuw', 'nowus') == [(70.0, '‖ n yu w  ‖', '‖ n o  wu ‖ s')]
        assert self.cmp.alignments('weCn', 'uHnus') == [(48.0, '‖ weC n ‖', '‖ uH  n ‖ us')]
        assert self.cmp.alignments('rawnd', 'rotundus') == [(115.0, '‖ r a - w n d ‖', '‖ r o t u n d ‖ us')]
        assert self.cmp.alignments('sow', 'suere') == [(57.5, '‖ s ow ‖', '‖ s u  ‖ ere')]
        assert self.cmp.alignments('sit', 'seHdere') == [(66.5, '‖ s i  t ‖', '‖ s eH d ‖ ere')]
        assert self.cmp.alignments('tSriy', 'treHs') == [(73.0, '‖ tS r iy ‖', '‖ t  r eH ‖ s')]
        assert self.cmp.alignments('tuwtS', 'dentis') == [(85.0, '‖ t uw tS ‖', 'den ‖ t i  s  ‖')]
        assert self.cmp.alignments('tSin', 'tenuis') == [(67.5, '‖ tS i n ‖', '‖ t  e n ‖ uis')]
        assert self.cmp.alignments('kiHnwaHwa', 'kenuaq') == [(105.5, '‖ k iH n w aH ‖ wa', '‖ k e  n u a  ‖ q')]
        assert self.cmp.alignments('niHna', 'nenah') == [(91.5, '‖ n iH n a ‖', '‖ n e  n a ‖ h')]
        assert self.cmp.alignments('naHpeHwa', 'naHpeHw') == [(115.0, '‖ n aH p eH w ‖ a', '‖ n aH p eH w ‖')]
        assert self.cmp.alignments('waHpimini', 'waHpemen') == [(150.0, '‖ w aH p i m i n ‖ i', '‖ w aH p e m e n ‖')]
        assert self.cmp.alignments('nameHsa', 'nameHqs') == [(125.0, '‖ n a m eH - s ‖ a', '‖ n a m eH q s ‖')]
        assert self.cmp.alignments('okimaHwa', 'okeHmaHw') == [(121.5, '‖ o k i  m aH w ‖ a', '‖ o k eH m aH w ‖')]
        assert self.cmp.alignments('sPiHsPiHpa', 'seHqsep') == [(97.0, '‖ sP iH - sP iH p ‖ a', '‖ s  eH q s  e  p ‖')]
        assert self.cmp.alignments('ahkohkwa', 'ahkeHh') == [(124.0, '‖ a h k o  h ‖ kwa', '‖ a h k eH h ‖')]
        assert self.cmp.alignments('pemaHtesiweni', 'pemaHtesewen') == [
            (
                257.5,
                '‖ p e m aH t e s i w e n ‖ i',
                '‖ p e m aH t e s e w e n ‖',
            )
        ]
        assert self.cmp.alignments('asenya', 'aqsen') == [(90.0, '‖ a - s e n ‖ ya', '‖ a q s e n ‖')]
        assert self.cmp.alignments('didoHmi', 'doH') == [(50.0, 'di ‖ d oH ‖ mi', '‖ d oH ‖')]
        assert self.cmp.alignments('tAugateEr', 'toxteCr') == [(130.0, '‖ tA u g a t e  r ‖', '‖ t  o x - t eC r ‖')]
        assert self.cmp.alignments('doteCr', 'tAugateEr') == [(112.5, '‖ d o t eC r ‖', 'tAu ‖ g a t e  r ‖')]
        assert self.cmp.alignments('ager', 'azPras') == [(61.0, '‖ a g  e r ‖', '‖ a zP - r ‖ as')]
        assert self.cmp.alignments('bAaraHmi', 'pAero') == [(74.0, '‖ bA a r aH ‖ mi', '‖ pA e r o  ‖')]
        assert self.cmp.alignments('kentum', 'hekaton') == [
            (111.5, '‖ k e n t u m ‖', 'he ‖ k a - t o n ‖'),
            (111.5, '‖ k e nt u m ‖', 'he ‖ k a t  o n ‖'),
        ]
        assert self.cmp.alignments('kentum', 'sateCm') == [
            (90.0, '‖ k e n t u  m ‖', '‖ s a - t eC m ‖'),
            (90.0, '‖ k e nt u  m ‖', '‖ s a t  eC m ‖'),
        ]

        # test cases from Downey, et al. (2008)
        assert self.cmp.alignments('api', 'api') == [(65.0, '‖ a p i ‖', '‖ a p i ‖')]
        assert self.cmp.alignments('apik', 'apik') == [(100.0, '‖ a p i k ‖', '‖ a p i k ‖')]
        assert self.cmp.alignments('apila', 'apila') == [(115.0, '‖ a p i l a ‖', '‖ a p i l a ‖')]
        assert self.cmp.alignments('api', 'apik') == [(65.0, '‖ a p i ‖', '‖ a p i ‖ k')]
        assert self.cmp.alignments('api', 'apila') == [(65.0, '‖ a p i ‖', '‖ a p i ‖ la')]
        assert self.cmp.alignments('apik', 'apila') == [(65.0, '‖ a p i ‖ k', '‖ a p i ‖ la')]
        assert self.cmp.alignments('kalarita', 'kalarita') == [(200.0, '‖ k a l a r i t a ‖', '‖ k a l a r i t a ‖')]
        assert self.cmp.alignments('kalara', 'kalara') == [(150.0, '‖ k a l a r a ‖', '‖ k a l a r a ‖')]
        assert self.cmp.alignments('makebela', 'makebela') == [(200.0, '‖ m a k e b e l a ‖', '‖ m a k e b e l a ‖')]
        # The following case has a different score, but the same alignment as
        # in Downey, et. al (2008)
        assert self.cmp.alignments('kalarita', 'kalara') == [(137.5, '‖ k a l a r i ‖ ta', '‖ k a l a r a ‖')]
        assert self.cmp.alignments('kalarita', 'makebela') == [
            (75.0, '‖ k - - a l a ‖ rita', 'ma ‖ k e b e l a ‖'),
            (75.0, '‖ k a - - l a ‖ rita', 'ma ‖ k e b e l a ‖'),
        ]
        assert self.cmp.alignments('kalara', 'makebela') == [(82.0, '‖ k a l a r a ‖', 'ma ‖ k e b e l a ‖')]

        # other alignment styles:
        cmp2 = ALINE(mode='local')
        assert cmp2.alignments('aHpakosiHs', 'waHpikonoHha') == [(120.0, '‖ aH p a k o s iH s ‖', 'w ‖ aH p i k o n oH h ‖ a')]
        cmp2 = ALINE(mode='semi-global')
        assert cmp2.alignments('aHpakosiHs', 'waHpikonoHha') == [(120.0, '‖ aH p a k o s iH s ‖', 'w ‖ aH p i k o n oH h ‖ a')]
        cmp2 = ALINE(mode='half-local')
        assert cmp2.alignments('aHpakosiHs', 'waHpikonoHha') == [(110.0, '‖ aH p a k o s iH s - ‖', 'w ‖ aH p i k o n oH h a ‖')]
        cmp2 = ALINE(mode='global')
        assert cmp2.alignments('aHpakosiHs', 'waHpikonoHha') == [(106.5, '‖ aH  p a k o s iH s - ‖', '‖ waH p i k o n oH h a ‖')]
        # The following just confirms that unknown values of mode use 'local'
        cmp2 = ALINE(mode='universal')
        assert cmp2.alignments('aHpakosiHs', 'waHpikonoHha') == [(120.0, '‖ aH p a k o s iH s ‖', 'w ‖ aH p i k o n oH h ‖ a')]
        assert cmp2.alignments('kan', 'kaABCDHn') == [(84.0, '‖ k a      n ‖', '‖ k aABCDH n ‖')]
        assert cmp2.alignments('kaABCDHn', 'kan') == [(84.0, '‖ k aABCDH n ‖', '‖ k a      n ‖')]
        cmp2 = ALINE(phones='ipa')
        assert cmp2.alignments('kɒgneit', 'kognaːtus') == [(163.0, '‖ k ɒ g n ei t ‖', '‖ k o g n aː t ‖ us')]

    def test_aline_alignment(self):
        """Test abydos.distance.ALINE.alignment."""
        assert self.cmp.alignment('ombre', 'om') == (50.0, '‖ o m ‖ bre', '‖ o m ‖')
        assert self.cmp.alignment('arbol', 'arbreC') == (88.0, '‖ a r b o l ‖', '‖ a r b - r ‖ eC')
        assert self.cmp.alignment('pluFma', 'plum') == (115.0, '‖ p l uF m ‖ a', '‖ p l u  m ‖')
        assert self.cmp.alignment('kabetSa', 'kap') == (75.0, '‖ k a b ‖ etSa', '‖ k a p ‖')
        assert self.cmp.alignment('boka', 'busP') == (68.5, '‖ b o k  ‖ a', '‖ b u sP ‖')
        assert self.cmp.alignment('pye', 'pye') == (65.0, '‖ p y e ‖', '‖ p y e ‖')
        assert self.cmp.alignment('koratSon', 'koFr') == (80.0, '‖ k o  r ‖ atSon', '‖ k oF r ‖')
        assert self.cmp.alignment('ber', 'vwar') == (60.5, '‖ b e  r ‖', '‖ v wa r ‖')
        assert self.cmp.alignment('benir', 'veCnir') == (115.5, '‖ b e  n i r ‖', '‖ v eC n i r ‖')
        assert self.cmp.alignment('detSir', 'dir') == (65.0, 'de ‖ tS i r ‖', '‖ d  i r ‖')

    def test_aline_sim(self):
        """Test abydos.distance.ALINE.sim."""
        # Base cases
        assert self.cmp.sim('', '') == 1.0
        assert self.cmp.sim('a', '') == 0.0
        assert self.cmp.sim('', 'a') == 0.0
        assert self.cmp.sim('abc', '') == 0.0
        assert self.cmp.sim('', 'abc') == 0.0
        assert self.cmp.sim('abc', 'abc') == 1.0
        assert self.cmp.sim('abcd', 'efgh') == 0.425

        assert self.cmp.sim('nigel', 'niall') == pytest.approx(abs=1e-7, expected=0.7037037037)
        assert self.cmp.sim('niall', 'nigel') == pytest.approx(abs=1e-7, expected=0.7037037037)
        assert self.cmp.sim('colin', 'coiln') == pytest.approx(abs=1e-7, expected=0.8333333333)
        assert self.cmp.sim('coiln', 'colin') == pytest.approx(abs=1e-7, expected=0.8333333333)
        assert self.cmp.sim('ATCAACGAGT'.lower(), 'AACGATTAG'.lower()) == pytest.approx(abs=1e-7, expected=0.685185185)

        # test cases from Downey, et al. (2008)
        assert self.cmp_downey.sim('api', 'api') == pytest.approx(abs=1e-7, expected=1.0)
        assert self.cmp_downey.sim('apik', 'apik') == pytest.approx(abs=1e-7, expected=1.0)
        assert self.cmp_downey.sim('apila', 'apila') == pytest.approx(abs=1e-7, expected=1.0)
        assert self.cmp_downey.sim('api', 'apik') == pytest.approx(abs=1e-7, expected=0.7878787879)
        assert self.cmp_downey.sim('api', 'apila') == pytest.approx(abs=1e-7, expected=0.7222222222)
        assert self.cmp_downey.sim('apik', 'apila') == pytest.approx(abs=1e-7, expected=0.6046511628)
        assert self.cmp_downey.sim('kalarita', 'kalarita') == pytest.approx(abs=1e-7, expected=1.0)
        assert self.cmp_downey.sim('kalara', 'kalara') == pytest.approx(abs=1e-7, expected=1.0)
        assert self.cmp_downey.sim('makebela', 'makebela') == pytest.approx(abs=1e-7, expected=1.0)
        assert self.cmp_downey.sim('kalarita', 'kalara') == pytest.approx(abs=1e-7, expected=0.785714286)
        assert self.cmp_downey.sim('kalarita', 'makebela') == pytest.approx(abs=1e-7, expected=0.375)
        assert self.cmp_downey.sim('kalara', 'makebela') == pytest.approx(abs=1e-7, expected=0.468571429)

    def test_aline_sim_score(self):
        """Test abydos.distance.ALINE.sim_score."""
        # Base cases
        assert self.cmp.sim_score('', '') == 1.0
        assert self.cmp.sim_score('a', '') == 0.0
        assert self.cmp.sim_score('', 'a') == 0.0
        assert self.cmp.sim_score('abc', '') == 0.0
        assert self.cmp.sim_score('', 'abc') == 0.0
        assert self.cmp.sim_score('abc', 'abc') == 85.0
        assert self.cmp.sim_score('abcd', 'efgh') == 51.0

        assert self.cmp.sim_score('nigel', 'niall') == pytest.approx(abs=1e-7, expected=95.0)
        assert self.cmp.sim_score('niall', 'nigel') == pytest.approx(abs=1e-7, expected=95.0)
        assert self.cmp.sim_score('colin', 'coiln') == pytest.approx(abs=1e-7, expected=112.5)
        assert self.cmp.sim_score('coiln', 'colin') == pytest.approx(abs=1e-7, expected=112.5)
        assert self.cmp.sim_score('ATCAACGAGT'.lower(), 'AACGATTAG'.lower()) == pytest.approx(abs=1e-7, expected=185.0)
