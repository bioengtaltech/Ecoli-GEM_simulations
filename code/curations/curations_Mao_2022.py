import cobra
from rebuild_groups import rebuild_groups_from_subsystems

# Load and rebuild model
model_path = 'path_to_repository/Ecoli-GEM/model/Ecoli-GEM.yml'
model = cobra.io.load_yaml_model(model_path)
rebuild_groups_from_subsystems(model)

print(model.reactions.FMNRx2.gene_reaction_rule)
# From b3844 or b0937 or (b2764 and b2763)
model.reactions.FMNRx2.gene_reaction_rule = '(b0937 or b3844 or b2764)'

print(model.reactions.ARGabcpp.gene_reaction_rule)
# From (b2308 and b2306 and b2310 and b2307) or (b0864 and b0860 and b0863 and b0862 and b0861)
model.reactions.ARGabcpp.gene_reaction_rule = '( b2310 and b2308 and b2306 and b2307 ) or ( b0862 and b0860 and b0864 and b0861 ) or ( b0862 and b0864 and b0863 and b0861 )'

print(model.reactions.ECAP1pp.gene_reaction_rule)
# From b3785 and b3793
model.reactions.ECAP1pp.gene_reaction_rule = '( b3785 and b3793 and b3792 )'

print(model.reactions.ECAP2pp.gene_reaction_rule)
# From b3785 and b3793
model.reactions.ECAP2pp.gene_reaction_rule = '( b3785 and b3793 and b3792 )'

print(model.reactions.ECAP3pp.gene_reaction_rule)
# From b3785 and b3793
model.reactions.ECAP3pp.gene_reaction_rule = '( b3785 and b3793 and b3792 )'

print(model.reactions.FADRx2.gene_reaction_rule)
# From b2764 and b2763
model.reactions.FADRx2.gene_reaction_rule = '( b2764 )'

print(model.reactions.BWCOGDS1.gene_reaction_rule)
# From (b3857 and b3856) or b3857
model.reactions.BWCOGDS1.gene_reaction_rule = '( b3857 )'

print(model.reactions.BWCOGDS2.gene_reaction_rule)
# From (b3857 and b3856) or b3857
model.reactions.BWCOGDS2.gene_reaction_rule = '( b3857 )'

print(model.reactions.THZPSN3.gene_reaction_rule)
# From b0423 and b3990 and b2530 and b3992 and b4407
model.reactions.THZPSN3.gene_reaction_rule = '( b3992 and b3990 and b0423 and b2530 and b4407 and b3991 )'

print(model.reactions.BMOGDS1.gene_reaction_rule)
# From b3857 or (b3857 and b3856)
model.reactions.BMOGDS1.gene_reaction_rule = '( b3857 )'

print(model.reactions.BMOGDS2.gene_reaction_rule)
# From (b3857 and b3856) or b3857
model.reactions.BMOGDS2.gene_reaction_rule = '( b3857 )'

print(model.reactions.MOGDS.gene_reaction_rule)
# From (b3857 and b3856) or b3857
model.reactions.MOGDS.gene_reaction_rule = '( b3857 )'

print(model.reactions.get_by_id('3NTD4pp').gene_reaction_rule)
# From b4213 or b0383 or b0383
model.reactions.get_by_id('3NTD4pp').gene_reaction_rule = '( b0383 or b4213 or b2744 )'

print(model.reactions.GLUDy.gene_reaction_rule)
# From b1761 or (b3213 and b3212)
model.reactions.GLUDy.gene_reaction_rule = '( b1761 )'

# Save model
output_path='path_to_output_dir/Ecoli-GEM.yml'
cobra.io.save_yaml_model(model, output_path, sort='True')
