# fastapiplayground
Evaluating fast api for python models served via the api

Install the dependencies
`pip3 install "fastapi[standard]"`

Running the server
`fastapi dev main.py`


Deploying to AWS Beanstalk
create the requirements file for all library dependencies
and put all the dependency and version
use command
`pip3 show fastapi`

to get the version


to create the source bundle
`git archive -v -o deployments/irisappv1.zip --format=zip HEAD`

