import streamlit as st
from Bio.PDB import PDBList
import py3Dmol
import os

def download_pdb(pdb_id):
    pdbl = PDBList()
    file_path = pdbl.retrieve_pdb_file(pdb_id, pdir='.', file_format='pdb')
    return file_path

def render_3d_structure(pdb_id, file_path):
    with open(file_path, "r") as f:
        pdb_data = f.read()
    view = py3Dmol.view(width=800, height=600)
    view.addModel(pdb_data, "pdb")
    view.setStyle({'cartoon': {'color': 'spectrum'}})
    view.zoomTo()
    return view

st.title("3D Molecule Viewer")

pdb_id = st.text_input("Enter PDB ID:", "1BNA")

if st.button("Show 3D Structure"):
    try:
        file_path = download_pdb(pdb_id)
        if not os.path.exists(file_path):
            st.error(f"File {file_path} does not exist.")
        else:
            view = render_3d_structure(pdb_id, file_path)
            st.subheader("3D Structure")
            with st.spinner('Rendering...'):
                st.components.v1.html(view._make_html(), height=600)
    except Exception as e:
        st.error(f"An error occurred: {e}")

