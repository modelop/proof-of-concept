fastscore use engine-1
fastscore engine reset
fastscore run xgboost_iris-py3 rest-trip rest-trip

curl -i -k -u fastscore:fastscore -H "Content-Type: application/json" --data-binary "@xgboost_iris_single.json" https://localhost:8000/api/1/service/engine-1/2/active/model/roundtrip/0/1
