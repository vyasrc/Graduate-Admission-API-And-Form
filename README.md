# Graduate-Admission-API-And-Form
A Machine Learning API and website to predict the chances of getting into a graduate program.

* Created a REST API, using Django to predict the chance of a person’s admission to a graduate school based on various parameters, using Python Language.
* Trained a neural network, using Keras API with Tensorflow backend on Google Colab and saved the model as a pickle file.
* Used a publicly available graduate admission dataset form [Kaggle](https://www.kaggle.com/mohansacharya/graduate-admissions/tasks?taskId=6) for training and testing the network.
* Also using Django Forms and Bootstrap, created a Django web application, where the user can enter the values and see the results. 
* PostreSQL was used for the database access and the whole project was deployed to an AWS EC2 Instance.

### Steps to create a database and giving permissions to it in Postgresql.

* CREATE DATABASE myproject;
* CREATE USER myprojectuser WITH PASSWORD 'password'; or change password of postgres '\password postgres'
* ALTER ROLE myprojectuser SET client_encoding TO 'utf8';
* ALTER ROLE myprojectuser SET default_transaction_isolation TO 'read committed';
* ALTER ROLE myprojectuser SET timezone TO 'UTC';
* GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser;                                                                            

![](https://github.com/vyasrc/Graduate-Admission-API-And-Form/blob/master/admission.png)
