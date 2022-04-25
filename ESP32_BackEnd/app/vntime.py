import arrow

class VnTimestamp:
	@staticmethod
	def today_8am():
		dateNow = arrow.utcnow().to("Asia/Ho_Chi_Minh").date()
		hourNow = arrow.utcnow().to("Asia/Ho_Chi_Minh").time().hour
		if hourNow >=8:
			return(arrow.get(dateNow).shift(hours=8).timestamp - 25200)
		else:
			return(arrow.get(dateNow).shift(hours=-16).timestamp - 25200)
	
	@staticmethod
	def tomorrow_8am():
		tomorrow = VnTimestamp.today_8am() +  86400
		return tomorrow

	@staticmethod
	def now():
		return arrow.utcnow().to("Asia/Ho_Chi_Minh").timestamp

	@staticmethod
	def work_start(date):
		""" Lấy ngày theo giờ hiện tại
		"""
		hourNow = arrow.utcnow().to("Asia/Ho_Chi_Minh").time().hour
		if hourNow >= 8:
			return arrow.get(date + ' 01:00:00', 'DD-MM-YYYY HH:mm:ss').timestamp
		else: 
			return arrow.get(date + ' 01:00:00', 'DD-MM-YYYY HH:mm:ss').shift(days=-1).timestamp

	@staticmethod
	def work_end(date):
		work_end = VnTimestamp.work_start(date) +  86399
		return work_end
	
	@staticmethod
	def day_start(date):
		return arrow.get(date, "DD-MM-YYYY", tzinfo="Asia/Ho_Chi_Minh").timestamp

	@staticmethod
	def day_end(date):
		return arrow.get(date, "DD-MM-YYYY", tzinfo="Asia/Ho_Chi_Minh").shift(days=1).timestamp - 1

	def today_start():
		dateNow = arrow.utcnow().to("Asia/Ho_Chi_Minh").date()
		return(arrow.get(dateNow).timestamp - 25200)
	
	@staticmethod
	def today_end():
		return VnTimestamp.today_start() +  86399

	@staticmethod
	def get_date_str(timestamp):
		"""
		Trả ra ngày tháng năm từ timestamp
		"""
		return arrow.get(timestamp, tzinfo="Asia/Ho_Chi_Minh").format("DD-MM-YYYY")
	@staticmethod
	def get_time_str(timestamp):
		""" Trả ra string HH:mm từ timestamp dầu vào

		"""
		return arrow.get(timestamp, tzinfo="Asia/Ho_Chi_Minh").format("HH:mm:ss")

	@staticmethod
	def get_date_time_str(timestamp):
		""" Trả ra string HH:mm/DD-MM-YYY từ timestamp dầu vào

		"""
		return arrow.get(timestamp, tzinfo="Asia/Ho_Chi_Minh").format("HH:mm/DD-MM-YYYY")


	@staticmethod
	def month_start():
		""" Trả ra timestamp của ngày đầu tiên trong tháng
  
		"""
		now = arrow.utcnow().timestamp
		date=arrow.get(now, tzinfo="Asia/Ho_Chi_Minh").format("DD-MM-YYYY")
		date = "01" + date[2:]
		return arrow.get(date, "DD-MM-YYYY", tzinfo="Asia/Ho_Chi_Minh").timestamp
