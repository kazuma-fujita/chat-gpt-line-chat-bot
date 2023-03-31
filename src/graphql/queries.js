/* eslint-disable */
// this is an auto generated file. This will be overwritten

export const getMessages = /* GraphQL */ `
  query GetMessages($id: ID!) {
    getMessages(id: $id) {
      id
      lineUserId
      content
      role
      createdAt
      updatedAt
    }
  }
`;
export const listMessages = /* GraphQL */ `
  query ListMessages(
    $filter: ModelMessagesFilterInput
    $limit: Int
    $nextToken: String
  ) {
    listMessages(filter: $filter, limit: $limit, nextToken: $nextToken) {
      items {
        id
        lineUserId
        content
        role
        createdAt
        updatedAt
      }
      nextToken
    }
  }
`;
export const getVoiceMessages = /* GraphQL */ `
  query GetVoiceMessages($id: ID!) {
    getVoiceMessages(id: $id) {
      id
      sessionId
      content
      role
      createdAt
      updatedAt
    }
  }
`;
export const listVoiceMessages = /* GraphQL */ `
  query ListVoiceMessages(
    $filter: ModelVoiceMessagesFilterInput
    $limit: Int
    $nextToken: String
  ) {
    listVoiceMessages(filter: $filter, limit: $limit, nextToken: $nextToken) {
      items {
        id
        sessionId
        content
        role
        createdAt
        updatedAt
      }
      nextToken
    }
  }
`;
export const messagesByLineUserIdAndCreatedAt = /* GraphQL */ `
  query MessagesByLineUserIdAndCreatedAt(
    $lineUserId: String!
    $createdAt: ModelStringKeyConditionInput
    $sortDirection: ModelSortDirection
    $filter: ModelMessagesFilterInput
    $limit: Int
    $nextToken: String
  ) {
    messagesByLineUserIdAndCreatedAt(
      lineUserId: $lineUserId
      createdAt: $createdAt
      sortDirection: $sortDirection
      filter: $filter
      limit: $limit
      nextToken: $nextToken
    ) {
      items {
        id
        lineUserId
        content
        role
        createdAt
        updatedAt
      }
      nextToken
    }
  }
`;
export const voiceMessagesBySessionIdAndCreatedAt = /* GraphQL */ `
  query VoiceMessagesBySessionIdAndCreatedAt(
    $sessionId: String!
    $createdAt: ModelStringKeyConditionInput
    $sortDirection: ModelSortDirection
    $filter: ModelVoiceMessagesFilterInput
    $limit: Int
    $nextToken: String
  ) {
    voiceMessagesBySessionIdAndCreatedAt(
      sessionId: $sessionId
      createdAt: $createdAt
      sortDirection: $sortDirection
      filter: $filter
      limit: $limit
      nextToken: $nextToken
    ) {
      items {
        id
        sessionId
        content
        role
        createdAt
        updatedAt
      }
      nextToken
    }
  }
`;
