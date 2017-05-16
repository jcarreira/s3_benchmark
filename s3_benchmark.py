from datetime import datetime
import boto3

# Let's use Amazon S3
s3 = boto3.resource('s3')

#for bucket in s3.buckets.all():
#    print(bucket.name)

print "Testing latency"

# test latency
data = "a"

for i in range(0,100):
	bef = datetime.now()
	s3.Bucket('pywrenbucket').put_object(Key='lat', Body=data)
	after = datetime.now()

	elapsed = after - bef
	print(elapsed.microseconds)


print("Testing bandwidth")

# test bandwidth
def repeat_to_length(string_to_expand, length):
   return (string_to_expand * ((length/len(string_to_expand))+1))[:length]

size = 10 * 1024 * 1024; # 10 MB
data = repeat_to_length('abcdef', size)

for i in range(0,100):
	bef = datetime.now()
	s3.Bucket('pywrenbucket').put_object(Key='bw', Body=data)
	after = datetime.now()

	elapsed = after - bef

	bw = 1.0 * size / elapsed.microseconds * 1000 * 1000
	bw = bw / 1024 / 1024 # translate to MB
	print("MB/sec: ", bw)
