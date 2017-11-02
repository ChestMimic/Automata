"""LSystem.py
Implementation of L-Systems for string processing
https://en.wikipedia.org/wiki/L-system
"""

import random

class LRule:
	def __init__(self, initial, final):
		"""	Initialize a basic L-System Rule. All ruletypes should be a subset of this rule.

		Keywords:
		initial -- The character this rule will replace
		final -- The character that this rule will insert
		"""
		self.root = initial
		self.result = final

	def pickResult(self):
		""" Provide just the result of this rule"""
		return self.result


class SLRule(LRule):
	def __init__(self, initial, weightedFinals):
		""" Initialize a stochiastic L-System rule.return

		Keywords:
		initial -- Character this rule will replace
		weightedFinals -- List of tuples featuring replacement characters and their respective probabilities
			weightedFinals list should be formatted similar to:
			[(A, 1),(B,1)...]
		"""
		LRule.__init__(self, initial, weightedFinals)
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


class LGrammar:
	def __init__(self, ruleList = [] ):
		"""Initialize a grammar system to process a list of rules

		Keyword:
		ruleList -- A list of LRule objects to use with processing
		"""
		self.rules = ruleList

	def getRule(self, rootVal):
		"""Find and return the LRule relating to an input character (None if no matching rule exists)"""
		for rule in self.rules:
			if rootVal == rule.root:
				return rule
		return None

	def processString(self, string, generations=1):
		""" Take an input and perform all relevant rules in grammar to produce an output.

		Keywords:
		axiom -- Initializing string of n characters
		generations -- Number of iterations of this ruleset too perform on axiom (default is one)

		Note:
		Default behavior for any characters without defined rules is to be constant 
		"""
		reply = ""
		generations -= 1
		for character in string:
			relevantRule = self.getRule(character)
			if relevantRule is None:
				reply += character
			else:
				reply += relevantRule.pickResult()
		if generations > 0:
			return self.processString(reply, generations)
		else:
			return reply


'''Confirm both rule types work'''
if __name__ == "__main__":
	rulelist = []
	rulelist.append(LRule('A', 'AB'))
	rulelist.append(LRule('B', 'A'))
	grammar1 = LGrammar(rulelist)
	print(grammar1.processString('A', 7))

	srules = []
	srules.append(SLRule('A', [('B', .5),('C', .5),('D',.5)]))
	grammar2 = LGrammar(srules)
	print(grammar2.processString('AAAAAAXAAAAAA'))