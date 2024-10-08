# Awesome-GenAI [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
Welcome to Awesome-GenAI! This repository is a curated collection of resources, tools, frameworks, and information related to Generative AI. Whether you are a beginner looking to learn about the basics or an experienced developer searching for the latest advancements in the field, this repository aims to provide valuable insights and resources to help you on your journey.

_If you want to contribute to this list (please do), send me a pull request or contact me.
Also, a listed repository should be deprecated if:

* Repository's owner explicitly says that "this library is not maintained".
* Not committed for a long time (2~3 years).


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
    - Blogs
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
    - Paid tutorials
    - Paid services


 ## Learning Resources
 ### Paper
 - [Attention Is All You Need](https://arxiv.org/abs/1706.03762) - Most modern LLMs rely on the transformer architecture, which is a deep neural network architecture introduced in the 2017 paper "Attention Is All You Need"
 - [TTS Papers](https://github.com/coqui-ai/TTS-papers) - Collection of TTS papers. [![Forks](https://img.shields.io/github/forks/coqui-ai/TTS-papers?style=social)](https://github.com/coqui-ai/TTS-papers/network/members) [![Stars](https://img.shields.io/github/stars/coqui-ai/TTS-papers?style=social)](https://github.com/coqui-ai/TTS-papers/stargazers)
 - [Fun Audo LLM Paper](https://funaudiollm.github.io/)
 ### Tutorials 
 - [Let's build GPT: from scratch, in code, spelled out.](https://www.youtube.com/watch?v=kCc8FmEb1nY)
 - [Create a Large Language Model from Scratch with Python – Tutorial](https://www.youtube.com/watch?v=UU1WVnMk4E8)
 - [HuggingFace Audio Deeplearning Course](https://huggingface.co/learn/audio-course/chapter0/introduction)
 - Microsoft free courses
     - [Generative AI for Beginners by Microsoft](https://github.com/microsoft/generative-ai-for-beginners) - [Video](https://learn.microsoft.com/en-us/shows/generative-ai-for-beginners/) [![Forks](https://img.shields.io/github/forks/microsoft/generative-ai-for-beginners?style=social)](https://github.com/microsoft/generative-ai-for-beginners/network/members) [![Stars](https://img.shields.io/github/stars/microsoft/generative-ai-for-beginners?style=social)](https://github.com/microsoft/generative-ai-for-beginners/stargazers)
     - [ML for Beginners](https://github.com/microsoft/ML-For-Beginners)
     - [AI for Beginners](https://microsoft.github.io/AI-For-Beginners/)
     - [Mastering GitHub Copilot for AI Paired Programming](https://github.com/microsoft/Mastering-GitHub-Copilot-for-Paired-Programming)
 - [llama3-from-scratch](https://github.com/naklecha/llama3-from-scratch) - llama3 implementation one matrix multiplication at a time [![Forks](https://img.shields.io/github/forks/naklecha/llama3-from-scratch?style=social)](https://github.com/naklecha/llama3-from-scratch/network/members) [![Stars](https://img.shields.io/github/stars/naklecha/llama3-from-scratch?style=social)](https://github.com/naklecha/llama3-from-scratch/stargazers)
 - [Build a Large Language Model from Scratch](https://github.com/rasbt/LLMs-from-scratch)
 - [Simple Guide to Local LLM Fine tuning on a Mac with MLX](https://apeatling.com/articles/simple-guide-to-local-llm-fine-tuning-on-a-mac-with-mlx/)
 - [Elasticsearch Labs](https://github.com/elastic/elasticsearch-labs) - Notebooks & Example Apps for Search & AI Applications with Elasticsearch. [![Forks](https://img.shields.io/github/forks/elastic/elasticsearch-labs?style=social)](https://github.com/elastic/elasticsearch-labs/network/members) [![Stars](https://img.shields.io/github/stars/elastic/elasticsearch-labs?style=social)](https://github.com/elastic/elasticsearch-labs/stargazers)

### blogs
* [Introducing Voicebox: The first generative AI model for speech to generalize across tasks with state-of-the-art performance](https://ai.meta.com/blog/voicebox-generative-ai-model-speech/)  
### books
- Build a Large Language Model (From Scratch) - [Free Chapters]
- Generative AI in Action - [Free Chapters]

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
## Benchmark 
- [llm-colosseum](https://github.com/OpenGenerativeAI/llm-colosseum) - Benchmark LLMs by fighting in Street Fighter 3! The new way to evaluate the quality of an LLM. [![Forks](https://img.shields.io/github/forks/OpenGenerativeAI/llm-colosseum?style=social)](https://github.com/OpenGenerativeAI/llm-colosseum/network/members) [![Stars](https://img.shields.io/github/stars/OpenGenerativeAI/llm-colosseum?style=social)](https://github.com/OpenGenerativeAI/llm-colosseum/stargazers)
## Tools & Frameworks
### ML
- [Pytorch](https://github.com/pytorch/pytorch) - Tensors and Dynamic neural networks in Python with strong GPU acceleration. [![Forks](https://img.shields.io/github/forks/pytorch/pytorch?style=social)](https://github.com/pytorch/pytorch/network/members) [![Stars](https://img.shields.io/github/stars/pytorch/pytorch?style=social)](https://github.com/pytorch/pytorch/stargazers)
- [Tensorflow](https://github.com/tensorflow/tensorflow) - An Open Source Machine Learning Framework for Everyone. [![Forks](https://img.shields.io/github/forks/tensorflow/tensorflow?style=social)](https://github.com/tensorflow/tensorflow/network/members) [![Stars](https://img.shields.io/github/stars/tensorflow/tensorflow?style=social)](https://github.com/tensorflow/tensorflow/stargazers)
- [MLX](https://github.com/ml-explore/mlx) - An array framework for Apple silicon. [![Forks](https://img.shields.io/github/forks/ml-explore/mlx?style=social)](https://github.com/ml-explore/mlx/network/members) [![Stars](https://img.shields.io/github/stars/ml-explore/mlx?style=social)](https://github.com/ml-explore/mlx/stargazers)
   - [MLX-Examples]() - Examples in the MLX Framework.
### Development Frameworks
- [Langchain](https://github.com/langchain-ai/langchain) - Build context-aware reasoning applications. [![Forks](https://img.shields.io/github/forks/langchain-ai/langchain?style=social)](https://github.com/langchain-ai/langchain/network/members) [![Stars](https://img.shields.io/github/stars/langchain-ai/langchain?style=social)](https://github.com/langchain-ai/langchain/stargazers)
- [LamaIndex](https://github.com/run-llama/llama_index) - LlamaIndex is a data framework for your LLM applications. [![Forks](https://img.shields.io/github/forks/run-llama/llama_index?style=social)](https://github.com/run-llama/llama_index/network/members) [![Stars](https://img.shields.io/github/stars/run-llama/llama_index?style=social)](https://github.com/run-llama/llama_index/stargazers)
- [Flowise](https://github.com/FlowiseAI/Flowise) - Drag & drop UI to build your customized LLM flow. [![Forks](https://img.shields.io/github/forks/FlowiseAI/Flowise?style=social)](https://github.com/FlowiseAI/Flowise/network/members) [![Stars](https://img.shields.io/github/stars/FlowiseAI/Flowise?style=social)](https://github.com/FlowiseAI/Flowise/stargazers)
- [AutoGen](https://github.com/microsoft/autogen) - A programming framework for agentic AI.  [![Forks](https://img.shields.io/github/forks/microsoft/autogen?style=social)](https://github.com/microsoft/autogen/network/members) [![Stars](https://img.shields.io/github/stars/microsoft/autogen?style=social)](https://github.com/microsoft/autogen/stargazers)
- [Auto-GPT](https://github.com/Significant-Gravitas/AutoGPT) - AutoGPT is the vision of accessible AI for everyone, to use and to build on. Our mission is to provide the tools, so that you can focus on what matters. [![Forks](https://img.shields.io/github/forks/Significant-Gravitas/AutoGPT?style=social)](https://github.com/Significant-Gravitas/AutoGPT/network/members) [![Stars](https://img.shields.io/github/stars/Significant-Gravitas/AutoGPT?style=social)](https://github.com/Significant-Gravitas/AutoGPT/stargazers)
- [AgentGPT](https://github.com/reworkd/AgentGPT) - Assemble, configure, and deploy autonomous AI Agents in your browser. [![Forks](https://img.shields.io/github/forks/reworkd/AgentGPT?style=social)](https://github.com/reworkd/AgentGPT/network/members) [![Stars](https://img.shields.io/github/stars/reworkd/AgentGPT?style=social)](https://github.com/reworkd/AgentGPT/stargazers)
- [dify](https://github.com/langgenius/dify) - Dify is an open-source LLM app development platform. Dify's intuitive interface combines AI workflow, RAG pipeline, agent capabilities, model management, observability features and more, letting you quickly go from prototype to production. [![Forks](https://img.shields.io/github/forks/langgenius/dify?style=social)](https://github.com/langgenius/dify/network/members) [![Stars](https://img.shields.io/github/stars/langgenius/dify?style=social)](https://github.com/langgenius/dify/stargazers)
- [DB-GPT](https://github.com/eosphoros-ai/DB-GPT) - AI Native Data App Development framework with AWEL(Agentic Workflow Expression Language) and Agents. [![Forks](https://img.shields.io/github/forks/eosphoros-ai/DB-GPT?style=social)](https://github.com/eosphoros-ai/DB-GPT/network/members) [![Stars](https://img.shields.io/github/stars/eosphoros-ai/DB-GPT?style=social)](https://github.com/eosphoros-ai/DB-GPT/stargazers)
- [AutoDev](https://github.com/unit-mesh/auto-dev) - AutoDev: The AI-powered coding wizard with multilingual support 🌐, auto code generation 🏗️, and a helpful bug-slaying assistant ! Customizable prompts and a magic Auto Dev/Testing/Document/Agent feature included!  [![Forks](https://img.shields.io/github/forks/unit-mesh/auto-dev?style=social)](https://github.com/unit-mesh/auto-dev/network/members) [![Stars](https://img.shields.io/github/stars/unit-mesh/auto-dev?style=social)](https://github.com/unit-mesh/auto-dev/stargazers)
- [AgentKit](https://github.com/BCG-X-Official/agentkit) - Starter-kit to build constrained agents with Nextjs, FastAPI and Langchain.   [![Forks](https://img.shields.io/github/forks/BCG-X-Official/agentkit?style=social)](https://github.com/BCG-X-Official/agentkit/network/members) [![Stars](https://img.shields.io/github/stars/BCG-X-Official/agentkit?style=social)](https://github.com/BCG-X-Official/agentkit/stargazers)
- [GraphRAG](https://github.com/microsoft/graphrag) - A modular graph-based Retrieval-Augmented Generation (RAG) system. [![Forks](https://img.shields.io/github/forks/microsoft/graphrag?style=social)](https://github.com/microsoft/graphrag/network/members) [![Stars](https://img.shields.io/github/stars/microsoft/graphrag?style=social)](https://github.com/microsoft/graphrag/stargazers)

### Open-source projects
#### TTS
- [Whisper](https://github.com/openai/whisper) - Robust Speech Recognition via Large-Scale Weak Supervision. [![Forks](https://img.shields.io/github/forks/openai/whisper?style=social)](https://github.com/openai/whisper/network/members) [![Stars](https://img.shields.io/github/stars/openai/whisper?style=social)](https://github.com/openai/whisper/stargazers)
- [Whisper Streamming](https://github.com/ufal/whisper_streaming) - Whisper realtime streaming for long speech-to-text transcription and translation. [![Forks](https://img.shields.io/github/forks/ufal/whisper_streaming?style=social)](https://github.com/ufal/whisper_streaming/network/members) [![Stars](https://img.shields.io/github/stars/ufal/whisper_streaming?style=social)](https://github.com/ufal/whisper_streaming/stargazers)
- [Faster Whisper](https://github.com/SYSTRAN/faster-whisper) - Faster Whisper transcription with CTranslate2. [![Forks](https://img.shields.io/github/forks/SYSTRAN/faster-whisper?style=social)](https://github.com/SYSTRAN/faster-whisper/network/members) [![Stars](https://img.shields.io/github/stars/SYSTRAN/faster-whisper?style=social)](https://github.com/SYSTRAN/faster-whisper/stargazers)
- [OpenVoice](https://github.com/myshell-ai/OpenVoice) - a versatile instant voice cloning approach that requires only a short audio clip from the reference speaker to replicate their voice and generate speech in multiple languages. [![Forks](https://img.shields.io/github/forks/myshell-ai/OpenVoice?style=social)](https://github.com/myshell-ai/OpenVoice/network/members) [![Stars](https://img.shields.io/github/stars/myshell-ai/OpenVoice?style=social)](https://github.com/myshell-ai/OpenVoice/stargazers)
- [ChatTTS](https://github.com/2noise/ChatTTS) - A generative speech model for daily dialogue. [![Forks](https://img.shields.io/github/forks/2noise/ChatTTS?style=social)](https://github.com/2noise/ChatTTS/network/members) [![Stars](https://img.shields.io/github/stars/2noise/ChatTTS?style=social)](https://github.com/2noise/ChatTTS/stargazers)
- [Coqui TTS](https://github.com/coqui-ai/TTS) - A deep learning toolkit for Text-to-Speech, battle-tested in research and production. [![Forks](https://img.shields.io/github/forks/coqui-ai/TTS?style=social)](https://github.com/coqui-ai/TTS/network/members) [![Stars](https://img.shields.io/github/stars/coqui-ai/TTS?style=social)](https://github.com/coqui-ai/TTS/stargazers)
- [Coqui STT Models](https://github.com/coqui-ai/STT-models) - Open models for Coqui STT. [![Forks](https://img.shields.io/github/forks/coqui-ai/STT-models?style=social)](https://github.com/coqui-ai/STT-models/network/members) [![Stars](https://img.shields.io/github/stars/coqui-ai/STT-models?style=social)](https://github.com/coqui-ai/STT-models/stargazers)
- [RealtimeTTS](https://github.com/KoljaB/RealtimeTTS) - https://github.com/KoljaB/RealtimeTTS. [![Forks](https://img.shields.io/github/forks/KoljaB/RealtimeTTS?style=social)](https://github.com/KoljaB/RealtimeTTS/network/members) [![Stars](https://img.shields.io/github/stars/KoljaB/RealtimeTTS?style=social)](https://github.com/KoljaB/RealtimeTTS/stargazers)
- [MockingBird](https://github.com/babysor/MockingBird) - Clone a voice in 5 seconds to generate arbitrary speech in real-time. [![Forks](https://img.shields.io/github/forks/babysor/MockingBird?style=social)](https://github.com/babysor/MockingBird/network/members) [![Stars](https://img.shields.io/github/stars/babysor/MockingBird?style=social)](https://github.com/babysor/MockingBird/stargazers)
- [GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS) -1 min voice data can also be used to train a good TTS model! (few shot voice cloning).
- [EmotiVoice](https://github.com/netease-youdao/EmotiVoice) - https://github.com/netease-youdao/EmotiVoice. [![Forks](https://img.shields.io/github/forks/netease-youdao/EmotiVoice?style=social)](https://github.com/netease-youdao/EmotiVoice/network/members) [![Stars](https://img.shields.io/github/stars/netease-youdao/EmotiVoice?style=social)](https://github.com/netease-youdao/EmotiVoice/stargazers)
- [NeMo](https://github.com/NVIDIA/NeMo) - A scalable generative AI framework built for researchers and developers working on Large Language Models, Multimodal, and Speech AI (Automatic Speech Recognition and Text-to-Speech). [![Forks](https://img.shields.io/github/forks/NVIDIA/NeMo?style=social)](https://github.com/NVIDIA/NeMo/network/members) [![Stars](https://img.shields.io/github/stars/NVIDIA/NeMo?style=social)](https://github.com/NVIDIA/NeMo/stargazers)
- [Vits](https://github.com/jaywalnut310/vits) -  Conditional Variational Autoencoder with Adversarial Learning for End-to-End Text-to-Speech. [![Forks](https://img.shields.io/github/forks/jaywalnut310/vits?style=social)](https://github.com/jaywalnut310/vits/network/members) [![Stars](https://img.shields.io/github/stars/jaywalnut310/vits?style=social)](https://github.com/jaywalnut310/vits/stargazers)
- [tacotron](https://github.com/keithito/tacotron) - A TensorFlow implementation of Google's Tacotron speech synthesis with pre-trained model (unofficial). [![Forks](https://img.shields.io/github/forks/keithito/tacotron?style=social)](https://github.com/keithito/tacotron/network/members) [![Stars](https://img.shields.io/github/stars/keithito/tacotron?style=social)](https://github.com/keithito/tacotron/stargazers)
- [tacotron2](https://github.com/NVIDIA/tacotron2) - PyTorch implementation with faster-than-realtime inference. [![Forks](https://img.shields.io/github/forks/NVIDIA/tacotron2?style=social)](https://github.com/NVIDIA/tacotron2/network/members) [![Stars](https://img.shields.io/github/stars/NVIDIA/tacotron2?style=social)](https://github.com/NVIDIA/tacotron2/stargazers)
- [FastSpeech](https://github.com/ming024/FastSpeech2) - An implementation of Microsoft's "FastSpeech 2: Fast and High-Quality End-to-End Text to Speech. [![Forks](https://img.shields.io/github/forks/ming024/FastSpeech2?style=social)](https://github.com/ming024/FastSpeech2/network/members) [![Stars](https://img.shields.io/github/stars/ming024/FastSpeech2?style=social)](https://github.com/ming024/FastSpeech2/stargazers)
- [VALL-E-X](https://github.com/Plachtaa/VALL-E-X) - An open source implementation of Microsoft's VALL-E X zero-shot TTS model. [![Forks](https://img.shields.io/github/forks/Plachtaa/VALL-E-X?style=social)](https://github.com/Plachtaa/VALL-E-X/network/members) [![Stars](https://img.shields.io/github/stars/Plachtaa/VALL-E-X?style=social)](https://github.com/Plachtaa/VALL-E-X/stargazers)
- [SenseVoice](https://github.com/FunAudioLLM/SenseVoice) - Multilingual Voice Understanding Model. [![Forks](https://img.shields.io/github/forks/FunAudioLLM/SenseVoice?style=social)](https://github.com/FunAudioLLM/SenseVoice/network/members) [![Stars](https://img.shields.io/github/stars/FunAudioLLM/SenseVoice?style=social)](https://github.com/FunAudioLLM/SenseVoice/stargazers)
- [CosyVoice]([https://github.com/FunAudioLLM/SenseVoice](https://github.com/FunAudioLLM/CosyVoice)) - Multi-lingual large voice generation model, providing inference, training and deployment full-stack ability.


### Clothing(Visual Try on)
- [IDM-VTON](https://github.com/yisol/IDM-VTON) - IDM-VTON : Improving Diffusion Models for Authentic Virtual Try-on in the Wild. [![Forks](https://img.shields.io/github/forks/yisol/IDM-VTON?style=social)](https://github.com/yisol/IDM-VTON/network/members) [![Stars](https://img.shields.io/github/stars/yisol/IDM-VTON?style=social)](https://github.com/yisol/IDM-VTON/stargazers)
- [MagicClothing](https://github.com/ShineChen1024/MagicClothing) - Official implementation of Magic Clothing: Controllable Garment-Driven Image Synthesis. [![Forks](https://img.shields.io/github/forks/ShineChen1024/MagicClothing?style=social)](https://github.com/ShineChen1024/MagicClothing/network/members) [![Stars](https://img.shields.io/github/stars/ShineChen1024/MagicClothing?style=social)](https://github.com/ShineChen1024/MagicClothing/stargazers)
- [StableVITON](https://github.com/rlawjdghek/StableVITON) - [CVPR2024] StableVITON: Learning Semantic Correspondence with Latent Diffusion Model for Virtual Try-On. [![Forks](https://img.shields.io/github/forks/rlawjdghek/StableVITON?style=social)](https://github.com/rlawjdghek/StableVITON/network/members) [![Stars](https://img.shields.io/github/stars/rlawjdghek/StableVITON?style=social)](https://github.com/rlawjdghek/StableVITON/stargazers)
- [HR Viton](https://github.com/sangyun884/HR-VITON) - Official PyTorch implementation for the paper High-Resolution Virtual Try-On with Misalignment and Occlusion-Handled Conditions (ECCV 2022). [![Forks](https://img.shields.io/github/forks/sangyun884/HR-VITON?style=social)](https://github.com/sangyun884/HR-VITON/network/members) [![Stars](https://img.shields.io/github/stars/sangyun884/HR-VITON?style=social)](https://github.com/sangyun884/HR-VITON/stargazers)
- [Dressing in order](https://github.com/cuiaiyu/dressing-in-order) - (ICCV'21) Official code of "Dressing in Order: Recurrent Person Image Generation for Pose Transfer, Virtual Try-on and Outfit Editing" by Aiyu Cui, Daniel McKee and Svetlana Lazebnik [![Forks](https://img.shields.io/github/forks/cuiaiyu/dressing-in-order?style=social)](https://github.com/cuiaiyu/dressing-in-order/network/members) [![Stars](https://img.shields.io/github/stars/cuiaiyu/dressing-in-order?style=social)](https://github.com/cuiaiyu/dressing-in-order/stargazers)
- [Dress Code](https://github.com/aimagelab/dress-code) - Dress Code: High-Resolution Multi-Category Virtual Try-On. ECCV 2022.  [![Forks](https://img.shields.io/github/forks/aimagelab/dress-code?style=social)](https://github.com/aimagelab/dress-code/network/members) [![Stars](https://img.shields.io/github/stars/aimagelab/dress-code?style=social)](https://github.com/aimagelab/dress-code/stargazers)
### Agent
- [BabyAGI](https://github.com/yoheinakajima/babyagi) - Python script that acts as an AI-powered task manager. [![Forks](https://img.shields.io/github/forks/yoheinakajima/babyagi?style=social)](https://github.com/yoheinakajima/babyagi/network/members) [![Stars](https://img.shields.io/github/stars/yoheinakajima/babyagi?style=social)](https://github.com/yoheinakajima/babyagi/stargazers)
- [SWE-agent](https://github.com/princeton-nlp/SWE-agent) - SWE-agent takes a GitHub issue and tries to automatically fix it, using GPT-4, or your LM of choice. It solves 12.47% of bugs in the SWE-bench evaluation set and takes just 1 minute to run. [![Forks](https://img.shields.io/github/forks/princeton-nlp/SWE-agent?style=social)](https://github.com/princeton-nlp/SWE-agent/network/members) [![Stars](https://img.shields.io/github/stars/princeton-nlp/SWE-agent?style=social)](https://github.com/princeton-nlp/SWE-agent/stargazers)
### Virtual Human
[MuseV](https://github.com/TMElyralab/MuseV) - MuseV: Infinite-length and High Fidelity Virtual Human Video Generation with Visual Conditioned Parallel Denoising by Tencent [![Forks](https://img.shields.io/github/forks/TMElyralab/MuseV?style=social)](https://github.com/TMElyralab/MuseV/network/members) [![Stars](https://img.shields.io/github/stars/TMElyralab/MuseV?style=social)](https://github.com/TMElyralab/MuseV/stargazers)

### Text2SQL
- [Vanna](https://github.com/vanna-ai/vanna) - Chat with your SQL database 📊. Accurate Text-to-SQL Generation via LLMs using RAG. [![Forks](https://img.shields.io/github/forks/vanna-ai/vanna?style=social)](https://github.com/vanna-ai/vanna/network/members) [![Stars](https://img.shields.io/github/stars/vanna-ai/vanna?style=social)](https://github.com/vanna-ai/vanna/stargazers)
- [SQLCoder](https://github.com/defog-ai/sqlcoder) - SoTA LLM for converting natural language questions to SQL queries. [![Forks](https://img.shields.io/github/forks/defog-ai/sqlcoder?style=social)](https://github.com/defog-ai/sqlcoder/network/members) [![Stars](https://img.shields.io/github/stars/defog-ai/sqlcoder?style=social)](https://github.com/defog-ai/sqlcoder/stargazers)
- [SQLChat](https://github.com/sqlchat/sqlchat) - Chat-based SQL Client and Editor for the next decade. [![Forks](https://img.shields.io/github/forks/sqlchat/sqlchat?style=social)](https://github.com/sqlchat/sqlchat/network/members) [![Stars](https://img.shields.io/github/stars/sqlchat/sqlchat?style=social)](https://github.com/sqlchat/sqlchat/stargazers)
- [Dataherald](https://github.com/Dataherald/dataherald) - Interact with your SQL database, Natural Language to SQL using LLMs. [![Forks](https://img.shields.io/github/forks/Dataherald/dataherald?style=social)](https://github.com/Dataherald/dataherald/network/members) [![Stars](https://img.shields.io/github/stars/Dataherald/dataherald?style=social)](https://github.com/Dataherald/dataherald/stargazers)
- [WrenAI](https://github.com/Canner/WrenAI) - Wren AI makes your database RAG-ready. Implement Text-to-SQL more accurately and securely. [![Forks](https://img.shields.io/github/forks/Canner/WrenAI?style=social)](https://github.com/Canner/WrenAI/network/members) [![Stars](https://img.shields.io/github/stars/Canner/WrenAI?style=social)](https://github.com/Canner/WrenAI/stargazers)
### Deep Fake
- [SadTalker](https://github.com/OpenTalker/SadTalker) - SadTalker：Learning Realistic 3D Motion Coefficients for Stylized Audio-Driven Single Image Talking Face Animation. [![Forks](https://img.shields.io/github/forks/OpenTalker/SadTalker?style=social)](https://github.com/OpenTalker/SadTalker/network/members) [![Stars](https://img.shields.io/github/stars/OpenTalker/SadTalker?style=social)](https://github.com/OpenTalker/SadTalker/stargazers)
- [Facefusion](https://github.com/facefusion/facefusion) - Next generation face swapper and enhancer. [![Forks](https://img.shields.io/github/forks/facefusion/facefusion?style=social)](https://github.com/facefusion/facefusion/network/members) [![Stars](https://img.shields.io/github/stars/facefusion/facefusion?style=social)](https://github.com/facefusion/facefusion/stargazers)
- [Ghost](https://github.com/ai-forever/ghost) - A new one shot face swap approach for image and video domains. [![Forks](https://img.shields.io/github/forks/ai-forever/ghost?style=social)](https://github.com/ai-forever/ghost/network/members) [![Stars](https://img.shields.io/github/stars/ai-forever/ghost?style=social)](https://github.com/ai-forever/ghost/stargazers)
- [](https://github.com/OpenTalker/video-retalking) - [SIGGRAPH Asia 2022] VideoReTalking: Audio-based Lip Synchronization for Talking Head Video Editing In the Wild. [![Forks](https://img.shields.io/github/forks/OpenTalker/video-retalking?style=social)](https://github.com/OpenTalker/video-retalking/network/members) [![Stars](https://img.shields.io/github/stars/OpenTalker/video-retalking?style=social)](https://github.com/OpenTalker/video-retalking/stargazers)
- [Fay](https://github.com/xszyou/Fay) - Fay is an open-source digital human framework integrating language models and digital characters. It offers retail, assistant, and agent versions for diverse applications like virtual shopping guides, broadcasters, assistants, waiters, teachers, and voice or text-based mobile assistants. [![Forks](https://img.shields.io/github/forks/xszyou/Fay?style=social)](https://github.com/xszyou/Fay/network/members) [![Stars](https://img.shields.io/github/stars/xszyou/Fay?style=social)](https://github.com/xszyou/Fay/stargazers)
