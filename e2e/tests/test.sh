rm -rf /results/*
bash /backend/wait-for-it frontend:8080
sh /tests/test.sh
curl webserver:8080 >> /output/out
