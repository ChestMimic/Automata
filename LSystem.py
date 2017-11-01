import random

class LRule:
	def __init__(self, initial, final):
		self.root = initial
		self.result = final

	def pickResult(self):
		return self.result


class SLRule(LRule):
	def __init__(self, initial, weightedFinals):
		LRule.__init__(initial, weightedFinals)
		self.weightScale = 0
		for item in self.result:
			if item[1] > self.weightScale:
				self.weightScale = item[1]

	def pickResult(self):
		diecast = random.randint(0, self.weightScale[1])
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
		self.rules = ruleList

	def getRule(self, rootVal):
		for rule in self.rules:
			if rootVal == rule.root:
				return rule
		return None

	def processString(self, string, generations=1):
		reply = ""
		generations -= 1
		for character in string:
			relevantRule = self.getRule(character)
			if relevantRule is None:
				reply += character
			else:
				reply += relevantRule.pickResult()

		print(reply)
		if generations > 0:
			return self.processString(reply, generations)
		else:
			return reply

if __name__ == "__main__":
	rulelist = []
	rulelist.append(LRule('A', 'AB'))
	rulelist.append(LRule('B', 'A'))
	grammar1 = LGrammar(rulelist)

	print(grammar1.processString('A', 5))


	srules = []
	srules.append(SLRule('A', [('AB', .5),('A', .5)]))
	grammar2 = LGrammar(srules)