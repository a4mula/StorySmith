---

**Story Smith: Style Guide**

This document outlines the standards for writing and formatting code, naming conventions, and maintaining consistency throughout the project.

---

## **1. Code Formatting**

Adhere to [PEP 8](https://peps.python.org/pep-0008/), the Python style guide. Key points include:

### **1.1. Indentation**

- Use 4 spaces for indentation. Do not use tabs.

### **1.2. Line Length**

- Limit all lines to a maximum of 79 characters. For docstrings and comments, limit lines to 72 characters.

### **1.3. Blank Lines**

- Use blank lines to separate sections of code:
    - Two blank lines between top-level functions and class definitions.
    - One blank line between methods inside a class.

### **1.4. Imports**

- Import one module per line.
- Group imports in the following order:
    1. Standard library imports.
    2. Related third-party imports.
    3. Local application-specific imports.
- Example:
    
    ```python
    import os
    import sys
    
    import pygame
    
    from game.utils import clamp
    
    ```
    

---

## **2. Naming Conventions**

### **2.1. Variables**

- Use `snake_case` for variable names.
    
    ```python
    player_health = 100
    
    ```
    

### **2.2. Functions**

- Use `snake_case` for function names.
    
    ```python
    def calculate_damage():
        pass
    
    ```
    

### **2.3. Classes**

- Use `PascalCase` for class names.
    
    ```python
    class PlayerCharacter:
        pass
    
    ```
    

### **2.4. Constants**

- Use `UPPER_CASE` for constants, typically defined in `constants.py`.
    
    ```python
    MAX_HEALTH = 150
    
    ```
    

### **2.5. Modules**

- Use `snake_case` for file and folder names.
    
    ```
    ui.py
    stage_manager.py
    
    ```
    

---

## **3. Comments and Docstrings**

### **3.1. Comments**

- Use comments sparingly to clarify non-obvious code. Avoid stating the obvious:
    
    ```python
    # Good
    # Calculate bonus points for critical hits
    critical_bonus = base_damage * 1.5
    
    # Bad
    # Assign critical bonus points
    critical_bonus = base_damage * 1.5
    
    ```
    

### **3.2. Docstrings**

- Use triple double quotes for docstrings.
- All public functions, classes, and modules must include docstrings.
- Example:
    
    ```python
    def calculate_damage(base_damage, multiplier):
        """
        Calculate the total damage based on base damage and multiplier.
    
        Args:
            base_damage (int): The base damage value.
            multiplier (float): The multiplier for critical hits.
    
        Returns:
            int: The total damage dealt.
        """
        return int(base_damage * multiplier)
    
    ```
    

---

## **4. Folder and File Structure**

### **4.1. Folder Organization**

- Group related files in logical directories:
    
    ```
    assets/
    game/
    tests/
    docs/
    
    ```
    

### **4.2. File Naming**

- Use `snake_case` for all filenames:
    
    ```
    ui.py
    boss.py
    
    ```
    

---

## **5. Testing Standards**

- Follow the same naming conventions for test files:
    
    ```
    test_ui.py
    test_boss.py
    
    ```
    
- Use descriptive test names:
    
    ```python
    def test_boss_health_update():
        pass
    
    ```
    
- Tests must assert expected behaviors:
    
    ```python
    assert boss.health == 100
    
    ```
    

---

## **6. Version Control**

### **6.1. Commit Messages**

- Write meaningful commit messages that describe changes:
    
    ```
    Add new boss ability to boss.py
    Fix issue with class stat modification
    Update README with installation instructions
    
    ```
    

### **6.2. Branch Naming**

- Use `feature/`, `bugfix/`, or `docs/` prefixes for branch names:
    
    ```
    feature/add-ui-transitions
    bugfix/fix-stage-rendering
    docs/update-contributing-guide
    
    ```
    

---

## **7. Asset Guidelines**

### **7.1. Graphics**

- Use `.png` or `.jpg` formats.
- Maintain a consistent aspect ratio (e.g., 16:9).

### **7.2. Audio**

- Use `.wav` for looping sounds, `.mp3` for non-looping.
- Ensure audio is normalized to avoid sudden volume spikes.

### **7.3. Fonts**

- Use `.ttf` or `.otf` formats.

---

## **8. Collaboration Practices**

- Regularly pull the latest changes from the main branch.
- Run all tests before pushing changes.
- Open a pull request (PR) for code reviews.

---

## **9. Documentation**

- Ensure all new modules and features are documented in the relevant `docs/` files.
- Add comments or docstrings for non-obvious logic or complex algorithms.

---

## **10. Code Review Checklist**

Before submitting code for review:

1. Does it adhere to the style guide?
2. Are all new functions/classes documented with docstrings?
3. Have all existing and new tests passed?
4. Is the code modular and maintainable?

---
