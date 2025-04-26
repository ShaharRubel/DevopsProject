## Todo
1. update connection to use local db - done
2. implement retry logic to connection db - done
   1. rewrite queries with new DB name - done
3. add logic to create table - done
4. add environment variable to be used in a container
5. update compose to include 3 things: - done
   1. backend - done
   2. frontend - done
   3. db - done
6. update helm chart to deploy the application - in progress
   1. add secret kubernetes
   2. add configmap with url of mysql
7. build a jenkins pipeline - in progress


### Things to improve:
1. add different requirements for each image and host
2. add mysql replication cluster on kubernetes
3. add namespace to all templates



## commands
- helm install mywebapp user-api
- kubectl port-forward service/backend-service 5000:5000
- kubectl port-forward service/frontend-service 5001:5001
- kubectl port-forward service/mysql 3306:3306
- kubectl get secret mysql-secret -o json
- kubectl get secrets/mysql-secret -o jsonpath="{.data.mysql-password}"