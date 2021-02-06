'use strict';
const { ComputeOptimizer } = require('aws-sdk');
const AWS = require('aws-sdk')
const bycrpt = require('bcryptjs')

module.exports.createUser = async (event, context) => {
  const salt = await bcryptjs.genSalt(10)
  const body = JSON.parse(event.body)
  const username = body.username
  const password = body.password
  const newUser = {
    TableName: process.env.DYNAMODB_USER_TABLE,
    Item: {
      pk: username,
      password: bycrpt.hashSync(password, salt)
    }
  }
  try {
    const dynamodb = new AWS.DynamoDB.DocumentClient()
    const registerUser = await dynamodb.put(newUser).promise()
    return {
      statusCode: 201,
      headers: {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Credentials': true,
        'Access-Control-Allow-Headers': 'Authorization'
      }
    }
  } catch(Error) {
    console.log('Error create new User')
    console.log('putError', Error)
    console.log('newUser Payload', newUser)
    return new Error('Error create new User')
  }

};