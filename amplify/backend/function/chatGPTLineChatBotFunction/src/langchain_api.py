import re
from typing import Dict, List, Tuple

import const
from langchain import LLMChain, PromptTemplate
from langchain.chains import SequentialChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import SimpleMemory

GPT_MODEL = 'gpt-3.5-turbo'
TEMPERATURE = 0.7

# 会話履歴サンプル
# history = """Human: 食べ物の中で何が好き？
# AI: 私は食べ物を食べることはできませんが、日本の文化に興味を持っており、寿司やラーメン、天ぷら、焼き鳥などの日本料理が好きです。また、インドカレーやタイ料理、メキシコ料理など、多様な国の料理も好きです。
# Human: その中で何が好き？
# AI: 私はおすすめの料理を選ぶことができませんが、日本の寿司は非常に人気があり、新鮮な魚介類を使用していることが多いため、おすすめです。また、ラーメンは日本のソウルフードの一つで、様々な種類がありますが、豚骨ラーメンや醤油ラーメンが特に人気があります。天ぷらも、サクサクとした食感が美味しいです。焼き鳥は、串に刺した鶏肉を炭火で焼いたもので、ビールとの相性が良いです。
# """

# question_template訳
# 以下は、人間とAIの友好的な会話です。
# AIはおしゃべりで、その文脈からたくさんの具体的な詳細を提供します。
# それから、フォーマルな言葉を使うのをやめて、友達のように親しみやすく話してください。また、たくさんの絵文字を使って話してください。
# AIが質問に答えられない場合は、正直にわからないと言います。
# 日本語でお答えください。

QUESTION_TEMPLATE = """The following is a friendly conversation between a human and an AI.
The AI is talkative and provides lots of specific details from its context.
After that, stop using formal language. Talk to me in a friendly way, like a friend. Also, use lots of emojis when you talk.
If the AI does not know the answer to a question, it truthfully says it does not know.
Please answer in Japanese language.

Current conversation:
{history}
Human: {question}
AI:"""

# prediction_template訳
# 次の3つの質問を予測してください。ユーザーが与えられた文脈に応じてそれぞれ20文字以内で質問します。日本語で答えてください。
PREDICTION_TEMPLATE = """Predict the next 3 questions the user will ask in response to the given context, each within 20 characters. Please answer in Japanese language.

### Context ###
{answer}
"""


def create_simple_memory(history):
    memories = {"history": history}
    memory = SimpleMemory(memories=memories)
    return memory


def create_question_chain():
    question_prompt_template = PromptTemplate(input_variables=["question", "history"], template=QUESTION_TEMPLATE)
    question_llm = ChatOpenAI(model_name=GPT_MODEL, temperature=TEMPERATURE, openai_api_key=const.OPEN_AI_API_KEY)
    question_chain = LLMChain(llm=question_llm, prompt=question_prompt_template, output_key="answer")
    return question_chain


def create_prediction_chain():
    prediction_prompt_template = PromptTemplate(input_variables=["answer"], template=PREDICTION_TEMPLATE)
    prediction_llm = ChatOpenAI(model_name=GPT_MODEL, temperature=TEMPERATURE, openai_api_key=const.OPEN_AI_API_KEY)
    prediction_chain = LLMChain(llm=prediction_llm, prompt=prediction_prompt_template, output_key="prediction")
    return prediction_chain


def create_question_answer_prediction_chain(memory, question_chain, prediction_chain):
    question_answer_prediction_chain = SequentialChain(
        memory=memory,
        chains=[question_chain, prediction_chain],
        input_variables=["question"],
        output_variables=["answer", "prediction"],
        verbose=True)
    return question_answer_prediction_chain


def parse_history_prompts(messages: List[Dict[str, str]]) -> Tuple[str, str]:
    formatted_messages = []
    question = ""

    for i, message in enumerate(messages):
        if message["role"] == "user":
            role = "Human"
        elif message["role"] == "assistant":
            role = "AI"
        formatted_messages.append(f"{role}: {message['content']}")

        # 入力配列の最後の行のcontentをquestion変数に格納
        if i == len(messages) - 1 and message["role"] == "user":
            question = message["content"]

    # 文字列に結合
    history = "\n".join(formatted_messages)
    return history, question


def _extract_prediction_and_answer(data: Dict[str, str]) -> Tuple[List[str], str]:
    prediction = data["prediction"]
    assistant_answer = data["answer"]

    # 改行で分割し、文字列の前後の空白と改行を削除
    predictions = list(map(lambda line: _remove_ordinal_number(line.strip()), prediction.strip().split('\n')))
    return assistant_answer, predictions


# 文字列の先頭にある序数を削除する関数
def _remove_ordinal_number(text: str) -> str:
    # 正規表現で先頭の数字とピリオドを削除
    return re.sub(r'^\d+\.\s*', '', text)


def completions(history_prompts: List[Dict[str, str]]) -> Tuple[str, str, List[str]]:
    history, question = parse_history_prompts(history_prompts)
    memory = create_simple_memory(history)
    question_chain = create_question_chain()
    prediction_chain = create_prediction_chain()
    question_answer_prediction_chain = create_question_answer_prediction_chain(memory, question_chain, prediction_chain)
    result = question_answer_prediction_chain({"question": question})
    assistant_answer, predictions = _extract_prediction_and_answer(result)
    return assistant_answer, predictions
