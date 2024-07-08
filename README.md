# Awesome-GenAI [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
Welcome to Awesome-GenAI! This repository is a curated collection of resources, tools, frameworks, and information related to Generative AI. Whether you are a beginner looking to learn about the basics or an experienced developer searching for the latest advancements in the field, this repository aims to provide valuable insights and resources to help you on your journey.

_If you want to contribute to this list (please do), send me a pull request or contact me.
Also, a listed repository should be deprecated if:

* Repository's owner explicitly says that "this library is not maintained".
* Not committed for a long time (2~3 years).

Further resources:

* For a list of free GenAI books available for download, go [here](https://github.com/onebirdrocks/Awesome-GenAI/blob/main/books.md).
* For a list of (mostly) free GenAI courses available online, go [here](https://github.com/onebirdrocks/Awesome-GenAI/blob/main/courses.md).
* For a list of professional or free-to-attend meetups and local GenAI events, go [here](https://github.com/onebirdrocks/Awesome-GenAI/blob/main/events.md).



## What is Generative AI?
Generative AI refers to a class of AI algorithms that generate new content, such as text, images, and audio, based on the data they are trained on. These models can create realistic and innovative outputs, making them useful in various applications like content creation, design, and entertainment.

<img src="./What-is-GenAI" alt="./What-is-GenAI" width="60%"/>

This diagram illustrates the hierarchical relationship between AI, Machine Learning, Deep Learning, GenAI, and LLM:
- **AI**  encompasses all technologies that simulate human intelligence.
- **Machine Learning** is a subset of AI, emphasizing learning from data and algorithms.
- **Deep Learning** is a subset of Machine Learning, utilizing multi-layer neural networks to handle complex data.
- **GenAI** (Generative AI) is an application of Deep Learning, focusing on generating new data.
- **LLM** (Large Language Models) is a branch of GenAI, specifically large-scale neural networks that generate and understand natural language text.

## Table of Contents
- Introduction
    - Overview of the project
    - Basic concepts of Generative AI
    - Contribution guidelines
- Learning Resources
    - Online courses
    - Books and papers
    - Tutorials
    - Workshops and conferences
- Tools and Frameworks
    - Development Frameworks
    - Open-source projects
- Models
    - Pre-trained models
    - Natural Language Processing models
    - Computer Vision models
    - Multimodal models
- Applications
    - Text generation
    - Image generation
    - Audio generation
    - Video generation
    - Other applications
- Datasets
    - Available datasets
    - Data collection and processing methods
    - Data augmentation techniques
- Research and Papers
    - Latest research updates
    - Important paper reviews
    - Research trends and hotspots
- Community and Events
    - Online and offline communities
    - Events and conferences
    - Projects and Case Studies
    - Success stories
    - Project showcases
    - Practical experience sharing
- Miscellaneous
    - Frequently Asked Questions
    - Useful tips
    - Recommended resources

 ## Learning Resources
 ### Paper
 - [Attention Is All You Need](https://arxiv.org/abs/1706.03762) - Most modern LLMs rely on the transformer architecture, which is a deep neural network architecture introduced in the 2017 paper "Attention Is All You Need"
 ### Tutorials 
 - [Let's build GPT: from scratch, in code, spelled out.](https://www.youtube.com/watch?v=kCc8FmEb1nY)

 ## Models
 ### Open Models 
- Meta
  - [Llama 3-8|70B](https://llama.meta.com/llama3/)
  - [Llama 2-7|13|70B](https://llama.meta.com/llama2/)
  - [Llama 1-7|13|33|65B](https://ai.facebook.com/blog/large-language-model-llama-meta-ai/)
  - [OPT-1.3|6.7|13|30|66B](https://arxiv.org/abs/2205.01068)
- Google
  - [Gemma2-9|27B](https://blog.google/technology/developers/google-gemma-2/)
  - [Gemma-2|7B](https://blog.google/technology/developers/gemma-open-models/)
  - [RecurrentGemma-2B](https://github.com/google-deepmind/recurrentgemma)
  - [T5](https://arxiv.org/abs/1910.10683)
- Microsoft
  - [Phi1-1.3B](https://huggingface.co/microsoft/phi-1)
  - [Phi2-2.7B](https://huggingface.co/microsoft/phi-2)
  - [Phi3-3.8|7|14B](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct)
- Apple
  - [OpenELM-1.1|3B](https://huggingface.co/apple/OpenELM)
- Stability AI
  - [StableLM-3B](https://huggingface.co/collections/stabilityai/stable-lm-650852cfd55dd4e15cdcb30a)
  - [StableLM-v2-1.6|12B](https://huggingface.co/collections/stabilityai/stable-lm-650852cfd55dd4e15cdcb30a)
  - [StableCode-3B](https://huggingface.co/collections/stabilityai/stable-code-64f9dfb4ebc8a1be0a3f7650)
- DataBricks
  - [MPT-7B](https://www.databricks.com/blog/mpt-7b)
  - [DBRX-132B-MoE](https://www.databricks.com/blog/introducing-dbrx-new-state-art-open-llm)
- Alibaba
  - [Qwen-1.8|7|14|72B](https://huggingface.co/collections/Qwen/qwen-65c0e50c3f1ab89cb8704144)
  - [Qwen1.5-1.8|4|7|14|32|72|110B](https://huggingface.co/collections/Qwen/qwen15-65c0a2f577b1ecb76d786524)
  - [CodeQwen-7B](https://huggingface.co/Qwen/CodeQwen1.5-7B)
  - [Qwen-VL-7B](https://huggingface.co/Qwen/Qwen-VL)
  - [Qwen2-0.5|1.5|7|57-MOE|72B](https://qwenlm.github.io/blog/qwen2/)

## Tools & Frameworks
### Development Frameworks
- [Langchain](https://github.com/langchain-ai/langchain) - Build context-aware reasoning applications. [![Forks](https://img.shields.io/github/forks/langchain-ai/langchain?style=social)](https://github.com/langchain-ai/langchain/network/members) [![Stars](https://img.shields.io/github/stars/langchain-ai/langchain?style=social)](https://github.com/langchain-ai/langchain/stargazers)
- [LamaIndex](https://github.com/run-llama/llama_index) - LlamaIndex is a data framework for your LLM applications. [![Forks](https://img.shields.io/github/forks/run-llama/llama_index?style=social)](https://github.com/run-llama/llama_index/network/members) [![Stars](https://img.shields.io/github/stars/run-llama/llama_index?style=social)](https://github.com/run-llama/llama_index/stargazers)
- [Flowise](https://github.com/FlowiseAI/Flowise) - Drag & drop UI to build your customized LLM flow. [![Forks](https://img.shields.io/github/forks/FlowiseAI/Flowise?style=social)](https://github.com/FlowiseAI/Flowise/network/members) [![Stars](https://img.shields.io/github/stars/FlowiseAI/Flowise?style=social)](https://github.com/FlowiseAI/Flowise/stargazers)
- [Auto-GPT](https://github.com/Significant-Gravitas/AutoGPT) - AutoGPT is the vision of accessible AI for everyone, to use and to build on. Our mission is to provide the tools, so that you can focus on what matters. [![Forks](https://img.shields.io/github/forks/Significant-Gravitas/AutoGPT?style=social)](https://github.com/Significant-Gravitas/AutoGPT/network/members) [![Stars](https://img.shields.io/github/stars/Significant-Gravitas/AutoGPT?style=social)](https://github.com/Significant-Gravitas/AutoGPT/stargazers)
- [AgentGPT](https://github.com/reworkd/AgentGPT) - Assemble, configure, and deploy autonomous AI Agents in your browser. [![Forks](https://img.shields.io/github/forks/reworkd/AgentGPT?style=social)](https://github.com/reworkd/AgentGPT/network/members) [![Stars](https://img.shields.io/github/stars/reworkd/AgentGPT?style=social)](https://github.com/reworkd/AgentGPT/stargazers)
- [GraphRAG](https://github.com/microsoft/graphrag) - A modular graph-based Retrieval-Augmented Generation (RAG) system. [![Forks](https://img.shields.io/github/forks/microsoft/graphrag?style=social)](https://github.com/microsoft/graphrag/network/members) [![Stars](https://img.shields.io/github/stars/microsoft/graphrag?style=social)](https://github.com/microsoft/graphrag/stargazers)




### Open-source projects
#### TTS
- [OpenVoice](https://github.com/myshell-ai/OpenVoice) - a versatile instant voice cloning approach that requires only a short audio clip from the reference speaker to replicate their voice and generate speech in multiple languages. [![Forks](https://img.shields.io/github/forks/myshell-ai/OpenVoice?style=social)](https://github.com/myshell-ai/OpenVoice/network/members) [![Stars](https://img.shields.io/github/stars/myshell-ai/OpenVoice?style=social)](https://github.com/myshell-ai/OpenVoice/stargazers)
- [Coqui TTS](https://github.com/coqui-ai/TTS) - A deep learning toolkit for Text-to-Speech, battle-tested in research and production. [![Forks](https://img.shields.io/github/forks/coqui-ai/TTS?style=social)](https://github.com/coqui-ai/TTS/network/members) [![Stars](https://img.shields.io/github/stars/coqui-ai/TTS?style=social)](https://github.com/coqui-ai/TTS/stargazers)
- [NeMo](https://github.com/NVIDIA/NeMo) - A scalable generative AI framework built for researchers and developers working on Large Language Models, Multimodal, and Speech AI (Automatic Speech Recognition and Text-to-Speech). [![Forks](https://img.shields.io/github/forks/NVIDIA/NeMo?style=social)](https://github.com/NVIDIA/NeMo/network/members) [![Stars](https://img.shields.io/github/stars/NVIDIA/NeMo?style=social)](https://github.com/NVIDIA/NeMo/stargazers)
- [Vits](https://github.com/jaywalnut310/vits) -  Conditional Variational Autoencoder with Adversarial Learning for End-to-End Text-to-Speech. [![Forks](https://img.shields.io/github/forks/jaywalnut310/vits?style=social)](https://github.com/jaywalnut310/vits/network/members) [![Stars](https://img.shields.io/github/stars/jaywalnut310/vits?style=social)](https://github.com/jaywalnut310/vits/stargazers)
- [tacotron](https://github.com/keithito/tacotron) - A TensorFlow implementation of Google's Tacotron speech synthesis with pre-trained model (unofficial). [![Forks](https://img.shields.io/github/forks/keithito/tacotron?style=social)](https://github.com/keithito/tacotron/network/members) [![Stars](https://img.shields.io/github/stars/keithito/tacotron?style=social)](https://github.com/keithito/tacotron/stargazers)
- [tacotron2](https://github.com/NVIDIA/tacotron2) - PyTorch implementation with faster-than-realtime inference. [![Forks](https://img.shields.io/github/forks/NVIDIA/tacotron2?style=social)](https://github.com/NVIDIA/tacotron2/network/members) [![Stars](https://img.shields.io/github/stars/NVIDIA/tacotron2?style=social)](https://github.com/NVIDIA/tacotron2/stargazers)
- [FastSpeech](https://github.com/ming024/FastSpeech2) - An implementation of Microsoft's "FastSpeech 2: Fast and High-Quality End-to-End Text to Speech. [![Forks](https://img.shields.io/github/forks/ming024/FastSpeech2?style=social)](https://github.com/ming024/FastSpeech2/network/members) [![Stars](https://img.shields.io/github/stars/ming024/FastSpeech2?style=social)](https://github.com/ming024/FastSpeech2/stargazers)


### Clothing(Visual Try on)
- [IDM-VTON](https://github.com/yisol/IDM-VTON) - IDM-VTON : Improving Diffusion Models for Authentic Virtual Try-on in the Wild. [![Forks](https://img.shields.io/github/forks/yisol/IDM-VTON?style=social)](https://github.com/yisol/IDM-VTON/network/members) [![Stars](https://img.shields.io/github/stars/yisol/IDM-VTON?style=social)](https://github.com/yisol/IDM-VTON/stargazers)
- [MagicClothing](https://github.com/ShineChen1024/MagicClothing) - Official implementation of Magic Clothing: Controllable Garment-Driven Image Synthesis. [![Forks](https://img.shields.io/github/forks/ShineChen1024/MagicClothing?style=social)](https://github.com/ShineChen1024/MagicClothing/network/members) [![Stars](https://img.shields.io/github/stars/ShineChen1024/MagicClothing?style=social)](https://github.com/ShineChen1024/MagicClothing/stargazers)
- [HR Viton](https://github.com/sangyun884/HR-VITON) - Official PyTorch implementation for the paper High-Resolution Virtual Try-On with Misalignment and Occlusion-Handled Conditions (ECCV 2022).
- [Dressing in order](https://github.com/cuiaiyu/dressing-in-order) - (ICCV'21) Official code of "Dressing in Order: Recurrent Person Image Generation for Pose Transfer, Virtual Try-on and Outfit Editing" by Aiyu Cui, Daniel McKee and Svetlana Lazebnik
- [Dress Code](https://github.com/aimagelab/dress-code) - Dress Code: High-Resolution Multi-Category Virtual Try-On. ECCV 2022. 
### Agent
- [BabyAGI](https://github.com/yoheinakajima/babyagi) - Python script that acts as an AI-powered task manager. [![Forks](https://img.shields.io/github/forks/yoheinakajima/babyagi?style=social)](https://github.com/yoheinakajima/babyagi/network/members) [![Stars](https://img.shields.io/github/stars/yoheinakajima/babyagi?style=social)](https://github.com/yoheinakajima/babyagi/stargazers)
- [SWE-agent](https://github.com/princeton-nlp/SWE-agent) - SWE-agent takes a GitHub issue and tries to automatically fix it, using GPT-4, or your LM of choice. It solves 12.47% of bugs in the SWE-bench evaluation set and takes just 1 minute to run. [![Forks](https://img.shields.io/github/forks/princeton-nlp/SWE-agent?style=social)](https://github.com/princeton-nlp/SWE-agent/network/members) [![Stars](https://img.shields.io/github/stars/princeton-nlp/SWE-agent?style=social)](https://github.com/princeton-nlp/SWE-agent/stargazers)
### Virtual Human
[MuseV](https://github.com/TMElyralab/MuseV) - MuseV: Infinite-length and High Fidelity Virtual Human Video Generation with Visual Conditioned Parallel Denoising by Tencent [![Forks](https://img.shields.io/github/forks/TMElyralab/MuseV?style=social)](https://github.com/TMElyralab/MuseV/network/members) [![Stars](https://img.shields.io/github/stars/TMElyralab/MuseV?style=social)](https://github.com/TMElyralab/MuseV/stargazers)
