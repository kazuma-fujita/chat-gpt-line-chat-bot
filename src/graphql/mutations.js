/* eslint-disable */
// this is an auto generated file. This will be overwritten

export const createMessages = /* GraphQL */ `
  mutation CreateMessages(
    $input: CreateMessagesInput!
    $condition: ModelMessagesConditionInput
  ) {
    createMessages(input: $input, condition: $condition) {
      id
      lineUserId
      content
      role
      createdAt
      updatedAt
    }
  }
`;
export const updateMessages = /* GraphQL */ `
  mutation UpdateMessages(
    $input: UpdateMessagesInput!
    $condition: ModelMessagesConditionInput
  ) {
    updateMessages(input: $input, condition: $condition) {
      id
      lineUserId
      content
      role
      createdAt
      updatedAt
    }
  }
`;
export const deleteMessages = /* GraphQL */ `
  mutation DeleteMessages(
    $input: DeleteMessagesInput!
    $condition: ModelMessagesConditionInput
  ) {
    deleteMessages(input: $input, condition: $condition) {
      id
      lineUserId
      content
      role
      createdAt
      updatedAt
    }
  }
`;
export const createVoiceMessages = /* GraphQL */ `
  mutation CreateVoiceMessages(
    $input: CreateVoiceMessagesInput!
    $condition: ModelVoiceMessagesConditionInput
  ) {
    createVoiceMessages(input: $input, condition: $condition) {
      id
      sessionId
      content
      role
      createdAt
      updatedAt
    }
  }
`;
export const updateVoiceMessages = /* GraphQL */ `
  mutation UpdateVoiceMessages(
    $input: UpdateVoiceMessagesInput!
    $condition: ModelVoiceMessagesConditionInput
  ) {
    updateVoiceMessages(input: $input, condition: $condition) {
      id
      sessionId
      content
      role
      createdAt
      updatedAt
    }
  }
`;
export const deleteVoiceMessages = /* GraphQL */ `
  mutation DeleteVoiceMessages(
    $input: DeleteVoiceMessagesInput!
    $condition: ModelVoiceMessagesConditionInput
  ) {
    deleteVoiceMessages(input: $input, condition: $condition) {
      id
      sessionId
      content
      role
      createdAt
      updatedAt
    }
  }
`;
