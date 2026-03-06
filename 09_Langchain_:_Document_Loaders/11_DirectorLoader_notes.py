"""
DirectoryLoader

DirectoryLoader is a document loader in LangChain that allows you
to load multiple files from a directory (folder).

It scans the folder, loads the files that match a pattern,
and converts them into LangChain Document objects.

Common Glob Patterns:

"**/*.txt"  → Loads all .txt files from all subfolders
"*.pdf"     → Loads all .pdf files in the main directory
"data/*.csv"→ Loads all .csv files inside the data folder
"**/*"      → Loads all files from all folders

Note:
"**" means recursive search through subfolders.
"""