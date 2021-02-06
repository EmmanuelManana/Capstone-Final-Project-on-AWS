'use strict';
const { ComputeOptimizer } = require('aws-sdk');
const AWS = require('aws-sdk')

module.exports.createUser = async (event, context) => {

  const body = JSON.parse(event.body);
  const username = body.username;
  const password = body.password;

  const newUser = {
    TableName: process.env.DYNAMODB_USER_TABLE,
    Item: {
      pk: username,
      password: password
    }
  }

  try {
    const dynamodb = new AWS.DynamoDB.DocumentClient();
    await dynamodb.put(newUser).promise();

    return {
      statusCode: 201,
      headers:{
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Credentials': true,
        'Access-Control-Allow-Headers': 'Authorization'
      }
    };

  } catch (erro) {
    console.error("User Creation erro Error")
    console.log("new user", newUser);
    return new Error("User Creation erro Error");
  }

};
