import cobra
from rebuild_groups import rebuild_groups_from_subsystems

# Load and rebuild model
model_path = 'path_to_repository/Ecoli-GEM/model/Ecoli-GEM.yml'
model = cobra.io.load_yaml_model(model_path)
rebuild_groups_from_subsystems(model)

# pntAB (THD2pp)
print(model.reactions.THD2pp.reaction)
model.reactions.THD2pp.add_metabolites({"h_c": -1, "h_p": 1})
print(model.reactions.THD2pp.reaction)

# glxK (b0514) to GLYCK2 & remove GLYCK
print(model.reactions.GLYCK2.gene_reaction_rule)
model.reactions.GLYCK2.gene_reaction_rule = '(b3124 or b0514)'
print(model.reactions.GLYCK2.gene_reaction_rule)
model.remove_reactions(['GLYCK'])

# HSDy 
print(model.reactions.HSDy.bounds)
print(model.reactions.HSDy.reversibility)
print(model.reactions.HSDy.reaction)
model.reactions.HSDy.lower_bound = 0
print(model.reactions.HSDy.bounds)

# SUCCt1pp
print(model.reactions.SUCCt1pp.bounds)
print(model.reactions.SUCCt1pp.reversibility)
print(model.reactions.SUCCt1pp.reaction)
model.reactions.SUCCt1pp.lower_bound = 0
print(model.reactions.SUCCt1pp.bounds)

# Save model
output_path='path_to_output_dir/Ecoli-GEM.yml'
cobra.io.save_yaml_model(model, output_path, sort='True')


