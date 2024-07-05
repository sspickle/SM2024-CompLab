import storage
import wifi

storage.remount("/", readonly=False)

if wifi.radio.ipv4_address:
    print("IP configured:", wifi.radio.ipv4_address)
else:
    print("No IP configured.")
    
print("Welcome to AAPT-SM24 Computation in the Lab workshop!")

