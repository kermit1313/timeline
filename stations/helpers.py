

def sort_by_order(to_order):
	n = len(to_order)
	
	for i in range(n):
		already_sorted = True
		for j in range(n - i - 1):
			if to_order[j].order > to_order[j+1].order:
				to_order[j], to_order[j+1] = to_order[j+1], to_order[j]
				already_sorted = False
		if already_sorted:
			break
	
	return to_order


def sort_by_station(to_order):
	n = len(to_order)
	
	for i in range(n):
		already_sorted = True
		for j in range(n - i - 1):
			if to_order[j]["Station_symbol"] < to_order[j+1]["Station_symbol"]:
				to_order[j], to_order[j+1] = to_order[j+1], to_order[j]
				already_sorted = False
		if already_sorted:
			break
	
	return to_order