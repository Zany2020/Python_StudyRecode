from Object_oriented.cmobilephone import CMobilePhone


class FoldPhone(CMobilePhone):
	def __init__(self, brand: str, model: str, length: float, width: float, height: float,
	             user: str, number: str, screen_size: float, resolution: str,
	             screen_tech: str, screen_manu: str, battery_cap: int,is_folded: bool):
		super().__init__(brand, model, length, width, height, user, number,
		                 screen_size, resolution, screen_tech, screen_manu, battery_cap)
		self._is_folded = is_folded
	
	def toggle_fold(self):
		self._is_folded = not self._is_folded
		status = "折叠" if self._is_folded else "展开"
		print(f"{self.model} 当前状态：{status}")
	
	def show_info(self):
		super().show_info()
		fold_status = "已折叠" if self._is_folded else "已展开"
		print(f"折叠状态：{fold_status}")
	
	





