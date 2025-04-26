# Tech Stack
![image](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue) ![image](https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white) ![image](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white) ![image](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=Selenium&logoColor=white) ![image](https://img.shields.io/badge/Jenkins-D24939?style=for-the-badge&logo=Jenkins&logoColor=white)
![image](https://img.shields.io/badge/Helm-0F1689?style=for-the-badge&logo=Helm&labelColor=0F1689) ![image](https://img.shields.io/badge/Docker%20Compose-2496ED?style=for-the-badge&logo=docker&logoColor=white)

# Steps to run it yourself
1. Download required files
```
git clone https://github.com/ShaharRubel/DevopsExpertAdvanced.git
pip install pymysql flask requests selenium
```
2. cd into direcotry
```commandline
cd DevopsProject
```
3. run helm chart
```commandline
helm install mywebapp user-api
```
4. portforward to access frontend and backend
```commandline
kubectl port-forward service/backend-service 5000:5000
kubectl port-forward service/frontend-service 5001:5001
```

# Steps to setup jenkins pipeline
1. setup credential named "dockerhub_id" with docker hub credentials
2. add a windows node to jenkins
3. create pipeline project and choose "pipeline script from scm"
4. choose branch main
5. choose build now

## Using postman collection
1. locate DevopsProject.postman_collection.json
2. click import collection in Postman
3. copy file to window prompt