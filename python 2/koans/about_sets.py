#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *


class AboutSets(Koan):
    def test_sets_make_keep_lists_unique(self):
        highlanders = ['MacLeod', 'Ramirez', 'MacLeod', 'Matunas',
            'MacLeod', 'Malcolm', 'MacLeod']
        
        print highlanders
        there_can_only_be_only_one = set(highlanders)
        print there_can_only_be_only_one

        # TODO: Not sure how they order the words, strange~~~
        self.assertEqual(set(['Malcolm', 'Matunas', 'MacLeod', 'Ramirez']), there_can_only_be_only_one)

    def test_sets_are_unordered(self):
        self.assertEqual(set(['5', '4', '3', '2', '1']), set('12345'))
        
    def test_convert_the_set_into_a_list_to_sort_it(self):
        # Convert set to list
        self.assertEqual(['1', '2', '3', '4', '5'], sorted(set('13245')))
        
    # ------------------------------------------------------------------

    def chars_in(self, a_set):
        return ''.join(sorted(a_set))

    def test_set_have_arithmetic_operators(self):
        # after sort acdelmo
        good_guy = set('macleod')
        # after sort amnstu
        bad_guy = set('mutunas')
        
        self.assertEqual('cdelo', self.chars_in(good_guy - bad_guy))
        # TODO: I think it's should be acdelmonstu
        self.assertEqual('acdelmnostu', self.chars_in(good_guy | bad_guy))
        self.assertEqual('am', self.chars_in(good_guy & bad_guy))
        self.assertEqual('cdelnostu', self.chars_in(good_guy ^ bad_guy))

    # ------------------------------------------------------------------

    def test_we_can_query_set_membership(self):
        self.assertEqual(True, 127 in set([127, 0, 0, 1]))
        self.assertEqual(True, 'cow' not in set('apocalypse now'))
        
    def test_we_can_compare_subsets(self):
        self.assertEqual(True, set('cake') <= set('cherry cake'))
        self.assertEqual(True, set('cake').issubset(set('cherry cake')))
        
        # compare ascii
        self.assertEqual(False, set('cake') > set('pie'))
