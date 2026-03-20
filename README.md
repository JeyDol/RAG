# RAG Service

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.135-green)
![PyTorch](https://img.shields.io/badge/PyTorch-sentence--transformers-red)
![ChromaDB](https://img.shields.io/badge/ChromaDB-1.5-orange)

REST API сервис на базе RAG (Retrieval-Augmented Generation). Загружаешь любой текст, задаёшь вопросы - сервис находит релевантные части текста и отдаёт их в GigaChat, который формирует ответ на основе твоих данных, а не общих знаний модели.

## Как это работает

При загрузке текст нарезается на чанки, каждый чанк превращается в вектор через sentence-transformers и сохраняется в ChromaDB. При вопросе — вопрос тоже становится вектором, ChromaDB находит самые похожие чанки, они передаются в GigaChat вместе с вопросом и модель отвечает строго на основе этих данных.

## Стек

- **FastAPI** - REST API
- **sentence-transformers (PyTorch)** - генерация эмбеддингов
- **ChromaDB** - векторная база данных
- **GigaChat API** - языковая модель

## Установка

```bash
git clone .....
cd rag-service
poetry install --no-root
