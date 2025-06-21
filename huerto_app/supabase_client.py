import os
import uuid
from dotenv import load_dotenv
from supabase import create_client, Client

# Cargar variables desde .env
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def subir_imagen(file):
    nombre_archivo = f"{uuid.uuid4()}.{file.name.split('.')[-1]}"
    path = nombre_archivo
    contenido = file.read()
    content_type = file.content_type

    try:
        supabase.storage.from_("plantas").upload(
            path,
            contenido,
            file_options={"content-type": content_type}
        )
    except Exception as e:
        raise Exception(f"❌ Error al subir imagen a Supabase: {e}")

    url = f"{SUPABASE_URL}/storage/v1/object/public/plantas/{nombre_archivo}"
    print("🔗 URL generada:", url)
    return url
