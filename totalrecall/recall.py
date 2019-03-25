""" Recalls the method or class property used as an input parameter by the calling frame"""
import inspect
import re


def total_recall(calling_frame):
    arguments = re.compile('\\(.*\\)')

    # The setup to gain access to the calling frames method call.
    calling_code = calling_frame.code_context[0].strip('\n')
    calling_locals = calling_frame.frame.f_locals
    target_call = arguments.search(calling_code)[0].strip('\\(').strip('\\)').split(', ')[0]

    # Get a list of the total dot notation call chain from the calling frames method argument list
    target_call_attrs = target_call.split('.')

    # Reverse the call chain so we can work from the logical start point since we will never have any idea of what to expect
    target_call_attrs.reverse()

    # Get a copy of primary target that we want to eventually call/access (removing it from the call chain list)
    prime_target_id = target_call_attrs.pop(0).strip('()')

    # We'll store the string "id" of the top most level object here later
    top_level_target_id = ''

    # Our eventual dot notation call chain that we might need to iterate through.
    dot_notation_chain = []

    # Check to see if our primary target is a callable method within calling frames locals before making this more complicated than it has to be.
    if prime_target_id in calling_locals and callable(calling_locals[prime_target_id]):
        return calling_locals[prime_target_id]()
    else:
        # If we're here, we need to loop through each of the target call attributes to find the top most level object we need to access first
        for attribute in target_call_attrs:
            if attribute.strip('()') in calling_locals:
                top_level_target_id = attribute.strip('()')
                break
            else:
                # Until we find the top most level, we need to construct a chain of attributes between the top most level object and our target so we can drill down to access it.
                dot_notation_chain.append(attribute.strip('()'))

    # Store the reference to the top level object that we need to access
    top_level_object = calling_frame.frame.f_locals[top_level_target_id]

    # Check to see if the top level object has as a property our target object and return it's value if so.
    if inspect.isclass(type(top_level_object)) and hasattr(top_level_object, prime_target_id):
        return getattr(top_level_object, prime_target_id)()

    # If we've gotten this far we now need to traverse dot notation chain to drill down into the object references
    current_level_object = top_level_object
    for index, command in enumerate(dot_notation_chain):
        # Is the command a class or a callable object within the current level object we're inspecting?
        if inspect.isclass(type(getattr(current_level_object, command))) or callable(getattr(current_level_object, command)):
            # If so, store the reference to the command as the new current level object and keep digging.
            current_level_object = getattr(current_level_object, command)
        else:
            # Than the current level object must be the parent to our prime target, return the value.
            return getattr(current_level_object, prime_target_id)

    # If we're here then we've drilled down to the bottom and we can recall the original calling frames argument.
    if callable(getattr(current_level_object, prime_target_id)):
        return getattr(current_level_object, prime_target_id)()
    else:
        return getattr(current_level_object, prime_target_id)


def total_stack_recall(stack, notation_chain):
    # 1. Loop through stack frames to find the reference to the leading object in the notation chain (use is).
    # 2. When you find it, get a reference to it.
    # 3. Begin looping through the notation chain checking for hasattr and creating a new pointers.
    # 4. Keep going down until you get to the final notation chain link and call it or use getattr
    pass
