'use strict';
const bcrypt = require('bcryptjs')
const { ComputeOptimizer } = require('aws-sdk');
const AWS = require('aws-sdk')

module.exports.createUser = async (event, context) => {
  const body = JSON.parse(event.body)
  const username = body.username
  const password = body.password
  const salt = bcrypt.genSaltSync(10)
  const newUser = {
    TableName: process.env.DYNAMODB_USER_TABLE,
    Item: {
      pk: username,
      password: bcrypt.hashSync(password, salt)
    }
  }
  try {
    const dynamodb = new AWS.DynamoDB.DocumentClient()
    await dynamodb.put(newUser).promise()
    return {
      statusCode: 201,
      headers: {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Credentials': true,
        'Access-Control-Allow-Headers': 'Authorization'
      }
    }
  } catch(error) {
    console.log('Error creatign user')
    console.log('error creating user amigo:', error)
    console.log('newUserParams', newUserParams)
    return new Error('Error creatign user')
  }

};