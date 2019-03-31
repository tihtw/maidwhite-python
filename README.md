# Maid White Python SDK


## Install

```
$ pip install maidwhite
```


## Usage 

```
from maidwhite import MaidWhite


# Get client with username and password
m = MaidWhite("username", "password")

# Get client with access token
m = MaidWhite("access_token")


# Get device list
l = m.get_devices()

# find device
ac = [x for x in l if x.display_name == "My Device"]

if len(ac) == 0:
	print("device not found")

my_device = ac[0]


# Get state
state = my_device.get_state()
print(state)

# Set state
my_device.set_state({"power_status": "true"})


# Get power status
power_status = my_device.get_power_status()
print(power_status)

# Set power status
my_device.set_power_status(True)

```





