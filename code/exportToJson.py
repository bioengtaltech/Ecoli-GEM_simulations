import cobra

def exportToJson(model_path, output_path):
    """
    Converts a GEM model from SBML (.xml) format to JSON format using CobraPy.

    Parameters:
        model_path (str): Path to the input SBML (.xml) model file.
        output_path (str): Path to save the output JSON model file.

    Example:
        convert_sbml_to_json("C:/path/to/model.xml", "C:/path/to/model.json")
    """
    try:
        # Load the model from SBML
        model = cobra.io.read_sbml_model(model_path)
        
        # Save the model in JSON format
        cobra.io.save_json_model(model, output_path)

        print(f"Successfully converted '{model_path}' to '{output_path}'.")

    except Exception as e:
        print(f"Error during conversion: {e}")

