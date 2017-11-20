"""LSystem.py
Implementation of L-Systems for string processing
https://en.wikipedia.org/wiki/L-system
"""

import random

from Grammar import LSystem, Markov

class Rule:
	def __init__(self, initial, final):
		"""	Initialize a basic Rule. All ruletypes should be a subset of this rule.

		Keywords:
		initial -- The character this rule will replace
		final -- The character that this rule will insert
		"""
		self.root = initial
		self.result = final

	def pickResult(self):
		""" Provide just the result of this rule"""
		return self.result


class StochiasticR(Rule):
	def __init__(self, initial, weightedFinals):
		""" Initialize a stochiastic rule.

		Keywords:
		initial -- String this rule will replace
		weightedFinals -- List of tuples featuring replacement Strings and their respective probabilities
			weightedFinals list should be formatted similar to:
			[(A, 1),(B,1)...]
		"""
		Rule.__init__(self, initial, weightedFinals)
		self.weightScale = 0
		for item in self.result:
			self.weightScale += item[1]

	def pickResult(self):
		""" Select one of the possible results based on their weights. 
		All weights are relative to each other. Two rules with equal weight values have equal probability of selection.
		"""
		diecast = random.uniform(0, self.weightScale)
		index = 0
		for item in self.result:
			indexNext = index + item[1]
			if diecast > indexNext:
				index = indexNext
			else:
				return item[0]
				break

	def addResult(self, result, weight):
		"""Append a weighted result to existing rule

		Keywords:
		result -- Outcome to be added
		weight -- Likelyhood this outcome should be selected
		"""
		tup = (result, weight)
		self.result.append(tup)





'''Confirm both rule types work'''
if __name__ == "__main__":
	rulelist = []
	rulelist.append(Rule('A', 'AB'))
	rulelist.append(Rule('B', 'A'))
	grammar1 = LSystem(rulelist)
	print(grammar1.processString('A', 7))

	srules = []
	srules.append(StochiasticR('A', [('B', .5),('C', .5),('D',.5)]))
	grammar2 = LSystem(srules)
	#random.seed(6)
	print(grammar2.processString('AAAAAAXAAAAAA'))

	markovRules  =[]
	markovRules.append(StochiasticR('A', [('A',.5),('B',.5)]))
	markovRules.append(StochiasticR('B', [('A',.5),('B',.5)]))
	markovGrammar = Markov(markovRules)
	print(markovGrammar.performOnAxiom('A', 6))