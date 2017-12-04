from datetime import datetime
import boto3

# Let's use Amazon S3
s3 = boto3.resource('s3')
client = boto3.client('s3')

#for bucket in s3.buckets.all():
#    print(bucket.name)

print "Testing latency"

# test latency
data = "a"
s3.Bucket('pywrenbucket').put_object(Key='lat', Body=data)

total_elapsed = 0
for i in range(0,100):
	bef = datetime.now()
	#s3.Bucket('pywrenbucket').get_object(Key='lat', Body=data)
        obj = client.get_object(Bucket='pywrenbucket', Key='lat')
	after = datetime.now()

	elapsed = after - bef
        total_elapsed = total_elapsed + elapsed.microseconds

print("Average Latency (us): ", total_elapsed / 100)


print("Testing bandwidth")

# test bandwidth
def repeat_to_length(string_to_expand, length):
   return (string_to_expand * ((length/len(string_to_expand))+1))[:length]

size = 10 * 1024 * 1024; # 10 MB
data = repeat_to_length('abcdef', size)
s3.Bucket('pywrenbucket').put_object(Key='bw', Body=data)

total_bw = 0
for i in range(0,100):
	bef = datetime.now()
        obj = client.get_object(Bucket='pywrenbucket', Key='bw')
	after = datetime.now()

	elapsed = after - bef

	bw = 1.0 * size / elapsed.microseconds * 1000 * 1000
	bw = bw / 1024 / 1024 # translate to MB
        total_bw = total_bw + bw

print("Avg bw MB/sec: ", total_bw / 100)
