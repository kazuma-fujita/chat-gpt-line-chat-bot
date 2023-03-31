/* eslint-disable */
// this is an auto generated file. This will be overwritten

export const onCreateMessages = /* GraphQL */ `
  subscription OnCreateMessages($filter: ModelSubscriptionMessagesFilterInput) {
    onCreateMessages(filter: $filter) {
      id
      lineUserId
      content
      role
      createdAt
      updatedAt
    }
  }
`;
export const onUpdateMessages = /* GraphQL */ `
  subscription OnUpdateMessages($filter: ModelSubscriptionMessagesFilterInput) {
    onUpdateMessages(filter: $filter) {
      id
      lineUserId
      content
      role
      createdAt
      updatedAt
    }
  }
`;
export const onDeleteMessages = /* GraphQL */ `
  subscription OnDeleteMessages($filter: ModelSubscriptionMessagesFilterInput) {
    onDeleteMessages(filter: $filter) {
      id
      lineUserId
      content
      role
      createdAt
      updatedAt
    }
  }
`;
export const onCreateVoiceMessages = /* GraphQL */ `
  subscription OnCreateVoiceMessages(
    $filter: ModelSubscriptionVoiceMessagesFilterInput
  ) {
    onCreateVoiceMessages(filter: $filter) {
      id
      sessionId
      content
      role
      createdAt
      updatedAt
    }
  }
`;
export const onUpdateVoiceMessages = /* GraphQL */ `
  subscription OnUpdateVoiceMessages(
    $filter: ModelSubscriptionVoiceMessagesFilterInput
  ) {
    onUpdateVoiceMessages(filter: $filter) {
      id
      sessionId
      content
      role
      createdAt
      updatedAt
    }
  }
`;
export const onDeleteVoiceMessages = /* GraphQL */ `
  subscription OnDeleteVoiceMessages(
    $filter: ModelSubscriptionVoiceMessagesFilterInput
  ) {
    onDeleteVoiceMessages(filter: $filter) {
      id
      sessionId
      content
      role
      createdAt
      updatedAt
    }
  }
`;
