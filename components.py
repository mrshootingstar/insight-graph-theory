def components(G): # The connected components
    comp = []
    seen = set() # Nodes we've already seen
    for u in G: # Try every starting point
        if u in seen: continue # Seen? Ignore it
        C = walk(G, u) # Traverse component
        seen.update(C) # Add keys of C to seen
        comp.append(C) # Collect the components
    return comp


comps = components(G)
comps