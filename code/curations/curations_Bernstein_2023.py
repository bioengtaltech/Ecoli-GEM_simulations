import cobra
from rebuild_groups import rebuild_groups_from_subsystems

# Load and rebuild model
model_path = 'path_to_repository/Ecoli-GEM/model/Ecoli-GEM.yml'
model = cobra.io.load_yaml_model(model_path)
rebuild_groups_from_subsystems(model)

#GHMT2r irreversible
print(model.reactions.GHMT2r.bounds)
model.reactions.GHMT2r.lower_bound = 0

# Save model
output_path='path_to_output_dir/Ecoli-GEM.yml'
cobra.io.save_yaml_model(model, output_path, sort='True')


