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

# Metabolites of GLYCK
metabolites = [met.id for met in model.reactions.GLYCK.metabolites]

# remove GLYCK
print(model.reactions.GLYCK.reaction)
print(model.reactions.GLYCK2.reaction)
model.remove_reactions(['GLYCK'])

# Check other reactions for GLYCK metabolites
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
# 3pg_c -> Produced by: 2 reactions, Consumed by: 2 reactions
# adp_c -> Produced by: 279 reactions, Consumed by: 8 reactions
# atp_c -> Produced by: 4 reactions, Consumed by: 345 reactions
# glyc__R_c -> Produced by: 5 reactions, Consumed by: 2 reactions
# h_c -> Produced by: 786 reactions, Consumed by: 293 reactions
# Conclusion: No dead-end reactions produced, keep all metabolites

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


