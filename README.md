# Chronomancy
A Python library for re-calling methods (or class properties) from within a method that they were initially passed in as an argument for.

For those who fancy dramatic and poetic descriptions (like me)...

_"We are piercing the veil of the Stack, using echos in time to reconstruct a pathway through memory, finding their source and recasting the spell."_

## There Be Dragons
Conventional wisdom states that one should avoid doing what this library does.

This library has specific and unique aims that fall outside of convention.

What's that? You've been told never to mess with the Python call stack? "It's dangerous! There be dragons!" they shout from their ivory towers of best practices.

Well, sometimes you need to slay a dragon to get what you want. And sometimes what you want is to reach back through time to recapture the essence of what was—or rather, to access what still is but from a different point in your code's execution.

So yes, we're breaking some "rules" here. But we're doing it with style, purpose, and just enough magical metaphor to make it fun.

## The Reason for Being

Chronomancy was born out of frustration with flaky Selenium tests. When testing web applications, elements often aren't ready when your code first looks for them. The conventional solution? Clunky, repetitive retry logic that bloats your codebase.

I whipped up Chronomancy in about a day to solve this annoyance. Instead of writing the same polling pattern over and over, I wanted a clean way to simply "try again" with the original method call when dealing with state fluctuations and latency issues.

What makes Chronomancy special is that when a method or property is passed as an argument, you typically only get the evaluated result. The connection to the source is lost. Chronomancy gives you a way to reach back and re-execute or re-access that source, getting fresh results without rewriting your code.

## Installation

```bash
pip install chronomancy
```

## How to Use

Using Chronomancy is now easier than ever with the new class-based approach:

```python
# ... other imports that I don't care about right now

from chronomancy import Chronomancy

def wait_for_element(get_element_func, max_attempts=10):
    # Create a Chronomancy instance - this is your anchor in time
    chronomancy = Chronomancy()
    
    attempts = 0
    element = None
    
    while attempts < max_attempts and not element:
        try:
            # Try to get the element
            element = get_element_func()
        except:
            # Element not ready? No problem! Let's pierce the veil of time...
            sleep(0.5)
            # Re-cast the spell (re-execute the original function)
            element = chronomancy.arcane_recall()
            attempts += 1
    
    if not element:
        raise TimeoutError("Even Chronomancy has its limits. Element never appeared.")
        
    return element

# Usage in the wild
driver.get("https://example.com")
element = wait_for_element(lambda: driver.find_element(By.ID, "appears-when-it-feels-like-it"))
```

The old function-based approach is still supported, but deprecated:

```python
from chronomancy.arcane_recall import arcane_recall
import inspect

def old_style_wait(get_element_func):
    calling_frame = inspect.stack()[1]  # Manually capturing the frame (no longer needed with new approach)
    # ... do other stuff
    # ... maybe go into an if block or loop
    if get_element_func() is None:
        # Re-cast the spell (re-execute the original function)
        element = arcane_recall(calling_frame)
        # ... do more stuff
```

## Limitations

Chronomancy is powerful, but even arcane arts have their limits:

- It works with regular Python method calls and property access, but might get confused by sufficiently advanced magic (like certain metaprogramming techniques)
- It relies on inspecting the Python call stack, which means it's somewhat implementation-specific
- Like any magic dealing with time, use it wisely and in moderation

## Examples

### Retrying a Flaky API Call

```python
def get_with_retry(url, max_attempts=3):
    chronomancy = Chronomancy()
    attempts = 0
    
    while attempts < max_attempts:
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response
        except:
            sleep(1)
            attempts += 1
            response = chronomancy.arcane_recall()
    
    return response  # Return the last attempt, successful or not
```

### Working with Dynamic Properties

```python
def process_when_ready(obj, timeout=10):
    chronomancy = Chronomancy()
    start_time = time.time()
    
    while time.time() - start_time < timeout:
        if obj.is_ready:  # A property that might change over time
            return obj.process()
        
        sleep(0.5)
        # Re-check the property using the same object reference
        if chronomancy.arcane_recall():  # Recalls obj.is_ready
            return obj.process()
            
    raise TimeoutError("Object never became ready")
```

## Future Expectations

The arcane arts are never truly mastered, only improved upon. Future evolutions of Chronomancy may include:

- Enhanced capabilities to handle more complex traversal of object references
- Improved handling of edge cases in various execution contexts
- Performance improvements to make the magic even more seamless
- Additional utilities for working with time-dependent code execution

## Not Safe for Human Consumption
Use this library at your own peril. You have been warned.

I mean, it's probably fine. It's been stable since 2019 without needing changes. But if your codebase suddenly starts exhibiting strange temporal paradoxes or your tests begin summoning Lovecraftian entities from beyond the veil... well, you were warned about the dragons.

In all seriousness, Chronomancy is a tool. Like any tool that works with Python's internals, use it thoughtfully and when it truly simplifies your code, not as your default approach to every problem.

## License

MIT License - See LICENSE file for details. Feel free to wield this power, but remember: with great power comes great responsibility... and occasionally, dragons.