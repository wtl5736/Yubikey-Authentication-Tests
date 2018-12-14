"""
Name: Yubikey_EfficiencyandError_Test.py
Author: Wesley Lee - wtl5736@rit.edu
Assignment: Authentication Project CSEC-472
Date Created: 12-05-2018

Description:
    Tests the Efficiency and Infrequent Error of a Yubikey
"""

import yubico_client
import time

times_list = list()

for x in range(100):
	try:
		start = time.time()
		client = yubico_client.Yubico(client_id= 'ENTER CLIENT ID HERE',
			key='ENTER API KEY HERE')

		otp = input("Enter OTP: ")
		print(client.verify(otp))
		
		end = time.time()
		final_time = end - start
		times_list.append(final_time)
		
		
	except yubico_client.yubico_exceptions.SignatureVerificationError as e:
		print("Verification Failed!")
		print("Verification Error: %s" % e)
		
		end = time.time()
		print(end - start)

total = 0
for y in range(len(times_list)):
	total += times_list[y]
	
print("Total Time:", total)
print("Average Time:", total/len(times_list))