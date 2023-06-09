from langchain.chat_models import ChatOpenAI
import itertools
from langchain.llms.base import LLM
import streamlit as st

from demo.synthesizers.json_synthesizer.json_synthesizer_chain import JsonSynthesizerChain

@st.cache_data
def synthesize(text: str, num_questions: int = 1, _llm: LLM = ChatOpenAI(temperature=0)):
    """
    Generate prompt set
    @param text: text to generate prompt set from
    @param num_questions: number of prompts to generate
    @return: prompt set as JSON list
    """
    st.info("`Generating eval set ...`")
    chain = JsonSynthesizerChain.from_llm(_llm)
    prompt_set = []
    for _ in range(num_questions):
        qa = chain.run(text)
        prompt_set.append(qa)

    prompt_set_full = list(itertools.chain.from_iterable(prompt_set))
    return prompt_set_full