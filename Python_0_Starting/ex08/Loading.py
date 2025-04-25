
def ft_tqdm(lst: range) -> None:
	total = len(lst)
	for i in range(total):
		percent = ((i + 1) / total) * 100
		bar = "=" * int(percent // 2) + " " * (50 - int(percent // 2))
		if percent == 100:
			bar = "=" * 49 + "🌷"
		print(f"\r{percent:.0f}%[{bar}] {i + 1}/{total}", end='')
		yield i
	print()