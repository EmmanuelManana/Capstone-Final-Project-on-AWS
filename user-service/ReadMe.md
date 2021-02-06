- read serverless.com docs on how to configure sls to work AWS
- npm install -g serverless
- serverless create --template aws-nodejs --name "my-special-service"
- sls deploy -v or sls dpeloy
- help, sls --help or sls -h

<!-- create a function though mocha -->
serverless create function -f testFunction --handler src/functions/testFunction.testFunction --path src/tests/