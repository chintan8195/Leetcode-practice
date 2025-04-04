"""
path is a / separate string describing the node. Example /Tres Potrillos/tacos/al_pastor
Values are all strings
API spec:
get(path): String -> returns the value of the node at the given path
create(path, value) -> creates a new node and sets it to the given value. 
Should error out if the node already exists or if the node’s parent does not exist. That is /Sweetgreen/naan_roll cannot be created if /Sweetgreen has not already been created
delete(path) -> deletes a node, but ONLY if it has no children
"""