
import requests


class MaidWhite(object):



	def __init__(self, username_or_access_token=None, password=None):
		self.host = "https://www.tih.tw"
		if password is not None:
			# get access_token
			response = self.get_access_token(username_or_access_token, password)
			if response == None:
				print("Warning, username or password incorrect.")
			else:
				self.access_token = response['access_token']
		elif username_or_access_token is not None:
			self.access_token = username_or_access_token



	def get_access_token(self, username=None, password=None):
		data = {
			"username": username,
			"password": password,
		}
		r = requests.post(self.host + "/2/token", data=data)
		if r.status_code != requests.codes.ok:
			# error
			print(r.text)
			return None
		response = r.json()
		print(response)
		return response

	def __call_get_api(self, path=""):
		header = {
			"Authorization": "Bearer " + self.access_token
		}
		r = requests.get(self.host + path, headers=header)
		if r.status_code != requests.codes.ok:
			# error
			print(r.text)
			return None
		response = r.json()
		print(response)
		return response



	def get_user_info(self):
		return self.__call_get_api("/2/me")

	def get_devices(self):
		response = self.__call_get_api("/2/devices")
		if response is None:
			return None

		return [Device(client=self, obj=x) for x in response['devices']]


	# def find_devices_
class Device(object):

	def __init__(self, client=None, obj=None, device_id=None):
		self.client = client
		if obj is not None:
			self.id = str(obj['id'])
			self.display_name = obj['display_name']
		else:
			self.id = str(device_id)
			state = self.get_state()
			self.display_name = state['display_name']

	def __repr__(self):
		return "device: " + self.display_name + " id: " + self.id 


	def __call_get_api(self, path=""):
		header = {
			"Authorization": "Bearer " + self.client.access_token
		}
		r = requests.get(self.client.host + path, headers=header)
		if r.status_code != requests.codes.ok:
			# error
			print(r.text)
			return None
		response = r.json()
		print(response)
		return response


	def get_state(self):
		return self.__call_get_api("/2/devices/" + self.id)

	def set_state(self, payload=None):
		header = {
			"Authorization": "Bearer " + self.client.access_token
		}
		r = requests.post(self.client.host + "/2/devices/" + self.id, headers=header, data=payload)
		if r.status_code != requests.codes.ok:
			# error
			print(r.text)
			return None
		response = r.json()
		print(response)
		return response

	def get_power_status(self):
		response = self.get_state()

		return response['power_status']

	def set_power_status(self, power_status):
		val = "false"
		if power_status == True:
			val = "true"
		return self.set_state({"power_status": val})



