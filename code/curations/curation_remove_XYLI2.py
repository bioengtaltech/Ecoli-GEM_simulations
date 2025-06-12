import cobra
from rebuild_groups import rebuild_groups_from_subsystems

# Load and rebuild model
model_path = 'path_to_repository/Ecoli-GEM/model/Ecoli-GEM.yml'
model = cobra.io.load_yaml_model(model_path)
rebuild_groups_from_subsystems(model)

# remove XYLI2
print(model.reactions.XYLI2.reaction)
print(model.reactions.XYLI1.reaction)
model.remove_reactions(['XYLI2'])

# Save model
output_path='path_to_output_dir/Ecoli-GEM.yml'
cobra.io.save_yaml_model(model, output_path, sort='True')
