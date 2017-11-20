class Grammar:
	def __init__(self, ruleList = [] ):
		"""Initialize a grammar system to process a list of rules

		Keyword:
		ruleList -- A list of LRule objects to use with processing
		"""
		self.rules = ruleList

	def getRule(self, rootVal, seed=None):
		"""Find and return the LRule relating to an input character (None if no matching rule exists)

		Keywords:
		rootVal -- character to be solved for
		"""
		for rule in self.rules:
			if rootVal == rule.root:
				return rule
		return None

	def addRule(self, rule):
		"""Add any rule object to this grammar"""
		self.rules.append(rule)

	def delRule(self, ruleAxiom):
		"""Remove a rule from this grammar"""
		r = self.getRule(ruleAxiom)
		self.rules.remove(r)


class LSystem(Grammar):
	def __init__(self, ruleList = []):
		Grammar.__init__(self, ruleList)

	def processString(self, string, generations=1, seed=None):
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


class Markov(Grammar):
	def __init__(self, ruleList = []):
		Grammar.__init__(self, ruleList)

		def performOnAxiom(self, axiom, generations=1):
			reply = ""
			generations -= 1
			relevantRule = self.getRule(axiom)
			nxt = relevantRule.pickResult()
			if relevantRule is None:
				#Non turing complete decision, handle silently
				return reply
			else:
				reply += nxt
			if generations > 0:
				return (reply + self.performOnAxiom(nxt, generations))
			else:
				return reply
