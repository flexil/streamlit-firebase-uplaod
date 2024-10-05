import streamlit as st
import firebase_admin
from firebase_admin import credentials, storage

cred = credentials.Certificate("path/to/your/serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'storageBucket': 'gs://tomato-disease-41450.appspot.com'
})
bucket = storage.client()

bucket = client.get_bucket(cred.options['storageBucket'])

# Upload a file
def upload_file(file):
    blob = bucket.blob(file.name)
    blob.upload_from_file(file)
    return blob.public_url


st.title("Firebase Storage Example")
file = st.file_uploader("Choose a file")
if file:
    url = upload_file(file)
    st.write(f"File uploaded: {url}")


