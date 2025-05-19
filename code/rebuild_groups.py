from cobra.core import Group

def rebuild_groups_from_subsystems(model):
    """
    Rebuilds groups from reaction subsystems and assigns them to the model.

    Parameters:
    - model (cobra.Model): The model to modify.
    """
    from collections import defaultdict

    # Clear any existing groups
    model.groups.clear()

    # Collect reactions by subsystem
    subsystem_to_reactions = defaultdict(list)
    for rxn in model.reactions:
        if rxn.subsystem:
            subsystem_to_reactions[rxn.subsystem].append(rxn)

    # Create groups from subsystem info
    for i, (subsystem, reactions) in enumerate(sorted(subsystem_to_reactions.items()), start=1):
        group_id = f"group{i}"
        metaid = f"meta_group{i}"
        name = subsystem

        group = Group(
            id=group_id,
            name=name,
            kind="partonomy"
        )
        group.annotation["sbo"] = "SBO:0000633"
        group.notes = {}
        #group._annotation["metaid"] = metaid  # For compatibility with XML export

        group.add_members(reactions)
        model.groups.append(group)

    print(f"Rebuilt {len(model.groups)} groups from subsystems.")

