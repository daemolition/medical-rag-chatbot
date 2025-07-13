# App-Folder Dokumentation

Der App-Folder enthält die wichtigsten Bestandteile des Projekts.

## Komponenten

* **data_loader.py**: Lädt PDF-Dateien und erstellt eine Vectorestore-Datenbank.
* **embeddings.py**: Initialisiert und lädt ein HuggingFace-Embeddings-Modell.
* **llm.py**: Lädt ein LLM-Modell.
* **pdf_loader.py**: Lädt PDF-Dateien und erstellt eine Liste von Dokumenten.
* **retriever.py**: Erstellt eine QA-Chain mit dem LLM-Modell und der Vectorestore-Datenbank.

### data_loader.py

* **process_and_store_pdfs()**: Lädt PDF-Dateien, erstellt Text-Bausteine und speichert sie in der Vectorestore-Datenbank.

### embeddings.py

* **get_embedding_model()**: Initialisiert und lädt ein HuggingFace-Embeddings-Modell.

### llm.py

* **load_llm()**: Lädt ein LLM-Modell.

### pdf_loader.py

* **load_pdf_files()**: Lädt PDF-Dateien und erstellt eine Liste von Dokumenten.

### retriever.py

* **create_qa_chain()**: Erstellt eine QA-Chain mit dem LLM-Modell und der Vectorestore-Datenbank.

### custom_exception.py

* **CustomException()**: Eine benutzerdefinierte Ausnahme-Klasse mit detaillierten Fehlerinformationen.

### logger.py

* **get_logger()**: Eine Funktion, die einen Logger erstellt.

### vectorestore.py

* **save_vectore_store()**: Speichert die Vectorestore-Datenbank.
* **load_vectore_store()**: Lädt die Vectorestore-Datenbank.