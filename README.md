# Madarin Auto-Coder
The Mandarin Auto-Coder aims to build a Mandarin Large Language Model for coding questions, bridging the language gap in coding education and providing Mandarin
speakers with accessible and effective coding solutions and instructions. 

## Baseline Model
[TAIDE](https://huggingface.co/taide) was chosen as the LLM to be fine-tuned in this project. This LLM is a mandarin based LLM which is able for five tasks, summary, writing letter, writing essay, English to Chinese translation, and Chinese to English translation.

## Data Prepocessing
[Tested-22k-Python-Alpaca](https://huggingface.co/datasets/Vezora/Tested-22k-Python-Alpaca) dataset was used in this project. We translated selected examples from the dataset into
Mandarin, cleaned the data by removing non-functional code, and reformatted it into a chain-of-thought structure.

## Few-Shot Prompting

## Chain-of-Thought Prompting
<img src="./images/example.png" width="50%">

## Quantization and Low-Rank Adapters

## Sample Output
<img src="./images/output.png" width="100%">

  
For further details on the implementation and usage of the model, please refer to the [code](https://github.com/Dawson-ma/Auto-Coder-in-Madarin/blob/main/ProfessionalCoderInMadarin.ipynb) provided.
