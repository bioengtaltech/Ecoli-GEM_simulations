import os
import cobra
from rebuild_groups import rebuild_groups_from_subsystems

def export_model_formats(model_path, output_dir, output_name, formats=None):
    """
    Load a GEM model and export it to specified formats.

    Parameters:
    - model_path (str): Path to the input model (SBML, YAML).
    - output_dir (str): Directory to save the exported files.
    - output_name (str): Base filename (without extension) for exported files.
    - formats (list of str, optional): List of formats to export. Supported: 'xml', 'yml', 'json', 'mat'.
                                       If not specified, exports to all supported formats.
    """
    # Set default formats if none are provided
    if not formats:
        formats = ['xml', 'yml', 'json', 'mat']

    # Load the model
    ext = os.path.splitext(model_path)[1].lower()
    if ext == '.xml':
        model = cobra.io.read_sbml_model(model_path)
    elif ext in ['.yml', '.yaml']:
        model = cobra.io.load_yaml_model(model_path)
        # Check for empty groups field, repair if empty
        if not model.groups:
            print("Groups are empty in the model — rebuilding from subsystem information.")
            rebuild_groups_from_subsystems(model)
    else:
        raise ValueError(f"Unsupported input model format: {ext}")

    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Export to specified formats
    for fmt in formats:
        fmt = fmt.lower()
        output_path = os.path.join(output_dir, f"{output_name}.{fmt}")

        if fmt == 'xml':
            cobra.io.write_sbml_model(model, output_path)
        elif fmt in ['yml', 'yaml']:
            cobra.io.save_yaml_model(model, output_path, sort=True)
        elif fmt == 'json':
            cobra.io.save_json_model(model, output_path)
        elif fmt == 'mat':
            cobra.io.save_matlab_model(model, output_path)
        else:
            raise ValueError(f"Unsupported export format: {fmt}")

    print(f"Model exported to: {', '.join(formats)} in {output_dir}")
    
