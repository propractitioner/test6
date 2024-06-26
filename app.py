import streamlit as st
from Bio.PDB import PDBList
import py3Dmol

def download_pdb(pdb_id):
    pdbl = PDBList()
    pdbl.retrieve_pdb_file(pdb_id, pdir='.', file_format='pdb')

def render_3d_structure(pdb_id):
    with open(f"{pdb_id}.pdb", "r") as f:
        pdb_data = f.read()
    view = py3Dmol.view(width=800, height=600)
    view.addModel(pdb_data, "pdb")
    view.setStyle({'cartoon': {'color': 'spectrum'}})
    view.zoomTo()
    view.show()

st.title("3D Molecule Viewer")

pdb_id = st.text_input("Enter PDB ID:", "1BNA")

if st.button("Show 3D Structure"):
    download_pdb(pdb_id)
    render_3d_structure(pdb_id)

    st.subheader("3D Structure")
    with st.spinner('Rendering...'):
        render_3d_structure(pdb_id)
        st.components.v1.html(view._make_html(), height=600)
