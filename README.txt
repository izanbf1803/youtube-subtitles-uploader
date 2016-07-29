Abre "C:\Python34\Lib\site-packages\googleapiclient\discovery.py"
Ves a la linea 747

Remplaza "(media_mime_type, encoding) = mimetypes.guess_type(media_filename)" por esto:

	(media_mime_type, encoding) = mimetypes.guess_type(media_filename)
        media_mime_type = "*/*" ##############################################
       