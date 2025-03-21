import logging
import memote_test_utils
import cobra
import memote.suite.api as memote_api

logging.basicConfig(level=logging.INFO, format="%(message)s")

# Define model directory
model_directory = "model/"

# Find model file. Requires either XML or YML file (prioritize XML)
model_path = memote_test_utils.find_model_file_path(model_directory)

# Load model (if YML, genes.tsv, mets.tsv, and rxns.tsv files are required)
if model_path.endswith(".xml"):
    model = cobra.io.read_sbml_model(model_path)
    logging.info(f"Loaded XML model: {model_path}")
elif model_path.endswith(".yml"):
    model = cobra.io.load_yaml_model(model_path)
    logging.info(f"Loaded YML model: {model_path}")

    # Load annotation files
    annotation_data = memote_test_utils.load_annotation_tsv_files(model_directory)
    # Append annotation information to model
    memote_test_utils.append_annotations(model, annotation_data["genes.tsv"], annotation_data["mets.tsv"], annotation_data["rxns.tsv"])
    
# Run memote test
_, result = memote_api.test_model(model, exclusive=None, skip=None, results=True)

# Generate html report
html_report = memote_api.snapshot_report(result)

# Save html report
report_path = 'memote_report.html'
with open(report_path, 'w', encoding='utf-8') as file:
    file.write(html_report)
