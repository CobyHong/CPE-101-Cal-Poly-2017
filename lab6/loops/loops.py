def for_version(items): #just counting down.
   result = []
   for i in range(len(items) - 1, -1, -1):
      result.append(items[i])
   return result

def while_version(items):
	i = len(items)-1
	result = []
	while i >=0:
		items.append(items[i])
		i -= 1
	return result

