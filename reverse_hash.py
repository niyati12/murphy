class Hash:
	def __init__(self,letters):
		self.base = letters

	def reverse_hash(self,num):
		pattern = ''
		while num > 7:
			index = num % 37
			try:
				pattern = self.base[index] + pattern
			except IndexError:
				pass
			num = (num - index)/37
		return pattern

if __name__ == '__main__':

	hash_key = Hash('acdegilmnoprstuw')
	print hash_key.reverse_hash(680131659347)