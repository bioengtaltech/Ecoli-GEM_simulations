import cobra
from rebuild_groups import rebuild_groups_from_subsystems

# Load and rebuild model
model_path = 'path_to_repository/Ecoli-GEM/model/Ecoli-GEM.yml'
model = cobra.io.load_yaml_model(model_path)
rebuild_groups_from_subsystems(model)

# Metabolites of XYLI2
metabolites = [met.id for met in model.reactions.XYLI2.metabolites]

# remove XYLI2
print(model.reactions.XYLI2.reaction)
print(model.reactions.XYLI1.reaction)
model.remove_reactions(['XYLI2'])

# Check other reactions for XYLI2 metabolites
for met_id in metabolites:
    met = model.metabolites.get_by_id(met_id)
    print(f"\nMetabolite: {met.id} ({met.name})")
    for rxn in met.reactions:
        print(f" - {rxn.id}: {rxn.reaction}")

def orphan_check(met_id):
    met = model.metabolites.get_by_id(met_id)
    producing = [r for r in met.reactions if met in r.products]
    consuming = [r for r in met.reactions if met in r.reactants]
    print(f"\n{met_id} -> Produced by: {len(producing)} reactions, Consumed by: {len(consuming)} reactions")

for met_id in metabolites:
    orphan_check(met_id)
# Metabolite results
# fru_c -> Produced by: 2 reactions, Consumed by: 1 reactions
# glc__D_c -> Produced by: 19 reactions, Consumed by: 2 reactions
# Conclusion: No dead-end reactions produced, keep all metabolites

# Save model
output_path='path_to_output_dir/Ecoli-GEM.yml'
cobra.io.save_yaml_model(model, output_path, sort='True')


