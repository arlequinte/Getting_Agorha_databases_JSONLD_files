# Getting_Agorha_databases_JSONLD_files
Going through HTML with Python and BeautifulSoup library.

The public website Agorha (for the release of the Parisian Institut National d'Histoire de l'Art research projects' databases), is currently developing its API for the users to get all files together from a selected project.

Still, the beta version is not public yet, and the API only provides the users with JSON files ; though all databases include JSON-LD, .n3, .4 and .rdf files within each of their contents.

Those Python scripts were written for the purposes of an internship at the French National Library's Department of Manuscripts in 2023.
They offer a way to get the JSON-LD file from each content of the database 88, and to concat them within a single JSON-LD document. 
