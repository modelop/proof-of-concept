from multiprocessing import Pool
import multiprocessing
import os

def tester(url):
	output = os.popen(url).read()
	return output

goodurls = ['curl -k -X POST -d @string.json https://localhost:8000/api/1/service/engine-1/2/active/model/roundtrip/0/1', 'curl -k -X POST -d @string.json https://localhost:8000/api/1/service/engine-1/2/active/model/roundtrip/0/1', 'curl -k -X POST -d @string.json https://localhost:8000/api/1/service/engine-1/2/active/model/roundtrip/0/1', 'curl -k -X POST -d @string.json https://localhost:8000/api/1/service/engine-1/2/active/model/roundtrip/0/1', 'curl -k -X POST -d @string.json https://localhost:8000/api/1/service/engine-1/2/active/model/roundtrip/0/1', 'curl -k -X POST -d @string.json https://localhost:8000/api/1/service/engine-1/2/active/model/roundtrip/0/1']
evilurls = ['curl -k -X POST -d @text.json https://localhost:8000/api/1/service/engine-1/2/active/model/roundtrip/0/1', 'curl -k -X POST -d @text.json https://localhost:8000/api/1/service/engine-1/2/active/model/roundtrip/0/1','curl -k -X POST -d @text.json https://localhost:8000/api/1/service/engine-1/2/active/model/roundtrip/0/1','curl -k -X POST -d @text.json https://localhost:8000/api/1/service/engine-1/2/active/model/roundtrip/0/1','curl -k -X POST -d @text.json https://localhost:8000/api/1/service/engine-1/2/active/model/roundtrip/0/1','curl -k -X POST -d @text.json https://localhost:8000/api/1/service/engine-1/2/active/model/roundtrip/0/1','curl -k -X POST -d @text.json https://localhost:8000/api/1/service/engine-1/2/active/model/roundtrip/0/1']
num_cores = multiprocessing.cpu_count()

p = Pool(num_cores)
results = []
results.append(p.map(tester, evilurls)) 
results.append(p.map(tester, evilurls))

print(results)



